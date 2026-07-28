import asyncio
import json
import os
import hashlib
import secrets
import sys
import re
import time
import aiofiles
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from urllib.parse import quote
from collections import deque, defaultdict
from pathlib import Path
import mtproto
from typing import Optional

from fastapi import FastAPI, Request, HTTPException, WebSocket, WebSocketDisconnect, Depends
from fastapi.responses import Response, HTMLResponse, JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import httpx
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("OXNET")

IRAN_TZ = ZoneInfo("Asia/Tehran")

app = FastAPI(title="OXNET", docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Persistence ───────────────────────────────────────────────────────────────
DATA_DIR = Path(os.environ.get("DATA_DIR", "/data"))
DATA_FILE = DATA_DIR / "oxnet_state.json"
SECRET_FILE = DATA_DIR / ".oxnet_secret"
PANEL_VERSION_FILE = Path(__file__).with_name("version.txt")
SAVE_LOCK = asyncio.Lock()


def _get_or_create_secret() -> str:
    env_secret = os.environ.get("SECRET_KEY")
    if env_secret:
        return env_secret
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if SECRET_FILE.exists():
            val = SECRET_FILE.read_text(encoding="utf-8").strip()
            if val:
                return val
        new_secret = secrets.token_urlsafe(32)
        SECRET_FILE.write_text(new_secret, encoding="utf-8")
        logger.info("SECRET_KEY جدید ساخته و در دیسک ذخیره شد (پایدار بین ری‌استارت‌ها).")
        return new_secret
    except Exception as e:
        logger.warning(f"عدم امکان ذخیره‌ی SECRET_KEY روی دیسک: {e} — از مقدار موقت استفاده می‌شود.")
        return secrets.token_urlsafe(32)


CONFIG = {
    "port": int(os.environ.get("PORT", 8000)),
    "secret": _get_or_create_secret(),
    "host": os.environ.get("RAILWAY_PUBLIC_DOMAIN", "localhost"),
}


def get_current_panel_version() -> str:
    try:
        if PANEL_VERSION_FILE.exists():
            for line in PANEL_VERSION_FILE.read_text(encoding="utf-8").splitlines():
                if line.startswith("version="):
                    return line.split("=", 1)[1].strip() or "1.0.0"
    except Exception:
        pass
    return "1.0.0"


def _state_snapshot() -> dict:
    return {"links": dict(LINKS), "subs": dict(SUBS), "customers": dict(CUSTOMERS), "settings": dict(SETTINGS), "password_hash": AUTH["password_hash"], "saved_at": datetime.now().isoformat()}


async def load_state():
    global LINKS, AUTH, SUBS
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        data = None
        if DATA_FILE.exists():
            async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
                raw = await f.read()
            data = json.loads(raw) if raw.strip() else None
        if data:
            LINKS.update(data.get("links", {}))
            SUBS.update(data.get("subs", {}))
            CUSTOMERS.update(data.get("customers", {}))
            SETTINGS.update(data.get("settings", {}))
            SETTINGS.setdefault("cloudflare", {"domains": []})
            if "password_hash" in data:
                AUTH["password_hash"] = data["password_hash"]
            logger.info(f"State loaded from JSON: {len(LINKS)} links, {len(SUBS)} subs")
    except Exception as e:
        logger.warning(f"Could not load state: {e}")

async def save_state():
    async with SAVE_LOCK:
        try:
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            data = _state_snapshot()
            tmp = DATA_FILE.with_suffix(".tmp")
            async with aiofiles.open(tmp, "w", encoding="utf-8") as f:
                await f.write(json.dumps(data, ensure_ascii=False, indent=2))
            tmp.replace(DATA_FILE)
        except Exception as e:
            logger.warning(f"Could not save state: {e}")

# ── In-memory state ───────────────────────────────────────────────────────────
connections: dict = {}
stats = {
    "total_bytes": 0,
    "total_requests": 0,
    "total_errors": 0,
    "start_time": time.time(),
}
error_logs: deque = deque(maxlen=50)
activity_logs: deque = deque(maxlen=200)
hourly_traffic: dict = defaultdict(int)
http_client: httpx.AsyncClient | None = None
LINKS: dict = {}
LINKS_LOCK = asyncio.Lock()
SUBS: dict = {}
SUBS_LOCK = asyncio.Lock()
CUSTOMERS: dict = {}
CUSTOMERS_LOCK = asyncio.Lock()
SETTINGS: dict = {
    "theme": {"accent": "#2563EB", "radius": 16, "density": "comfortable", "mode": "light"},
    "security": {"lockout_enabled": True, "max_attempts": 5, "lock_minutes": 10, "allowed_ips": []},
    "cleanup": {"auto_delete_expired_days": 0, "inactive_archive_days": 0, "log_keep": 150, "low_resource": False},
    "cloudflare": {"domains": []},
    "smart_profiles": {
        "general": ["trojan-ws", "vless-ws", "xhttp-stream-up"],
        "mobile": ["trojan-ws", "vless-ws", "shadowsocks-tls"],
        "mci": ["trojan-ws", "vless-ws"],
        "irancell": ["vless-ws", "trojan-ws", "xhttp-stream-up"],
        "wifi": ["xhttp-stream-up", "trojan-ws", "vless-ws"],
    }
}
FAILED_LOGINS: dict = {}

PROTOCOLS = (
    "vless-ws",
    "xhttp-packet-up", "xhttp-stream-up", "xhttp-stream-one",
    "trojan-ws",
    "trojan-xhttp-packet-up", "trojan-xhttp-stream-up",
    "shadowsocks-tls", "mtproto", "multi",
)
DEFAULT_PROTOCOL = "vless-ws"

def log_activity(kind: str, message: str, level: str = "info"):
    activity_logs.append({
        "kind": kind,
        "level": level,
        "message": message,
        "time": datetime.now().isoformat(),
    })


# ── Auth ──────────────────────────────────────────────────────────────────────
SESSION_COOKIE = "oxnet_session"
SESSION_TTL = 60 * 60 * 24 * 7

def hash_password(pw: str) -> str:
    return hashlib.sha256(f"{pw}{CONFIG['secret']}".encode()).hexdigest()

AUTH = {"password_hash": hash_password(os.environ.get("ADMIN_PASSWORD", "123456"))}

def security_client_allowed(ip: str) -> bool:
    allowed = SETTINGS.get("security", {}).get("allowed_ips") or []
    return not allowed or ip in allowed

def is_login_locked(ip: str) -> tuple[bool, int]:
    sec = SETTINGS.get("security", {})
    if not sec.get("lockout_enabled", True):
        return False, 0
    rec = FAILED_LOGINS.get(ip) or {"count": 0, "until": 0}
    until = float(rec.get("until") or 0)
    if until > time.time():
        return True, int(until - time.time())
    return False, 0

def record_login_failure(ip: str):
    sec = SETTINGS.get("security", {})
    max_attempts = int(sec.get("max_attempts", 5) or 5)
    lock_minutes = int(sec.get("lock_minutes", 10) or 10)
    rec = FAILED_LOGINS.setdefault(ip, {"count": 0, "until": 0})
    rec["count"] = int(rec.get("count", 0)) + 1
    if rec["count"] >= max_attempts:
        rec["until"] = time.time() + lock_minutes * 60
        rec["count"] = 0

def record_login_success(ip: str):
    FAILED_LOGINS.pop(ip, None)

SESSIONS: dict = {}
SESSIONS_LOCK = asyncio.Lock()

async def create_session() -> str:
    token = secrets.token_urlsafe(32)
    async with SESSIONS_LOCK:
        SESSIONS[token] = time.time() + SESSION_TTL
    return token

async def is_valid_session(token: str | None) -> bool:
    if not token:
        return False
    async with SESSIONS_LOCK:
        exp = SESSIONS.get(token)
        if exp is None:
            return False
        if exp < time.time():
            SESSIONS.pop(token, None)
            return False
        return True

async def destroy_session(token: str | None):
    if not token:
        return
    async with SESSIONS_LOCK:
        SESSIONS.pop(token, None)

async def require_auth(request: Request):
    token = request.cookies.get(SESSION_COOKIE)
    if not await is_valid_session(token):
        raise HTTPException(status_code=401, detail="unauthorized")
    return token

# ── Startup / Shutdown ────────────────────────────────────────────────────────
@app.on_event("startup")
async def startup():
    global http_client
    limits = httpx.Limits(max_connections=500, max_keepalive_connections=100)
    timeout = httpx.Timeout(30.0, connect=10.0)
    http_client = httpx.AsyncClient(
        limits=limits, timeout=timeout, follow_redirects=True,
    )
    await load_state()
    await _restart_mtproto_instances()
    log_activity("system", "سرور راه‌اندازی شد", "ok")
    logger.info(f"OXNET v1.0.0 started on port {CONFIG['port']}")

async def _restart_mtproto_instances():
    async with LINKS_LOCK:
        targets = [
            (uid, d) for uid, d in LINKS.items()
            if d.get("protocol") == "mtproto" and d.get("active", True)
        ]
    for uid, d in targets:
        try:
            inst = await mtproto.start_instance(
                uid,
                secret=d.get("mtproto_secret"),
                domain=d.get("mtproto_domain", mtproto.DEFAULT_FAKE_TLS_DOMAIN),
                preferred_port=d.get("mtproto_port"),
                force_port=d.get("mtproto_manual_port", False),
                ad_tag=d.get("ad_tag"),
            )
            old_port = d.get("mtproto_port")
            async with LINKS_LOCK:
                LINKS[uid]["mtproto_port"] = inst["port"]
                LINKS[uid]["mtproto_secret"] = inst["secret"]

            if (d.get("mtproto_proxy_id") and inst["port"] != old_port
                    and not d.get("mtproto_manual_port", False)):
                asyncio.create_task(_reattach_mtproto_public_proxy(
                    uid, inst["port"], d.get("mtproto_proxy_id"), d.get("label", "")
                ))
        except Exception as exc:
            logger.error(f"ری‌استارت خودکار MTProto ناموفق برای {uid[:8]}: {exc}")

async def _mtproto_usage_callback(uuid: str, n_bytes: int) -> bool:
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
        if link is None:
            return False
        if not is_link_allowed(link):
            return False
        link["used_bytes"] += n_bytes
        stats["total_bytes"] += n_bytes
        hourly_traffic[now_ir().strftime("%H:00")] += n_bytes
    return True

mtproto.set_usage_callback(_mtproto_usage_callback)

async def _attach_mtproto_public_proxy(uid: str, application_port: int, label: str):
    async with LINKS_LOCK:
        if uid in LINKS:
            LINKS[uid]["mtproto_public_pending"] = False
    await save_state()

async def _reattach_mtproto_public_proxy(uid: str, new_port: int, old_proxy_id: Optional[str], label: str):
    await _attach_mtproto_public_proxy(uid, new_port, label)

# ===== تابع جدید برای به‌روزرسانی ad_tag روی پروکسی =====
async def _update_mtproto_ad_tag(uuid: str, ad_tag: str):
    try:
        await mtproto.stop_instance(uuid)
        async with LINKS_LOCK:
            link = LINKS.get(uuid)
            if not link:
                return
            inst = await mtproto.start_instance(
                uuid,
                secret=link.get("mtproto_secret"),
                domain=link.get("mtproto_domain", mtproto.DEFAULT_FAKE_TLS_DOMAIN),
                preferred_port=link.get("mtproto_port"),
                force_port=link.get("mtproto_manual_port", False),
                ad_tag=ad_tag,
            )
            link["mtproto_port"] = inst["port"]
            link["mtproto_secret"] = inst["secret"]
            link["ad_tag"] = ad_tag
            link["ad_tag_status"] = "done"          # ← جدید
            link["ad_tag_link"] = generate_share_link(   # ← جدید، لینک تازه با سکرت جدید
                uuid, get_host(), remark=f"OXNET-{link.get('label','')}", protocol="mtproto"
            )
        await save_state()            # ذخیره فوری در دیتابیس/دیسک
        logger.info(f"MTProto[{uuid[:8]}]: ad_tag به‌روز شد و instance ری‌استارت شد")
    except Exception as exc:
        logger.error(f"خطا در به‌روزرسانی ad_tag برای {uuid[:8]}: {exc}")
        async with LINKS_LOCK:
            if uuid in LINKS:
                LINKS[uuid]["active"] = False
                LINKS[uuid]["ad_tag_status"] = "error"
        log_activity("link", f"به‌روزرسانی ad_tag برای «{LINKS.get(uuid,{}).get('label','')}» ناموفق بود", "err")

@app.on_event("shutdown")
async def shutdown():
    await save_state()
    await mtproto.stop_all()
    if http_client:
        await http_client.aclose()

# ── Helpers ───────────────────────────────────────────────────────────────────
def normalize_config_path(value: str | None) -> str | None:
    """Return a clean user-facing path token such as PlanAsli for /ws/PlanAsli."""
    if value is None:
        return None
    value = str(value).strip().strip('/')
    if value.startswith('ws/'):
        value = value[3:]
    if not value:
        return None
    value = re.sub(r'\s+', '-', value)
    value = re.sub(r'[^A-Za-z0-9._-]', '', value)[:64]
    if len(value) < 2:
        return None
    return value

async def resolve_link_id(token: str) -> str | None:
    """Resolve either the original UUID or the custom path to the internal UUID."""
    async with LINKS_LOCK:
        if token in LINKS:
            return token
        for uid, link in LINKS.items():
            if link.get('path') == token:
                return uid
    return None

async def unique_config_path(base: str | None, fallback: str) -> str:
    base = normalize_config_path(base) or fallback
    async with LINKS_LOCK:
        used = {uid for uid in LINKS} | {str(v.get('path')) for v in LINKS.values() if v.get('path')}
    candidate = base
    i = 2
    while candidate in used:
        candidate = f"{base}-{i}"
        i += 1
    return candidate

def proto_slug(proto: str) -> str:
    return proto.replace('shadowsocks-tls', 'ss').replace('trojan-', 'tr-').replace('vless-', 'vl-').replace('xhttp-', 'xh-').replace('-up', '').replace('-one', '1')

def get_host() -> str:
    return os.environ.get("RAILWAY_PUBLIC_DOMAIN", CONFIG["host"])

def generate_uuid() -> str:
    h = secrets.token_hex(16)
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"

def now_ir() -> datetime:
    return datetime.now(IRAN_TZ)


def _uri_authority_host(host: str) -> str:
    host = str(host or "").strip()
    if host.startswith("[") and host.endswith("]"):
        return host
    # IPv6 literals must be bracketed in URI authority: vless://uuid@[IPv6]:443
    if ":" in host and not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", host):
        return f"[{host}]"
    return host

def generate_share_link(uuid: str, host: str, remark: str = "OXNET", protocol: str = DEFAULT_PROTOCOL, sni_host: str | None = None) -> str:
    link_obj = LINKS.get(uuid, {})
    public_path = link_obj.get("path") or uuid
    tls_host = (sni_host or host).strip()
    authority_host = _uri_authority_host(host)
    if protocol == "shadowsocks-tls":
        import base64
        # SIP002 plugin form with explicit websocket mode and always a fragment/name.
        # This fixes links that previously ended as "...?" without plugin/name.
        user = base64.urlsafe_b64encode(f"chacha20-ietf-poly1305:{uuid}".encode()).decode().rstrip("=")
        plugin = quote(f"v2ray-plugin;tls;mode=websocket;host={tls_host};path=/ss/{public_path}", safe="")
        return f"ss://{user}@{authority_host}:443?plugin={plugin}#{quote(remark or 'OXNET-Shadowsocks')}"
    if protocol == "mtproto":
        link = LINKS.get(uuid)
        port = link.get("mtproto_port") if link else None
        secret = link.get("mtproto_secret") if link else None
        if not port or not secret:
            return f"tg://proxy?server={host}&port=0&secret=not_ready#{quote(remark)}"
        pub_host = link.get("mtproto_public_host") if link else None
        pub_port = link.get("mtproto_public_port") if link else None
        final_host = pub_host or host
        final_port = pub_port or port
        return mtproto.generate_mtproto_link(final_host, final_port, secret)
    if protocol == "trojan-ws":
        params = {
            "security": "tls", "type": "ws", "host": tls_host,
            "path": "/trojan-ws", "sni": tls_host, "fp": "chrome", "alpn": "http/1.1",
        }
        query = "&".join(f"{k}={quote(str(v))}" for k, v in params.items())
        return f"trojan://{uuid}@{authority_host}:443?{query}#{quote(remark)}"
    if protocol.startswith("trojan-xhttp-"):
        mode = protocol.replace("trojan-xhttp-", "")
        if mode == "stream-one":
            mode = "stream-up"
        path = f"/xhttp-siz10/{mode}/{public_path}"
        params = {
            "security": "tls", "type": "xhttp", "mode": mode, "host": tls_host,
            "path": path, "sni": tls_host, "fp": "chrome", "alpn": "h2,http/1.1",
        }
        query = "&".join(f"{k}={quote(str(v))}" for k, v in params.items())
        return f"trojan://{uuid}@{authority_host}:443?{query}#{quote(remark)}"
    if protocol == "vless-ws":
        path = f"/ws/{public_path}"
        params = {
            "encryption": "none",
            "security": "tls",
            "type": "ws",
            "host": tls_host,
            "path": path,
            "sni": tls_host,
            "fp": "chrome",
            "alpn": "http/1.1",
        }
    else:
        mode = protocol.replace("xhttp-", "")
        if mode == "stream-one":
            mode = "stream-up"
        path = f"/xhttp-siz10/{mode}/{public_path}"
        params = {
            "encryption": "none",
            "security": "tls",
            "type": "xhttp",
            "mode": mode,
            "host": tls_host,
            "path": path,
            "sni": tls_host,
            "fp": "chrome",
            "alpn": "h2,http/1.1",
        }
    query = "&".join(f"{k}={quote(str(v))}" for k, v in params.items())
    return f"vless://{uuid}@{authority_host}:443?{query}#{quote(remark)}"

def uptime() -> str:
    secs = int(time.time() - stats["start_time"])
    h, m, s = secs // 3600, (secs % 3600) // 60, secs % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def parse_size_to_bytes(value: float, unit: str) -> int:
    unit = unit.upper()
    if unit == "GB": return int(value * 1024 ** 3)
    if unit == "MB": return int(value * 1024 ** 2)
    if unit == "KB": return int(value * 1024)
    return int(value)

def is_link_expired(link: dict) -> bool:
    exp = link.get("expires_at")
    if not exp:
        return False
    try:
        return datetime.now() > datetime.fromisoformat(exp)
    except Exception:
        return False

def is_link_allowed(link: dict | None) -> bool:
    if link is None:
        return False
    if not link.get("active", True):
        return False
    if is_link_expired(link):
        return False
    lb = link.get("limit_bytes", 0)
    if lb > 0 and link.get("used_bytes", 0) >= lb:
        return False
    return True

def fmt_bytes(b: int) -> str:
    if b < 1024: return f"{b} B"
    if b < 1024**2: return f"{b/1024:.1f} KB"
    if b < 1024**3: return f"{b/1024**2:.2f} MB"
    return f"{b/1024**3:.2f} GB"

def client_ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = request.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "نامشخص"

# ── Default link ──────────────────────────────────────────────────────────────
_default_link_created = False

async def ensure_default_link():
    global _default_link_created
    if _default_link_created:
        return
    async with LINKS_LOCK:
        if not any(l.get("is_default") for l in LINKS.values()):
            uid = hashlib.sha256(f"default{CONFIG['secret']}".encode()).hexdigest()
            uid = f"{uid[:8]}-{uid[8:12]}-{uid[12:16]}-{uid[16:20]}-{uid[20:32]}"
            if uid not in LINKS:
                LINKS[uid] = {
                    "label": "لینک پیش‌فرض",
                    "limit_bytes": 0,
                    "used_bytes": 0,
                    "created_at": datetime.now().isoformat(),
                    "active": True,
                    "expires_at": None,
                    "note": "",
                    "is_default": True,
                    "sub_id": None,
                    "protocol": DEFAULT_PROTOCOL,
                    "path": uid,
                }
                await save_state()
        _default_link_created = True

# ── Basic endpoints ───────────────────────────────────────────────────────────
@app.get("/")
async def root():
    return {"service": "OXNET", "version": get_current_panel_version(), "status": "active"}

@app.get("/health")
async def health():
    return {"status": "ok", "connections": len(connections), "uptime": uptime()}

# ── Subscription (single link) ────────────────────────────────────────────────
@app.get("/sub/{uuid}")
async def subscription_single(uuid: str):
    import base64
    uid = await resolve_link_id(uuid)
    if not uid:
        raise HTTPException(status_code=404, detail="not found or inactive")
    async with LINKS_LOCK:
        link = LINKS.get(uid)
    if not link or not is_link_allowed(link):
        raise HTTPException(status_code=404, detail="not found or inactive")
    host = get_host()
    proto = link.get("protocol", DEFAULT_PROTOCOL)
    vless = generate_share_link(uid, host, remark=f"OXNET-{link['label']}", protocol=proto)
    content = base64.b64encode(vless.encode()).decode()
    return Response(content=content, media_type="text/plain",
                    headers={"profile-title": quote(link["label"])})

@app.get("/sub-all")
async def subscription_all(_=Depends(require_auth)):
    import base64
    host = get_host()
    async with LINKS_LOCK:
        lines = [
            generate_share_link(uid, host, remark=f"OXNET-{d['label']}", protocol=d.get("protocol", DEFAULT_PROTOCOL))
            for uid, d in LINKS.items()
            if is_link_allowed(d)
        ]
    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain")

# ══════════════════════════════════════════════════════════════════════════════
# SUB GROUP endpoints (بدون تغییر)
# ══════════════════════════════════════════════════════════════════════════════

@app.post("/api/subs")
async def create_sub(request: Request, _=Depends(require_auth)):
    body = await request.json()
    name = (body.get("name") or "گروه جدید").strip()[:60]
    desc = (body.get("desc") or "").strip()[:200]
    password = (body.get("password") or "").strip()
    sub_id = generate_uuid()
    uuid_key = secrets.token_urlsafe(16)
    async with SUBS_LOCK:
        SUBS[sub_id] = {
            "name": name,
            "desc": desc,
            "password_hash": hash_password(password) if password else None,
            "uuid_key": uuid_key,
            "created_at": datetime.now().isoformat(),
            "link_ids": [],
        }
    await save_state()
    log_activity("sub", f"گروه «{name}» ساخته شد", "ok")
    host = get_host()
    return {
        "sub_id": sub_id,
        **SUBS[sub_id],
        "public_url": f"https://{host}/p/{uuid_key}",
        "sub_url": f"https://{host}/sub-group/{uuid_key}",
    }

@app.get("/api/subs")
async def list_subs(_=Depends(require_auth)):
    host = get_host()
    async with SUBS_LOCK:
        snap_subs = dict(SUBS)
    async with LINKS_LOCK:
        snap_links = dict(LINKS)
    result = []
    for sid, s in snap_subs.items():
        link_ids = s.get("link_ids", [])
        active_count = sum(1 for lid in link_ids if is_link_allowed(snap_links.get(lid)))
        total_used = sum(snap_links[lid].get("used_bytes", 0) for lid in link_ids if lid in snap_links)
        result.append({
            "sub_id": sid,
            **s,
            "password_hash": None,
            "has_password": s.get("password_hash") is not None,
            "links_count": len(link_ids),
            "active_count": active_count,
            "total_used_bytes": total_used,
            "total_used_fmt": fmt_bytes(total_used),
            "public_url": f"https://{host}/p/{s['uuid_key']}",
            "sub_url": f"https://{host}/sub-group/{s['uuid_key']}",
            "cloudflare_subs": cloudflare_sub_urls_for_key(host, s["uuid_key"]),
        })
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"subs": result}

