import asyncio
import secrets
import socket
from datetime import datetime
from typing import Optional

from main import LINKS, LINKS_LOCK, connections, stats, error_logs, logger, is_link_allowed, save_state
from relay_vless import check_and_use
from shadowsocks_ws import SSDecryptor, SSEncryptor, parse_ss_header

SS_TCP_INSTANCES: dict[str, dict] = {}
SS_TCP_PORTS: set[int] = set()
_USAGE_CALLBACK = None


def set_usage_callback(cb):
    global _USAGE_CALLBACK
    _USAGE_CALLBACK = cb


async def _use_quota(uid: str, n: int) -> bool:
    if _USAGE_CALLBACK:
        return await _USAGE_CALLBACK(uid, n)
    return await check_and_use(uid, n)


def _pick_port(preferred: Optional[int] = None, force: bool = False) -> int:
    if preferred and preferred not in SS_TCP_PORTS:
        return preferred
    if force and preferred:
        raise RuntimeError(f"پورت {preferred} در حال استفاده است")
    for p in range(8700, 8800):
        if p not in SS_TCP_PORTS:
            return p
    raise RuntimeError("هیچ پورت آزادی برای Shadowsocks TCP پیدا نشد")


async def _tcp_to_remote(uid: str, conn_id: str, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, decryptor: SSDecryptor):
    while True:
        data = await reader.read(256 * 1024)
        if not data:
            break
        for plain in decryptor.feed(data):
            if not await _use_quota(uid, len(plain)):
                return
            connections[conn_id]["bytes"] += len(plain)
            writer.write(plain)
            if writer.transport.get_write_buffer_size() > 512 * 1024:
                await writer.drain()


async def _remote_to_tcp(uid: str, conn_id: str, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, encryptor: SSEncryptor):
    while True:
        data = await reader.read(256 * 1024)
        if not data:
            break
        if not await _use_quota(uid, len(data)):
            return
        connections[conn_id]["bytes"] += len(data)
        writer.write(encryptor.encrypt_chunk(data))
        if writer.transport.get_write_buffer_size() > 512 * 1024:
            await writer.drain()


async def _handle_client(uid: str, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    conn_id = secrets.token_urlsafe(6)
    peer = writer.get_extra_info("peername")
    ip = peer[0] if peer else "نامشخص"
    remote_writer = None
    async with LINKS_LOCK:
        link = LINKS.get(uid)
    if not is_link_allowed(link):
        writer.close(); await writer.wait_closed(); return
    connections[conn_id] = {"uuid": uid, "ip": ip, "transport": "shadowsocks-tcp", "connected_at": datetime.now().isoformat(), "bytes": 0}
    try:
        decryptor = SSDecryptor(uid)
        first_plain = None
        while first_plain is None:
            data = await asyncio.wait_for(reader.read(256 * 1024), timeout=15.0)
            if not data:
                return
            chunks = decryptor.feed(data)
            if chunks:
                first_plain = b"".join(chunks)
        if not await _use_quota(uid, len(first_plain)):
            return
        address, port, payload = parse_ss_header(first_plain)
        stats["total_requests"] += 1
        connections[conn_id]["bytes"] += len(first_plain)
        remote_reader, remote_writer = await asyncio.wait_for(asyncio.open_connection(address, port), timeout=10.0)
        sock = remote_writer.transport.get_extra_info('socket')
        if sock:
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        if payload:
            remote_writer.write(payload)
            await remote_writer.drain()
        encryptor = SSEncryptor(uid)
        done, pending = await asyncio.wait({
            asyncio.create_task(_tcp_to_remote(uid, conn_id, reader, remote_writer, decryptor)),
            asyncio.create_task(_remote_to_tcp(uid, conn_id, remote_reader, writer, encryptor)),
        }, return_when=asyncio.FIRST_COMPLETED)
        for t in pending:
            t.cancel()
        await save_state()
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": f"ss-tcp: {exc}", "time": datetime.now().isoformat()})
        logger.error(f"SS-TCP error [{conn_id}]: {exc}")
    finally:
        try:
            if remote_writer:
                remote_writer.close(); await remote_writer.wait_closed()
        except Exception:
            pass
        try:
            writer.close(); await writer.wait_closed()
        except Exception:
            pass
        connections.pop(conn_id, None)


async def start_instance(uid: str, preferred_port: Optional[int] = None, force_port: bool = False) -> dict:
    if uid in SS_TCP_INSTANCES:
        return {"port": SS_TCP_INSTANCES[uid]["port"]}
    port = _pick_port(preferred_port, force_port)
    server = await asyncio.start_server(lambda r, w: _handle_client(uid, r, w), "0.0.0.0", port, reuse_address=True)
    SS_TCP_INSTANCES[uid] = {"server": server, "port": port}
    SS_TCP_PORTS.add(port)
    logger.info(f"SS-TCP[{uid[:8]}] started on {port}")
    return {"port": port}


async def stop_instance(uid: str):
    inst = SS_TCP_INSTANCES.pop(uid, None)
    if not inst:
        return
    SS_TCP_PORTS.discard(inst["port"])
    server = inst["server"]
    server.close()
    await server.wait_closed()


async def stop_all():
    for uid in list(SS_TCP_INSTANCES.keys()):
        await stop_instance(uid)
