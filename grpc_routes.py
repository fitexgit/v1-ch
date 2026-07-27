# grpc_routes.py — Experimental VLESS/Trojan gRPC transport for OXNET
import asyncio
import secrets
from datetime import datetime
from typing import AsyncIterator

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse

from main import LINKS, LINKS_LOCK, connections, stats, error_logs, logger, is_link_allowed, save_state, resolve_link_id
from relay_vless import parse_vless_header, check_and_use
from trojan import parse_trojan_header, find_uuid_by_trojan_hash

router = APIRouter()

GRPC_CONTENT_TYPE = "application/grpc"


def _frame(payload: bytes) -> bytes:
    return b"\x00" + len(payload).to_bytes(4, "big") + payload


async def _grpc_messages(request: Request) -> AsyncIterator[bytes]:
    buf = b""
    async for chunk in request.stream():
        if not chunk:
            continue
        buf += chunk
        while len(buf) >= 5:
            ln = int.from_bytes(buf[1:5], "big")
            if len(buf) < 5 + ln:
                break
            msg = buf[5:5 + ln]
            buf = buf[5 + ln:]
            if msg:
                yield msg


def _client_ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real = request.headers.get("x-real-ip")
    if real:
        return real.strip()
    return request.client.host if request.client else "نامشخص"


async def _tcp_to_queue(uid: str, conn_id: str, reader: asyncio.StreamReader, queue: asyncio.Queue, prefix_vless: bool):
    first = True
    try:
        while True:
            data = await reader.read(256 * 1024)
            if not data:
                break
            if not await check_and_use(uid, len(data)):
                break
            connections[conn_id]["bytes"] += len(data)
            if prefix_vless and first:
                data = b"\x00\x00" + data
                first = False
            await queue.put(_frame(data))
    finally:
        await queue.put(None)


async def _vless_grpc_stream(request: Request, token: str):
    uid = await resolve_link_id(token)
    async with LINKS_LOCK:
        link = LINKS.get(uid) if uid else None
    if not is_link_allowed(link):
        raise HTTPException(status_code=403, detail="not authorized")

    conn_id = secrets.token_urlsafe(6)
    ip = _client_ip(request)
    connections[conn_id] = {"uuid": uid, "ip": ip, "transport": "vless-grpc", "connected_at": datetime.now().isoformat(), "bytes": 0}
    queue: asyncio.Queue = asyncio.Queue(maxsize=128)
    writer = None

    async def body():
        nonlocal writer
        try:
            gen = _grpc_messages(request)
            first_plain = await asyncio.wait_for(gen.__anext__(), timeout=20.0)
            command, address, port, payload = await parse_vless_header(first_plain)
            if command != 1:
                raise ValueError("only TCP command is supported")
            if not await check_and_use(uid, len(first_plain)):
                raise ValueError("quota/disabled")
            stats["total_requests"] += 1
            connections[conn_id]["bytes"] += len(first_plain)
            reader, writer = await asyncio.wait_for(asyncio.open_connection(address, port), timeout=10.0)
            if payload:
                writer.write(payload)
                await writer.drain()
            reader_task = asyncio.create_task(_tcp_to_queue(uid, conn_id, reader, queue, True))
            async def request_to_tcp():
                async for msg in gen:
                    if not await check_and_use(uid, len(msg)):
                        break
                    connections[conn_id]["bytes"] += len(msg)
                    writer.write(msg)
                    if writer.transport.get_write_buffer_size() > 512 * 1024:
                        await writer.drain()
                try:
                    writer.write_eof()
                except Exception:
                    pass
            writer_task = asyncio.create_task(request_to_tcp())
            while True:
                item = await queue.get()
                if item is None:
                    break
                yield item
            writer_task.cancel()
            await save_state()
        except Exception as exc:
            stats["total_errors"] += 1
            error_logs.append({"error": f"vless-grpc: {exc}", "time": datetime.now().isoformat()})
            logger.error(f"VLESS-gRPC error [{conn_id}]: {exc}")
        finally:
            try:
                if writer:
                    writer.close(); await writer.wait_closed()
            except Exception:
                pass
            connections.pop(conn_id, None)
    return StreamingResponse(body(), media_type=GRPC_CONTENT_TYPE, headers={"grpc-status": "0"})


async def _trojan_grpc_stream(request: Request):
    conn_id = secrets.token_urlsafe(6)
    ip = _client_ip(request)
    uid = None
    queue: asyncio.Queue = asyncio.Queue(maxsize=128)
    writer = None

    async def body():
        nonlocal uid, writer
        try:
            gen = _grpc_messages(request)
            first_plain = await asyncio.wait_for(gen.__anext__(), timeout=20.0)
            pw_hash, command, address, port, payload = await parse_trojan_header(first_plain)
            uid = await find_uuid_by_trojan_hash(pw_hash)
            async with LINKS_LOCK:
                link = LINKS.get(uid) if uid else None
            if not is_link_allowed(link):
                raise ValueError("not authorized")
            connections[conn_id] = {"uuid": uid, "ip": ip, "transport": "trojan-grpc", "connected_at": datetime.now().isoformat(), "bytes": 0}
            if command != 1:
                raise ValueError("only TCP command is supported")
            if not await check_and_use(uid, len(first_plain)):
                raise ValueError("quota/disabled")
            stats["total_requests"] += 1
            connections[conn_id]["bytes"] += len(first_plain)
            reader, writer = await asyncio.wait_for(asyncio.open_connection(address, port), timeout=10.0)
            if payload:
                writer.write(payload)
                await writer.drain()
            reader_task = asyncio.create_task(_tcp_to_queue(uid, conn_id, reader, queue, False))
            async def request_to_tcp():
                async for msg in gen:
                    if not await check_and_use(uid, len(msg)):
                        break
                    connections[conn_id]["bytes"] += len(msg)
                    writer.write(msg)
                    if writer.transport.get_write_buffer_size() > 512 * 1024:
                        await writer.drain()
                try:
                    writer.write_eof()
                except Exception:
                    pass
            writer_task = asyncio.create_task(request_to_tcp())
            while True:
                item = await queue.get()
                if item is None:
                    break
                yield item
            writer_task.cancel()
            await save_state()
        except Exception as exc:
            stats["total_errors"] += 1
            error_logs.append({"error": f"trojan-grpc: {exc}", "time": datetime.now().isoformat()})
            logger.error(f"Trojan-gRPC error [{conn_id}]: {exc}")
        finally:
            try:
                if writer:
                    writer.close(); await writer.wait_closed()
            except Exception:
                pass
            connections.pop(conn_id, None)
    return StreamingResponse(body(), media_type=GRPC_CONTENT_TYPE, headers={"grpc-status": "0"})


@router.post("/vgrpc-{token}/Tun")
@router.post("/vgrpc-{token}")
async def vless_grpc(token: str, request: Request):
    return await _vless_grpc_stream(request, token)


@router.post("/tgrpc-{token}/Tun")
@router.post("/tgrpc-{token}")
async def trojan_grpc(token: str, request: Request):
    return await _trojan_grpc_stream(request)