@app.patch("/api/subs/{sub_id}")
async def update_sub(sub_id: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    async with SUBS_LOCK:
        if sub_id not in SUBS:
            raise HTTPException(status_code=404, detail="sub not found")
        s = SUBS[sub_id]
        if "name" in body:
            s["name"] = str(body["name"])[:60]
        if "desc" in body:
            s["desc"] = str(body["desc"])[:200]
        if "password" in body:
            pw = str(body["password"]).strip()
            s["password_hash"] = hash_password(pw) if pw else None
        if "link_ids" in body:
            s["link_ids"] = list(body["link_ids"])
    await save_state()
    return {"ok": True}

@app.delete("/api/subs/{sub_id}")
async def delete_sub(sub_id: str, _=Depends(require_auth)):
    async with SUBS_LOCK:
        if sub_id not in SUBS:
            raise HTTPException(status_code=404, detail="sub not found")
        name = SUBS[sub_id].get("name", sub_id)
        del SUBS[sub_id]
    async with LINKS_LOCK:
        for link in LINKS.values():
            if link.get("sub_id") == sub_id:
                link["sub_id"] = None
    await save_state()
    log_activity("sub", f"گروه «{name}» حذف شد", "warn")
    return {"ok": True, "deleted": sub_id}

@app.post("/api/subs/{sub_id}/links")
async def assign_link_to_sub(sub_id: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    link_id = str(body.get("link_id", ""))
    action = str(body.get("action", "add"))
    async with SUBS_LOCK:
        if sub_id not in SUBS:
            raise HTTPException(status_code=404, detail="sub not found")
        s = SUBS[sub_id]
        ids = s.setdefault("link_ids", [])
        if action == "add":
            if link_id not in ids:
                ids.append(link_id)
        else:
            if link_id in ids:
                ids.remove(link_id)
    async with LINKS_LOCK:
        if link_id in LINKS:
            LINKS[link_id]["sub_id"] = sub_id if action == "add" else None
    await save_state()
    return {"ok": True}

# ── Public sub-group subscription file ───────────────────────────────────────
@app.get("/sub-group/{uuid_key}")
async def sub_group_subscription(uuid_key: str, request: Request):
    import base64
    async with SUBS_LOCK:
        sub = next((s for s in SUBS.values() if s.get("uuid_key") == uuid_key), None)
    if not sub:
        raise HTTPException(status_code=404, detail="not found")
    if sub.get("password_hash"):
        pw = request.query_params.get("pw", "")
        if hash_password(pw) != sub["password_hash"]:
            raise HTTPException(status_code=403, detail="wrong password")
    host = get_host()
    link_ids = sub.get("link_ids", [])
    async with LINKS_LOCK:
        lines = []
        for lid in link_ids:
            link = LINKS.get(lid)
            if link and is_link_allowed(link):
                lines.append(generate_share_link(lid, host, remark=f"OXNET-{link['label']}", protocol=link.get("protocol", DEFAULT_PROTOCOL)))
    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(
        content=content,
        media_type="text/plain",
        headers={
            "profile-title": quote(sub["name"]),
            "profile-update-interval": "12",
        }
    )

# ── Auth endpoints ────────────────────────────────────────────────────────────
@app.post("/api/login")
async def api_login(request: Request):
    body = await request.json()
    ip = client_ip(request)
    if not security_client_allowed(ip):
        log_activity("auth", f"ورود از IP غیرمجاز مسدود شد: {ip}", "err")
        raise HTTPException(status_code=403, detail="IP شما مجاز نیست")
    locked, remaining = is_login_locked(ip)
    if locked:
        raise HTTPException(status_code=429, detail=f"ورود موقتاً قفل است؛ {remaining} ثانیه دیگر تلاش کنید")
    if hash_password(str(body.get("password", ""))) != AUTH["password_hash"]:
        record_login_failure(ip)
        log_activity("auth", f"تلاش ورود ناموفق از {ip}", "err")
        raise HTTPException(status_code=401, detail="رمز عبور اشتباه است")
    record_login_success(ip)
    token = await create_session()
    log_activity("auth", f"ورود موفق به پنل از {ip}", "ok")
    resp = JSONResponse({"ok": True})
    resp.set_cookie(SESSION_COOKIE, token, max_age=SESSION_TTL, httponly=True, samesite="lax", path="/")
    return resp

@app.post("/api/logout")
async def api_logout(request: Request):
    await destroy_session(request.cookies.get(SESSION_COOKIE))
    resp = JSONResponse({"ok": True})
    resp.delete_cookie(SESSION_COOKIE, path="/")
    return resp

@app.get("/api/me")
async def api_me(request: Request):
    return {"authenticated": await is_valid_session(request.cookies.get(SESSION_COOKIE))}

@app.post("/api/change-password")
async def api_change_password(request: Request, token=Depends(require_auth)):
    body = await request.json()
    if hash_password(str(body.get("current_password", ""))) != AUTH["password_hash"]:
        raise HTTPException(status_code=400, detail="رمز فعلی اشتباه است")
    new = str(body.get("new_password", ""))
    if len(new) < 4:
        raise HTTPException(status_code=400, detail="رمز جدید باید حداقل ۴ کاراکتر باشد")
    AUTH["password_hash"] = hash_password(new)
    async with SESSIONS_LOCK:
        SESSIONS.clear()
        SESSIONS[token] = time.time() + SESSION_TTL
    await save_state()
    log_activity("auth", "رمز عبور پنل تغییر کرد", "ok")
    return {"ok": True}

# ── Stats ─────────────────────────────────────────────────────────────────────
@app.get("/stats")
async def get_stats(_=Depends(require_auth)):
    async with LINKS_LOCK:
        snap = dict(LINKS)
    return {
        "active_connections": len(connections),
        "total_traffic_mb": round(stats["total_bytes"] / (1024 ** 2), 2),
        "total_requests": stats["total_requests"],
        "total_errors": stats["total_errors"],
        "uptime": uptime(),
        "timestamp": datetime.now().isoformat(),
        "hourly": dict(hourly_traffic),
        "recent_errors": list(error_logs)[-10:],
        "links_count": len(snap),
        "active_links": sum(1 for l in snap.values() if is_link_allowed(l)),
        "expired_links": sum(1 for l in snap.values() if is_link_expired(l)),
        "subs_count": len(SUBS),
        "protocol_counts": {
            "vless_ws": sum(1 for l in snap.values() if l.get("protocol") == "vless-ws"),
            "trojan_ws": sum(1 for l in snap.values() if l.get("protocol") == "trojan-ws"),
            "xhttp": sum(1 for l in snap.values() if "xhttp" in str(l.get("protocol", ""))),
            "shadowsocks_tls": sum(1 for l in snap.values() if l.get("protocol") == "shadowsocks-tls"),
            "mtproto": sum(1 for l in snap.values() if l.get("protocol") == "mtproto"),
        },
        "top_links": sorted([
            {"label": l.get("label", ""), "protocol": l.get("protocol", DEFAULT_PROTOCOL), "used_bytes": l.get("used_bytes", 0)}
            for l in snap.values()
        ], key=lambda x: x["used_bytes"], reverse=True)[:8],
        "db_mode": "JSON File",
    }

@app.get("/api/activity")
async def get_activity(_=Depends(require_auth)):
    return {"logs": list(activity_logs)[-150:]}

# ── Live connections (with IP) ────────────────────────────────────────────────
@app.get("/api/connections")
async def get_connections(_=Depends(require_auth)):
    async with LINKS_LOCK:
        snap = dict(LINKS)
    grouped: dict[str, dict] = {}
    for conn_id, c in connections.items():
        ip = c.get("ip", "نامشخص")
        link = snap.get(c.get("uuid"))
        label = link.get("label") if link else "نامشخص"
        g = grouped.get(ip)
        if g is None:
            g = {
                "ip": ip,
                "sessions": 0,
                "bytes": 0,
                "labels": set(),
                "transports": set(),
                "first_connected_at": c.get("connected_at"),
                "last_connected_at": c.get("connected_at"),
            }
            grouped[ip] = g
        g["sessions"] += 1
        g["bytes"] += c.get("bytes", 0)
        g["labels"].add(label)
        g["transports"].add(c.get("transport", "vless-ws"))
        ca = c.get("connected_at")
        if ca:
            if not g["first_connected_at"] or ca < g["first_connected_at"]:
                g["first_connected_at"] = ca
            if not g["last_connected_at"] or ca > g["last_connected_at"]:
                g["last_connected_at"] = ca
    for uid, link in snap.items():
        if link.get("protocol") == "mtproto":
            label = link.get("label", "نامشخص")
            for c in mtproto.get_instance_connections(uid):
                ip = c["ip"]
                g = grouped.get(ip)
                if g is None:
                    g = {
                        "ip": ip, "sessions": 0, "bytes": 0,
                        "labels": set(), "transports": set(),
                        "first_connected_at": None, "last_connected_at": None,
                    }
                    grouped[ip] = g
                g["sessions"] += 1
                g["labels"].add(label)
                g["transports"].add("mtproto")
    result = []
    for ip, g in grouped.items():
        result.append({
            "ip": ip,
            "sessions": g["sessions"],
            "labels": sorted(g["labels"]),
            "label": " · ".join(sorted(g["labels"])) if g["labels"] else "نامشخص",
            "transports": sorted(g["transports"]),
            "bytes": g["bytes"],
            "bytes_fmt": fmt_bytes(g["bytes"]),
            "connected_at": g["first_connected_at"],
            "last_connected_at": g["last_connected_at"],
        })
    result.sort(key=lambda x: x.get("last_connected_at") or "", reverse=True)
    return {
        "connections": result,
        "count": len(result),
        "raw_count": len(connections),
    }


# ── Cloudflare Domains / Clean IP subscriptions ─────────────────────────────
def _cf_domains() -> list[dict]:
    cf = SETTINGS.setdefault("cloudflare", {"domains": []})
    if isinstance(cf, dict):
        cf.setdefault("domains", [])
        return cf["domains"]
    SETTINGS["cloudflare"] = {"domains": []}
    return SETTINGS["cloudflare"]["domains"]

def _norm_domain(value: str) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"^https?://", "", value).split("/", 1)[0].strip().strip(".")
    return value

def _norm_clean_ips(raw) -> list[str]:
    # Supports IPv4, domains, and IPv6 literals. Backslash-escaped colons from chat copy are normalized.
    parts = re.split(r"[\n,\s]+", raw) if isinstance(raw, str) else list(raw or [])
    out=[]
    for x in parts:
        x=str(x).strip().replace("\\:", ":")
        if x.startswith("[") and x.endswith("]"):
            x=x[1:-1].strip()
        if x and x not in out:
            out.append(x)
    return out[:300]

def _cf_slug(domain: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "-", domain).strip("-") or secrets.token_urlsafe(8)

def _find_cf_domain(key: str) -> dict | None:
    key = _norm_domain(key) or key
    for d in _cf_domains():
        if d.get("domain") == key or d.get("slug") == key:
            return d
    return None

def cloudflare_sub_urls_for_key(host: str, uuid_key: str) -> list[dict]:
    return [
        {
            "name": cf.get("name") or cf.get("domain"),
            "domain": cf.get("domain"),
            "slug": cf.get("slug") or _cf_slug(cf.get("domain", "")),
            "clean_ip_count": len(cf.get("clean_ips") or []),
            "sub_url": f"{{https://{host}}}/cf-sub/{cf.get('slug') or _cf_slug(cf.get('domain',''))}/{uuid_key}",
        }
        for cf in _cf_domains()
    ]

@app.get("/api/cloudflare/domains")
async def api_cloudflare_domains(_=Depends(require_auth)):
    host=get_host()
    items=[]
    for d in _cf_domains():
        slug=d.get('slug') or _cf_slug(d.get('domain',''))
        items.append({**d, "slug": slug, "sub_url": f"{{https://{host}}}/cf-sub/{slug}", "group_sub_template": f"{{https://{host}}}/cf-sub/{slug}/{{uuid_key}}"})
    return {"domains": items}

@app.post("/api/cloudflare/domains")
async def api_cloudflare_save_domain(request: Request, _=Depends(require_auth)):
    body = await request.json()
    domain = _norm_domain(body.get("domain") or "")
    if not domain or "." not in domain:
        raise HTTPException(status_code=400, detail="دامنه کلادفلیر معتبر نیست")
    clean_ips = _norm_clean_ips(body.get("clean_ips") or body.get("ips") or "")
    name = (body.get("name") or domain).strip()[:80]
    key = str(body.get("key") or body.get("id") or body.get("slug") or "").strip()
    domains = _cf_domains()
    item = next((x for x in domains if key and (x.get("id") == key or x.get("slug") == key or x.get("domain") == _norm_domain(key))), None)
    if not item:
        item = next((x for x in domains if x.get("domain") == domain), None)
    if not item:
        item = {"id": generate_uuid(), "slug": _cf_slug(domain), "domain": domain, "created_at": datetime.now().isoformat()}
        domains.append(item)
    old_slug = item.get("slug")
    item.update({"name": name, "domain": domain, "slug": _cf_slug(domain), "clean_ips": clean_ips, "updated_at": datetime.now().isoformat()})
    if old_slug and old_slug != item["slug"]:
        item["previous_slug"] = old_slug
    await save_state()
    host=get_host()
    return {"ok": True, "domain": item, "sub_url": f"{{https://{host}}}/cf-sub/{item['slug']}"}

@app.delete("/api/cloudflare/domains/{key}")
async def api_cloudflare_delete_domain(key: str, _=Depends(require_auth)):
    domains=_cf_domains(); item=_find_cf_domain(key)
    if not item:
        raise HTTPException(status_code=404, detail="دامنه پیدا نشد")
    domains.remove(item)
    await save_state()
    return {"ok": True}

@app.get("/cf-sub/{key}")
async def cloudflare_subscription(key: str):
    import base64
    item=_find_cf_domain(key)
    if not item:
        raise HTTPException(status_code=404, detail="cloudflare domain not found")
    domain=item.get("domain")
    clean_ips=item.get("clean_ips") or []
    targets=clean_ips if clean_ips else [domain]
    async with LINKS_LOCK:
        snap=dict(LINKS)
    lines=[]
    for uid, link in snap.items():
        if not is_link_allowed(link):
            continue
        proto=link.get("protocol", DEFAULT_PROTOCOL)
        if proto == "mtproto":
            continue
        for target in targets:
            remark = f"OXNET-CF-{domain}-{link.get('label','')}" + (f"-{target}" if clean_ips else "")
            lines.append(generate_share_link(uid, target, remark=remark, protocol=proto, sni_host=domain))
    content=base64.b64encode("\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain", headers={"profile-title": quote(f"OXNET Cloudflare {domain}")})


@app.get("/cf-sub/{key}/{uuid_key}")
async def cloudflare_group_subscription(key: str, uuid_key: str, request: Request):
    import base64
    item=_find_cf_domain(key)
    if not item:
        raise HTTPException(status_code=404, detail="cloudflare domain not found")
    async with SUBS_LOCK:
        sub = next((s for s in SUBS.values() if s.get("uuid_key") == uuid_key), None)
    if not sub:
        raise HTTPException(status_code=404, detail="sub not found")
    if sub.get("password_hash"):
        pw = request.query_params.get("pw", "")
        if hash_password(pw) != sub["password_hash"]:
            raise HTTPException(status_code=403, detail="wrong password")
    domain=item.get("domain")
    clean_ips=item.get("clean_ips") or []
    targets=clean_ips if clean_ips else [domain]
    link_ids=sub.get("link_ids", [])
    async with LINKS_LOCK:
        lines=[]
        for lid in link_ids:
            link=LINKS.get(lid)
            if not link or not is_link_allowed(link):
                continue
            proto=link.get("protocol", DEFAULT_PROTOCOL)
            if proto == "mtproto":
                continue
            for target in targets:
                remark=f"OXNET-CF-{domain}-{link.get('label','')}" + (f"-{target}" if clean_ips else "")
                lines.append(generate_share_link(lid, target, remark=remark, protocol=proto, sni_host=domain))
    content=base64.b64encode("\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain", headers={"profile-title": quote(f"{sub.get('name','OXNET')} Cloudflare {domain}")})

# ── Link Management ───────────────────────────────────────────────────────────
@app.post("/api/links")
async def create_link(request: Request, _=Depends(require_auth)):
    body = await request.json()
    label = (body.get("label") or "لینک جدید").strip()[:60]
    lv = float(body.get("limit_value") or 0)
    lu = body.get("limit_unit") or "GB"
    limit_bytes = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
    exp_days = int(body.get("expires_days") or 0)
    expires_at = (datetime.now() + timedelta(days=exp_days)).isoformat() if exp_days > 0 else None
    note = (body.get("note") or "").strip()[:200]
    sub_id = body.get("sub_id") or None
    protocol = body.get("protocol") or DEFAULT_PROTOCOL
    if protocol not in PROTOCOLS:
        protocol = DEFAULT_PROTOCOL
    custom_path = normalize_config_path(body.get("custom_path"))

    if protocol == "multi":
        host = get_host()
        base_path = await unique_config_path(custom_path, generate_uuid()[:8])
        sub_id = generate_uuid()
        uuid_key = base_path
        multi_protocols = [
            "vless-ws", "xhttp-packet-up", "xhttp-stream-up",
            "trojan-ws", "trojan-xhttp-packet-up", "trojan-xhttp-stream-up",
            "shadowsocks-tls",
        ]
        sub = {
            "name": label,
            "desc": "Multi Protocol subscription",
            "uuid_key": uuid_key,
            "password_hash": None,
            "created_at": datetime.now().isoformat(),
            "link_ids": [],
        }
        links_out = []
        async with LINKS_LOCK:
            for p in multi_protocols:
                muid = generate_uuid()
                mpath = f"{base_path}-{proto_slug(p)}"
                i = 2
                used_paths = {str(v.get('path')) for v in LINKS.values() if v.get('path')}
                while mpath in LINKS or mpath in used_paths:
                    mpath = f"{base_path}-{proto_slug(p)}-{i}"
                    i += 1
                LINKS[muid] = {
                    "label": f"{label} - {p}",
                    "limit_bytes": limit_bytes,
                    "used_bytes": 0,
                    "created_at": datetime.now().isoformat(),
                    "active": True,
                    "expires_at": expires_at,
                    "note": note,
                    "is_default": False,
                    "sub_id": sub_id,
                    "protocol": p,
                    "path": mpath,
                    "is_multi_child": True,
                    "multi_group_id": sub_id,
                    "multi_group_path": base_path,
                    "ad_tag": None,
                }
                sub["link_ids"].append(muid)
                links_out.append({"uuid": muid, "path": mpath, "protocol": p, "vless_link": generate_share_link(muid, host, remark=f"OXNET-{label}-{p}", protocol=p)})
        async with SUBS_LOCK:
            SUBS[sub_id] = sub
        await save_state()
        log_activity("link", f"ساب مولتی پروتکل «{label}» ساخته شد", "ok")
        return {"ok": True, "mode": "multi", "sub_id": sub_id, "path": uuid_key, "sub_url": f"https://{host}/sub-group/{uuid_key}", "links": links_out}

    uid = generate_uuid()
    public_path = await unique_config_path(custom_path, uid)
    link_data = {
        "label": label,
        "limit_bytes": limit_bytes,
        "used_bytes": 0,
        "created_at": datetime.now().isoformat(),
        "active": True,
        "expires_at": expires_at,
        "note": note,
        "is_default": False,
        "sub_id": sub_id,
        "protocol": protocol,
        "path": public_path,
        "ad_tag": None,
    }

    if protocol == "mtproto":
        raw_port = body.get("mtproto_port")
        manual_port = int(raw_port) if raw_port not in (None, "", 0, "0") else None
        if manual_port is not None and not (1 <= manual_port <= 65535):
            raise HTTPException(status_code=400, detail="شماره پورت نامعتبر است")
        raw_domain = (body.get("mtproto_domain") or "").strip()
        domain = raw_domain if raw_domain else mtproto.DEFAULT_FAKE_TLS_DOMAIN
        try:
            inst = await mtproto.start_instance(
                uid,
                domain=domain,
                preferred_port=manual_port,
                force_port=manual_port is not None,
                ad_tag=None,
            )
        except RuntimeError as exc:
            logger.error(f"راه‌اندازی MTProto ناموفق برای {uid[:8]}: {exc}")
            raise HTTPException(status_code=409, detail=str(exc))
        except Exception as exc:
            logger.error(f"راه‌اندازی MTProto ناموفق برای {uid[:8]}: {exc}")
            raise HTTPException(status_code=502, detail=f"راه‌اندازی MTProto ناموفق: {exc}")
        link_data["mtproto_port"] = inst["port"]
        link_data["mtproto_secret"] = inst["secret"]
        link_data["mtproto_domain"] = inst["domain"]
        link_data["mtproto_manual_port"] = manual_port is not None
        link_data["mtproto_public_pending"] = False


    async with LINKS_LOCK:
        LINKS[uid] = link_data

    if sub_id:
        async with SUBS_LOCK:
            if sub_id in SUBS:
                ids = SUBS[sub_id].setdefault("link_ids", [])
                if uid not in ids:
                    ids.append(uid)

    await save_state()
    log_activity("link", f"کانفیگ «{label}» ساخته شد", "ok")
    host = get_host()
    return {
        "uuid": uid,
        **LINKS[uid],
        "expired": False,
        "vless_link": generate_share_link(uid, host, remark=f"OXNET-{label}", protocol=protocol),
        "sub_url": f"https://{host}/sub/{LINKS[uid].get('path') or uid}",
    }

@app.get("/api/links")
async def list_links(_=Depends(require_auth)):
    host = get_host()
    async with LINKS_LOCK:
        snap = dict(LINKS)
    result = []
    for uid, d in snap.items():
        proto = d.get("protocol", DEFAULT_PROTOCOL)
        result.append({
            "uuid": uid,
            **d,
            "protocol": proto,
            "expired": is_link_expired(d),
            "vless_link": generate_share_link(uid, host, remark=f"OXNET-{d['label']}", protocol=proto),
            "sub_url": f"https://{host}/sub/{d.get('path') or uid}",
        })
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"links": result}

@app.patch("/api/links/{uid}")
async def update_link(uid: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    mtproto_action = None
    new_sub = "UNCHANGED"

    async with LINKS_LOCK:
        if uid not in LINKS:
            raise HTTPException(status_code=404, detail="link not found")
        link = LINKS[uid]
        old_sub = link.get("sub_id")
        label = link.get("label")

        if "active" in body:
            new_active = bool(body["active"])
            changed = new_active != link.get("active", True)
            link["active"] = new_active
            log_activity("link", f"کانفیگ «{label}» {'فعال' if new_active else 'غیرفعال'} شد", "ok" if new_active else "warn")
            if changed and link.get("protocol") == "mtproto":
                mtproto_action = ("start" if new_active else "stop", dict(link))

        if "label" in body:
            link["label"] = str(body["label"])[:60]
        if "note" in body:
            link["note"] = str(body["note"])[:200]
        if "reset_usage" in body and body["reset_usage"]:
            link["used_bytes"] = 0
            log_activity("link", f"مصرف کانفیگ «{label}» ریست شد", "info")
        if "limit_value" in body:
            lv = float(body.get("limit_value") or 0)
            lu = body.get("limit_unit") or "GB"
            link["limit_bytes"] = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
        if "expires_days" in body:
            ed = int(body["expires_days"] or 0)
            link["expires_at"] = (datetime.now() + timedelta(days=ed)).isoformat() if ed > 0 else None
        if any(k in body for k in ("label", "note", "limit_value", "expires_days")):
            log_activity("link", f"کانفیگ «{link['label']}» ویرایش شد", "info")
        new_sub = body.get("sub_id", "UNCHANGED")
        if new_sub != "UNCHANGED":
            link["sub_id"] = new_sub or None

    if new_sub != "UNCHANGED":
        async with SUBS_LOCK:
            if old_sub and old_sub in SUBS:
                ids = SUBS[old_sub].get("link_ids", [])
                if uid in ids:
                    ids.remove(uid)
            if new_sub and new_sub in SUBS:
                ids = SUBS[new_sub].setdefault("link_ids", [])
                if uid not in ids:
                    ids.append(uid)

    if mtproto_action:
        action, snap = mtproto_action
        if action == "stop":
            await mtproto.stop_instance(uid)
        else:
            try:
                old_port = snap.get("mtproto_port")
                inst = await mtproto.start_instance(
                    uid,
                    secret=snap.get("mtproto_secret"),
                    domain=snap.get("mtproto_domain", mtproto.DEFAULT_FAKE_TLS_DOMAIN),
                    preferred_port=snap.get("mtproto_port"),
                    force_port=snap.get("mtproto_manual_port", False),
                    ad_tag=snap.get("ad_tag"),
                )
                async with LINKS_LOCK:
                    if uid in LINKS:
                        LINKS[uid]["mtproto_port"] = inst["port"]
                        LINKS[uid]["mtproto_secret"] = inst["secret"]
                if (snap.get("mtproto_proxy_id") and inst["port"] != old_port
                        and not snap.get("mtproto_manual_port", False)):
                    asyncio.create_task(_reattach_mtproto_public_proxy(
                        uid, inst["port"], snap.get("mtproto_proxy_id"), snap.get("label", "")
                    ))
            except Exception as exc:
                logger.error(f"روشن کردن MTProto ناموفق برای {uid[:8]}: {exc}")
                async with LINKS_LOCK:
                    if uid in LINKS:
                        LINKS[uid]["active"] = False
                log_activity("link", f"روشن کردن پروکسی تلگرام «{label}» ناموفق بود", "err")
                await save_state()
                raise HTTPException(status_code=502, detail=f"روشن کردن پروکسی تلگرام ناموفق بود: {exc}")

    await save_state()
    return {"ok": True}

# ===== Endpoint جدید برای به‌روزرسانی ad_tag =====
@app.patch("/api/links/{uid}/ad-tag")
async def update_ad_tag(uid: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    ad_tag = str(body.get("ad_tag", "")).strip()
    if not ad_tag:
        raise HTTPException(status_code=400, detail="ad_tag نمی‌تواند خالی باشد")

    async with LINKS_LOCK:
        if uid not in LINKS:
            raise HTTPException(status_code=404, detail="link not found")
        link = LINKS[uid]
        if link.get("protocol") != "mtproto":
            raise HTTPException(status_code=400, detail="این کانفیگ MTProto نیست")
        link["ad_tag_status"] = "pending"   # ← جدید

    asyncio.create_task(_update_mtproto_ad_tag(uid, ad_tag))
    log_activity("link", f"درخواست به‌روزرسانی ad_tag برای «{link.get('label','')}» ثبت شد", "info")
    return {"ok": True, "message": "ad_tag در حال اعمال است، پروکسی ری‌استارت می‌شود"}


# اندپوینت جدید برای پول کردن وضعیت
@app.get("/api/links/{uid}/ad-tag/status")
async def get_ad_tag_status(uid: str, _=Depends(require_auth)):
    async with LINKS_LOCK:
        link = LINKS.get(uid)
        if not link:
            raise HTTPException(status_code=404, detail="link not found")
        return {
            "status": link.get("ad_tag_status", "idle"),
            "link": link.get("ad_tag_link"),
            "ad_tag": link.get("ad_tag"),
        }

@app.delete("/api/links/{uid}")
async def delete_link(uid: str, _=Depends(require_auth)):
    async with LINKS_LOCK:
        if uid not in LINKS:
            raise HTTPException(status_code=404, detail="link not found")
        label = LINKS[uid].get("label", uid)
        sub_id = LINKS[uid].get("sub_id")
        proto = LINKS[uid].get("protocol")
        del LINKS[uid]
    if proto == "mtproto":
        await mtproto.stop_instance(uid)
    if sub_id:
        async with SUBS_LOCK:
            if sub_id in SUBS:
                ids = SUBS[sub_id].get("link_ids", [])
                if uid in ids:
                    ids.remove(uid)
    await save_state()
    log_activity("link", f"کانفیگ «{label}» حذف شد", "err")
    return {"ok": True, "deleted": uid}

# ══════════════════════════════════════════════════════════════════════════════
# VLESS Relay
# ══════════════════════════════════════════════════════════════════════════════
from relay_vless import (
    RELAY_BUF,
    parse_vless_header,
    check_and_use,
    relay_ws_to_tcp,
    relay_tcp_to_ws,
    websocket_tunnel,
)

from trojan import trojan_ws_tunnel
from shadowsocks_ws import shadowsocks_ws_tunnel

app.add_api_websocket_route("/ws/{uuid}", websocket_tunnel)
app.add_api_websocket_route("/trojan-ws", trojan_ws_tunnel)
app.add_api_websocket_route("/ss/{uuid}", shadowsocks_ws_tunnel)

# ══════════════════════════════════════════════════════════════════════════════
# XHTTP
# ══════════════════════════════════════════════════════════════════════════════
from xhttp_siz10 import router as xhttp_router
app.include_router(xhttp_router)

# ── HTTP Proxy ────────────────────────────────────────────────────────────────
_HOP = {"connection","keep-alive","proxy-authenticate","proxy-authorization",
        "te","trailers","transfer-encoding","upgrade","content-encoding","content-length"}

@app.api_route("/proxy/{target_url:path}", methods=["GET","POST","PUT","DELETE","PATCH","HEAD","OPTIONS"])
async def http_proxy(target_url: str, request: Request):
    if not target_url.startswith("http"):
        target_url = "https://" + target_url
    try:
        body = await request.body()
        headers = {k: v for k, v in request.headers.items() if k.lower() not in _HOP and k.lower() != "host"}
        resp = await http_client.request(method=request.method, url=target_url, headers=headers, content=body)
        stats["total_bytes"] += len(resp.content)
        stats["total_requests"] += 1
        hourly_traffic[now_ir().strftime("%H:00")] += len(resp.content)
        return Response(content=resp.content, status_code=resp.status_code,
                        headers={k: v for k, v in resp.headers.items() if k.lower() not in _HOP})
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "url": target_url, "time": datetime.now().isoformat()})
        raise HTTPException(status_code=502, detail=f"Proxy error: {exc}")

# ── Public sub page ───────────────────────────────────────────────────────────
@app.get("/p/{uuid_key}", response_class=HTMLResponse)
async def public_sub_page(uuid_key: str, request: Request):
    from pages import get_public_page_html
    async with SUBS_LOCK:
        sub = next(({"sub_id": sid, **s} for sid, s in SUBS.items() if s.get("uuid_key") == uuid_key), None)
    if not sub:
        return HTMLResponse("<h2 style='font-family:sans-serif;padding:40px'>گروه پیدا نشد</h2>", status_code=404)
    return HTMLResponse(content=get_public_page_html(uuid_key))

@app.get("/api/public/sub/{uuid_key}")
async def public_sub_data(uuid_key: str, request: Request):
    async with SUBS_LOCK:
        sub_entry = next(((sid, s) for sid, s in SUBS.items() if s.get("uuid_key") == uuid_key), None)
    if not sub_entry:
        raise HTTPException(status_code=404, detail="not found")
    sub_id, sub = sub_entry

    has_pw = sub.get("password_hash") is not None
    if has_pw:
        pw = request.query_params.get("pw", "")
        if hash_password(pw) != sub["password_hash"]:
            return JSONResponse({"locked": True, "name": sub["name"]})

    host = get_host()
    link_ids = sub.get("link_ids", [])
    async with LINKS_LOCK:
        snap = dict(LINKS)

    links_out = []
    active_conns = 0
    for lid in link_ids:
        link = snap.get(lid)
        if not link:
            continue
        allowed = is_link_allowed(link)
        conn_count = sum(1 for c in connections.values() if c.get("uuid") == lid)
        active_conns += conn_count
        proto = link.get("protocol", DEFAULT_PROTOCOL)
        links_out.append({
            "uuid": lid,
            "label": link["label"],
            "active": allowed,
            "protocol": proto,
            "used_bytes": link.get("used_bytes", 0),
            "used_fmt": fmt_bytes(link.get("used_bytes", 0)),
            "limit_bytes": link.get("limit_bytes", 0),
            "limit_fmt": "∞" if link.get("limit_bytes", 0) == 0 else fmt_bytes(link["limit_bytes"]),
            "expires_at": link.get("expires_at"),
            "vless_link": generate_share_link(lid, host, remark=f"OXNET-{link['label']}", protocol=proto),
            "sub_url": f"https://{host}/sub/{link.get('path') or lid}",
            "connections": conn_count,
        })

    total_used = sum(l["used_bytes"] for l in links_out)
    return {
        "locked": False,
        "name": sub["name"],
        "desc": sub.get("desc", ""),
        "sub_url": f"https://{host}/sub-group/{uuid_key}",
        "cloudflare_subs": cloudflare_sub_urls_for_key(host, uuid_key),
        "active_connections": active_conns,
        "total_used_fmt": fmt_bytes(total_used),
        "links": links_out,
    }


# ══════════════════════════════════════════════════════════════════════════════
# OXNET stable management APIs
# ══════════════════════════════════════════════════════════════════════════════
@app.get("/api/settings")
async def api_settings(_=Depends(require_auth)):
    return {"settings": SETTINGS}

@app.patch("/api/settings")
async def api_update_settings(request: Request, _=Depends(require_auth)):
    body = await request.json()
    for section in ("theme", "security", "cleanup"):
        if section in body and isinstance(body[section], dict):
            SETTINGS.setdefault(section, {}).update(body[section])
    await save_state()
    log_activity("system", "تنظیمات پیشرفته ذخیره شد", "ok")
    return {"ok": True, "settings": SETTINGS}

@app.get("/api/customers")
async def api_customers(_=Depends(require_auth)):
    async with CUSTOMERS_LOCK:
        return {"customers": [{"customer_id": cid, **c} for cid, c in CUSTOMERS.items()]}

@app.post("/api/customers")
async def api_create_customer(request: Request, _=Depends(require_auth)):
    body = await request.json()
    cid = generate_uuid()
    CUSTOMERS[cid] = {
        "name": str(body.get("name") or "کاربر جدید")[:80],
        "phone": str(body.get("phone") or "")[:40],
        "note": str(body.get("note") or "")[:300],
        "status": str(body.get("status") or "active")[:30],
        "link_ids": list(body.get("link_ids") or []),
        "created_at": datetime.now().isoformat(),
    }
    await save_state()
    return {"ok": True, "customer_id": cid, **CUSTOMERS[cid]}

@app.patch("/api/customers/{cid}")
async def api_update_customer(cid: str, request: Request, _=Depends(require_auth)):
    if cid not in CUSTOMERS:
        raise HTTPException(status_code=404, detail="customer not found")
    body = await request.json()
    for k in ("name", "phone", "note", "status"):
        if k in body: CUSTOMERS[cid][k] = str(body[k])[:300]
    if "link_ids" in body: CUSTOMERS[cid]["link_ids"] = list(body.get("link_ids") or [])
    await save_state()
    return {"ok": True, "customer_id": cid, **CUSTOMERS[cid]}

@app.delete("/api/customers/{cid}")
async def api_delete_customer(cid: str, _=Depends(require_auth)):
    CUSTOMERS.pop(cid, None)
    await save_state()
    return {"ok": True}

@app.get("/api/config-health")
async def api_config_health(_=Depends(require_auth)):
    async with LINKS_LOCK:
        snap = dict(LINKS)
    rows=[]
    now = datetime.now()
    for uid,l in snap.items():
        used=l.get("used_bytes",0); limit=l.get("limit_bytes",0); expired=is_link_expired(l)
        conn_count=sum(1 for c in connections.values() if c.get("uuid")==uid)
        score=100
        reasons=[]
        if not l.get("active", True): score-=45; reasons.append("غیرفعال")
        if expired: score-=45; reasons.append("منقضی")
        if limit and used>=limit: score-=40; reasons.append("سهمیه تمام")
        if conn_count>0: reasons.append("اتصال زنده")
        if "xhttp" in str(l.get("protocol","")) and conn_count==0: score-=5
        status="سالم" if score>=80 else ("نیازمند بررسی" if score>=45 else "خراب/مسدود")
        rows.append({"uuid":uid,"label":l.get("label"),"protocol":l.get("protocol"),"score":max(0,score),"status":status,"reasons":reasons,"used_bytes":used,"limit_bytes":limit,"active_connections":conn_count})
    rows.sort(key=lambda x:x["score"])
    return {"items": rows}

@app.post("/api/smart-subscription")
async def api_smart_subscription(request: Request, _=Depends(require_auth)):
    body = await request.json()
    label = str(body.get("label") or "Smart Iran")[:60]
    profile = str(body.get("profile") or "general")
    protocols = SETTINGS.get("smart_profiles", {}).get(profile) or SETTINGS["smart_profiles"]["general"]
    fake = {"label": label, "protocol": "multi", "custom_path": body.get("custom_path"), "limit_value": body.get("limit_value", 0), "limit_unit": body.get("limit_unit", "GB"), "expires_days": body.get("expires_days", 0), "note": "Smart Subscription"}
    host=get_host(); base_path=await unique_config_path(normalize_config_path(fake.get("custom_path")), generate_uuid()[:8]); sub_id=generate_uuid(); uuid_key=base_path
    sub={"name":label,"desc":f"Smart Subscription · {profile}","uuid_key":uuid_key,"password_hash":None,"created_at":datetime.now().isoformat(),"link_ids":[],"smart_profile":profile}
    limit_bytes=0 if float(fake.get("limit_value") or 0)<=0 else parse_size_to_bytes(float(fake.get("limit_value") or 0), fake.get("limit_unit") or "GB")
    expires_at=(datetime.now()+timedelta(days=int(fake.get("expires_days") or 0))).isoformat() if int(fake.get("expires_days") or 0)>0 else None
    async with LINKS_LOCK:
        for proto in protocols:
            muid=generate_uuid(); mpath=f"{base_path}-{proto_slug(proto)}"; LINKS[muid]={"label":f"{label} - {proto}","limit_bytes":limit_bytes,"used_bytes":0,"created_at":datetime.now().isoformat(),"active":True,"expires_at":expires_at,"note":"Smart Subscription","is_default":False,"sub_id":sub_id,"protocol":proto,"path":mpath,"is_multi_child":True,"multi_group_id":sub_id,"ad_tag":None}; sub["link_ids"].append(muid)
    SUBS[sub_id]=sub
    await save_state()
    return {"ok":True,"sub_id":sub_id,"sub_url":f"https://{host}/sub-group/{uuid_key}","profile":profile,"protocols":protocols}

@app.get("/api/backup/export")
async def api_backup_export(_=Depends(require_auth)):
    return JSONResponse(_state_snapshot(), headers={"Content-Disposition":"attachment; filename=oxnet-backup.json"})

@app.get("/api/backup/restore-points")
async def api_backup_restore_points(_=Depends(require_auth)):
    return {"items": SETTINGS.setdefault("backups", [])[-20:]}

@app.post("/api/backup/save")
async def api_backup_save(request: Request, _=Depends(require_auth)):
    body = await request.json()
    name = str(body.get("name") or f"Backup {datetime.now().strftime('%Y-%m-%d %H:%M')}")[:80]
    bid = generate_uuid()
    item = {"id": bid, "name": name, "created_at": datetime.now().isoformat(), "data": _state_snapshot()}
    SETTINGS.setdefault("backups", []).append(item)
    SETTINGS["backups"] = SETTINGS["backups"][-20:]
    await save_state()
    return {"ok": True, "id": bid, "name": name}

@app.post("/api/backup/restore/{bid}")
async def api_backup_restore(bid: str, _=Depends(require_auth)):
    item = next((b for b in SETTINGS.setdefault("backups", []) if b.get("id") == bid), None)
    if not item:
        raise HTTPException(status_code=404, detail="backup not found")
    data = item.get("data") or {}
    LINKS.clear(); LINKS.update(data.get("links", {}))
    SUBS.clear(); SUBS.update(data.get("subs", {}))
    CUSTOMERS.clear(); CUSTOMERS.update(data.get("customers", {}))
    SETTINGS.update(data.get("settings", {}))
    if data.get("password_hash"):
        AUTH["password_hash"] = data["password_hash"]
    await save_state()
    log_activity("system", f"ریستور بکاپ «{item.get('name','')}» انجام شد", "ok")
    return {"ok": True, "restored": item.get("name")}

@app.post("/api/backup/import")
async def api_backup_import(request: Request, _=Depends(require_auth)):
    data = await request.json()
    if not isinstance(data, dict):
        raise HTTPException(status_code=400, detail="backup invalid")
    LINKS.clear(); LINKS.update(data.get("links", {}))
    SUBS.clear(); SUBS.update(data.get("subs", {}))
    CUSTOMERS.clear(); CUSTOMERS.update(data.get("customers", {}))
    SETTINGS.update(data.get("settings", {}))
    if data.get("password_hash"): AUTH["password_hash"] = data["password_hash"]
    await save_state(); log_activity("system", "بکاپ ایمپورت شد", "ok")
    return {"ok": True, "links": len(LINKS), "subs": len(SUBS), "customers": len(CUSTOMERS)}

@app.get("/api/monitoring")
async def api_monitoring(_=Depends(require_auth)):
    async with LINKS_LOCK: snap=dict(LINKS)
    proto={}
    for l in snap.values(): proto[l.get("protocol",DEFAULT_PROTOCOL)] = proto.get(l.get("protocol",DEFAULT_PROTOCOL),0)+1
    ipmap={}
    for c in connections.values(): ipmap[c.get("ip","?")] = ipmap.get(c.get("ip","?"),0)+1
    return {"protocols":proto,"top_ips":sorted(ipmap.items(), key=lambda x:x[1], reverse=True)[:10],"top_links":sorted([{"label":l.get("label"),"used_bytes":l.get("used_bytes",0),"protocol":l.get("protocol")} for l in snap.values()], key=lambda x:x["used_bytes"], reverse=True)[:10],"errors":list(error_logs)[-20:],"db_mode":"JSON File"}

@app.post("/api/cleanup/run")
async def api_cleanup_run(request: Request, _=Depends(require_auth)):
    body=await request.json(); expired_days=int(body.get("expired_days",0) or 0); reset_logs=bool(body.get("reset_logs",False)); inactive_days=int(body.get("inactive_days",0) or 0)
    deleted=[]; archived=[]; now=datetime.now()
    async with LINKS_LOCK:
        for uid,l in list(LINKS.items()):
            if expired_days and l.get("expires_at"):
                try:
                    if (now-datetime.fromisoformat(l["expires_at"])).days>=expired_days:
                        deleted.append(uid); del LINKS[uid]; continue
                except Exception: pass
            if inactive_days and not l.get("active",True):
                l["archived"] = True; archived.append(uid)
    if reset_logs:
        error_logs.clear(); activity_logs.clear()
    await save_state()
    return {"ok":True,"deleted":len(deleted),"archived":len(archived),"logs_reset":reset_logs}

# ══════════════════════════════════════════════════════════════════════════════
# Version / Auto-Update
# ══════════════════════════════════════════════════════════════════════════════
update_log = deque(maxlen=100)
update_state = {"running": False, "progress": 0}
def load_update_history(): return []

@app.get("/api/version")
async def api_version(_=Depends(require_auth)):
    current_info = {"version": get_current_panel_version(), "description": "نسخه نصب‌شده OXNET"}
    return {"repo": "standalone", "branch": "local", "current": current_info, "latest": current_info, "update_available": False}

@app.get("/api/update-history")
async def api_update_history(_=Depends(require_auth)):
    return {"history": load_update_history()}

@app.get("/api/update-log")
async def api_update_log(_=Depends(require_auth)):
    return {"running": update_state["running"], "progress": update_state["progress"], "logs": list(update_log)[-100:]}

@app.post("/api/update")
async def api_update(_=Depends(require_auth)):
    raise HTTPException(status_code=404, detail="بروزرسانی خودکار در نسخه مستقل OXNET حذف شده است")


# ── HTML Pages ───────────────────────────────────────────────────────────────
from pages import LOGIN_HTML, DASHBOARD_HTML

def render_html(html: str) -> str:
    v = get_current_panel_version()
    return html.replace("v1.0.0", f"v{v}").replace("v1.1.0", f"v{v}").replace("v1.2.0", f"v{v}").replace("v1.2.1", f"v{v}").replace("v2.0.0", f"v{v}").replace("v2.0.1", f"v{v}").replace("v2.0.2", f"v{v}").replace("v2.0.3", f"v{v}").replace("v2.0.4", f"v{v}").replace("v2.0.5", f"v{v}").replace("v2.0.6", f"v{v}").replace("v2.0.7", f"v{v}").replace("v2.0.8", f"v{v}").replace("v2.0.9", f"v{v}").replace("· 1.0.0", f"· {v}").replace("· 1.1.0", f"· {v}").replace("· 1.2.0", f"· {v}").replace("· 1.2.1", f"· {v}").replace("· 2.0.0", f"· {v}").replace("· 2.0.1", f"· {v}").replace("· 2.0.2", f"· {v}").replace("· 2.0.3", f"· {v}").replace("· 2.0.4", f"· {v}").replace("· 2.0.5", f"· {v}").replace("· 2.0.6", f"· {v}").replace("· 2.0.7", f"· {v}").replace("· 2.0.8", f"· {v}").replace("· 2.0.9", f"· {v}")


# ── Central: Announcements & Support ─────────────────────────────────────────
@app.get("/api/announcements")
async def api_announcements(_=Depends(require_auth)):
    return {"announcements": []}

@app.post("/api/announcements/view")
async def api_announcements_view(request: Request, _=Depends(require_auth)):
    return {"ok": True}

@app.get("/api/support/messages")
async def api_support_messages(_=Depends(require_auth)):
    return {"messages": [], "blocked": False}

@app.post("/api/support/send")
async def api_support_send(request: Request, _=Depends(require_auth)):
    raise HTTPException(status_code=404, detail="این بخش در نسخه مستقل OXNET حذف شده است")

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    if await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        return RedirectResponse(url="/dashboard")
    return HTMLResponse(content=render_html(LOGIN_HTML))

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    if not await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        return RedirectResponse(url="/login")
    await ensure_default_link()
    return HTMLResponse(content=render_html(DASHBOARD_HTML))

@app.get("/test-ws", response_class=HTMLResponse)
async def test_ws_redirect():
    return HTMLResponse(content="<script>location.href='/dashboard'</script>")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=CONFIG["port"], log_level="info", workers=1)
