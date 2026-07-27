
# pages.py  -  OXNET v1.2.1
# شامل: LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · OXNET</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#F7F8FA;--card:#FFFFFF;--accent:#111827;--text:#111827;--dim:#64748B;--mid:#334155;--border:rgba(15,23,42,0.10)}@media(prefers-color-scheme:dark){:root{--bg:#0B0D10;--card:#151A20;--accent:#F8FAFC;--text:#F8FAFC;--dim:#94A3B8;--mid:#CBD5E1;--border:rgba(255,255,255,0.10)}}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px}
.bg{position:fixed;inset:0;background:linear-gradient(135deg,#ffffff 0%,var(--bg) 55%,#eef2f7 100%);z-index:0}
.grid{position:fixed;inset:0;background-image:linear-gradient(rgba(15,23,42,0.035) 1px,transparent 1px),linear-gradient(90deg,rgba(15,23,42,0.035) 1px,transparent 1px);background-size:44px 44px;z-index:0}
.orb{position:fixed;border-radius:50%;filter:blur(90px);z-index:0;animation:fl 9s ease-in-out infinite}
.o1{width:380px;height:380px;background:rgba(17,24,39,0.05);top:-100px;right:-80px}
.o2{width:280px;height:280px;background:rgba(37,99,235,0.05);bottom:-60px;left:-60px;animation-delay:4s}
@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-18px)}}
.wrap{position:relative;z-index:10;width:100%;max-width:400px}
.card{background:var(--card);border:1px solid var(--border);border-radius:20px;padding:38px 34px 34px;backdrop-filter:blur(24px);box-shadow:0 20px 60px rgba(15,23,42,.12)}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:28px}
.brand-img{width:48px;height:48px;border-radius:13px;overflow:hidden;border:1px solid var(--border);box-shadow:0 0 20px rgba(59,130,246,0.3);flex-shrink:0}
.brand-img img{width:100%;height:100%;object-fit:cover}
.brand-mark{width:48px;height:48px;border-radius:14px;display:flex;align-items:center;justify-content:center;background:#0f172a;color:#fff;font-weight:800;letter-spacing:.04em;border:1px solid rgba(15,23,42,.12);box-shadow:0 8px 24px rgba(15,23,42,.12)}
.brand-mark.small{width:38px;height:38px;border-radius:10px;font-size:12px;flex-shrink:0}
.brand-name{font-size:16px;font-weight:700;color:var(--text)}
.brand-sub{font-size:11px;color:var(--dim);margin-top:2px}
h1{font-size:21px;font-weight:700;color:var(--text);margin-bottom:5px;letter-spacing:-.02em}
.sub{font-size:12px;color:var(--mid);margin-bottom:24px;line-height:1.6}
.hint{display:flex;align-items:center;gap:10px;background:rgba(59,130,246,0.07);border:1px solid rgba(59,130,246,0.15);border-radius:10px;padding:10px 14px;margin-bottom:20px}
.hint-label{font-size:11px;color:var(--dim);flex:1}
.hint-val{font-family:ui-monospace,monospace;font-size:14px;font-weight:700;color:var(--accent);background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.25);padding:3px 11px;border-radius:7px;cursor:pointer;transition:.15s;letter-spacing:.08em}
.hint-val:hover{background:rgba(59,130,246,0.22)}
.field{margin-bottom:18px}
.field label{display:block;font-size:10.5px;font-weight:600;color:var(--mid);margin-bottom:7px;text-transform:uppercase;letter-spacing:.06em}
.inp-wrap{position:relative}
input[type=password]{width:100%;padding:13px 44px 13px 16px;border-radius:11px;border:1px solid var(--border);background:rgba(0,0,0,.3);color:var(--text);font-family:inherit;font-size:14px;outline:none;transition:.2s}
input[type=password]:focus{border-color:rgba(59,130,246,.55);background:rgba(0,0,0,.4);box-shadow:0 0 0 3px rgba(59,130,246,.1)}
.ic{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--dim);font-size:18px;pointer-events:none;transition:.2s}
input:focus+.ic{color:var(--accent)}
.err{display:none;background:rgba(239,68,68,.08);border:1px solid rgba(239,68,68,.2);border-radius:10px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:#F87171;align-items:center;gap:8px}
.err.show{display:flex}
.btn{width:100%;padding:13px;border-radius:11px;border:none;cursor:pointer;background:linear-gradient(135deg,#111827,#374151);color:#fff;font-family:inherit;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 10px 24px rgba(15,23,42,.18);transition:.2s;position:relative;overflow:hidden}
.btn::before{content:'';position:absolute;inset:0;background:rgba(255,255,255,.08);opacity:0;transition:.2s}
.btn:hover::before{opacity:1}
.btn:disabled{opacity:.5;cursor:not-allowed}
.footer{margin-top:22px;padding-top:18px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11px;color:var(--dim)}
.footer a{color:var(--accent);font-weight:600;text-decoration:none;display:flex;align-items:center;gap:4px}
@keyframes spin{to{transform:rotate(360deg)}}
#pg-updates,#pg-support,#modal-update{display:none!important}

.pc-ss{background:rgba(20,184,166,.12);color:#0F766E}
[data-theme="dark"] .pc-ss{color:#5EEAD4}
.dash-hero{display:grid;grid-template-columns:1.35fr .9fr;gap:16px;margin-bottom:18px}
.dash-main-card{position:relative;overflow:hidden;border-radius:26px;padding:28px;border:1px solid var(--card-b);background:linear-gradient(145deg,var(--card) 0%,var(--bg3) 100%);box-shadow:0 18px 60px rgba(15,23,42,.08)}
.dash-main-card:before{content:'';position:absolute;inset:auto -110px -140px auto;width:340px;height:340px;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.16),transparent 68%)}
.dash-eyebrow{font-size:11px;font-weight:800;letter-spacing:.14em;color:var(--t3);text-transform:uppercase;margin-bottom:10px}
.dash-title{font-size:34px;font-weight:900;letter-spacing:-.04em;color:var(--t1);line-height:1.2;margin-bottom:8px}
.dash-title span{color:var(--accent2)}
.dash-desc{max-width:620px;color:var(--t2);font-size:13px;line-height:2}
.dash-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}
.dash-side{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.dash-kpi{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:18px;box-shadow:0 10px 30px rgba(15,23,42,.05)}
.dash-kpi-icon{width:36px;height:36px;border-radius:12px;display:flex;align-items:center;justify-content:center;background:var(--accent-d);color:var(--accent2);font-size:18px;margin-bottom:14px}
.dash-kpi-label{font-size:10px;color:var(--t3);font-weight:800;text-transform:uppercase;letter-spacing:.08em}
.dash-kpi-val{font-size:28px;font-weight:900;color:var(--t1);line-height:1;margin-top:7px}
.dash-kpi-sub{font-size:10px;color:var(--t3);margin-top:8px}
.dash-chart-grid{display:grid;grid-template-columns:1.45fr .85fr;gap:16px;margin-bottom:16px}
.dash-chart-card{background:var(--card);border:1px solid var(--card-b);border-radius:24px;padding:20px 22px;box-shadow:0 12px 36px rgba(15,23,42,.06)}
.dash-card-head{display:flex;align-items:flex-start;justify-content:space-between;gap:10px;margin-bottom:12px}
.dash-card-title{font-size:14px;font-weight:900;color:var(--t1);display:flex;align-items:center;gap:8px}
.dash-card-sub{font-size:10px;color:var(--t3);margin-top:3px}
.dash-protocols{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:16px}
.dash-protocol{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:16px;display:flex;align-items:center;gap:12px}
.dash-protocol i{width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:var(--accent-d);color:var(--accent2);font-size:17px;flex-shrink:0}
.dash-protocol b{font-size:12px;color:var(--t1)}
.dash-protocol span{display:block;font-size:10px;color:var(--t3);margin-top:2px}
.multi-group-card{border:1px solid var(--card-b);border-radius:18px;background:linear-gradient(145deg,var(--card),var(--bg3));padding:16px;margin-bottom:12px}
.multi-group-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:12px}
.multi-group-title{font-size:14px;font-weight:900;color:var(--t1);display:flex;align-items:center;gap:8px}
.multi-protos{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.multi-protos span{font-size:10px;padding:4px 8px;border-radius:7px;background:var(--accent-d);color:var(--t2);font-weight:700}
@media(max-width:1000px){.dash-hero,.dash-chart-grid{grid-template-columns:1fr}.dash-protocols{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.dash-side,.dash-protocols{grid-template-columns:1fr}.dash-title{font-size:26px}}

</style>
</head>
<body>
<div class="bg"></div><div class="grid"></div>
<div class="orb o1"></div><div class="orb o2"></div>
<div class="wrap">
  <div class="card">
    <div class="brand">
      <div class="brand-mark">OX</div>
      <div><div class="brand-name">oxnet</div><div class="brand-sub">OXNET · v1.2.1</div></div>
    </div>
    <h1>ورود به پنل</h1>
    <p class="sub">رمز عبور را برای دسترسی به داشبورد وارد کنید</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <form id="form">
      <div class="field">
        <label>رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required>
          <i class="ti ti-lock ic"></i>
        </div>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
    </form>
    <div class="footer">OXNET · 1.2.1</div>
  </div>
</div>
<script>
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به داشبورد';
  }
});
</script>
</body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OXNET · oxnet</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#F7F8FA;--bg2:#FFFFFF;--bg3:#F1F5F9;
  --card:#FFFFFF;--card-b:rgba(15,23,42,0.10);--card-bh:rgba(15,23,42,0.20);
  --accent:#111827;--accent2:#2563EB;--accent-d:rgba(37,99,235,0.08);
  --green:#059669;--green-bg:rgba(5,150,105,0.08);--green-t:#047857;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#991B1B;
  --amber:#D97706;--amber-bg:rgba(217,119,6,0.08);--amber-t:#92400E;
  --purple:#6D28D9;--purple-bg:rgba(109,40,217,0.08);
  --t1:#111827;--t2:#334155;--t3:#64748B;
  --sidebar-w:248px;--radius:16px;
  --shadow:0 12px 34px rgba(15,23,42,0.08);
}
[data-theme="dark"]{
  --bg:#0B0D10;--bg2:#111418;--bg3:#171B21;
  --card:#151A20;--card-b:rgba(255,255,255,0.10);--card-bh:rgba(255,255,255,0.18);
  --accent:#F8FAFC;--accent2:#60A5FA;--accent-d:rgba(96,165,250,0.10);
  --green:#22C55E;--green-bg:rgba(34,197,94,0.10);--green-t:#86EFAC;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.10);--red-t:#FCA5A5;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.10);--amber-t:#FCD34D;
  --purple:#A78BFA;--purple-bg:rgba(167,139,250,0.10);
  --t1:#F8FAFC;--t2:#CBD5E1;--t3:#94A3B8;
  --shadow:0 10px 30px rgba(0,0,0,0.32);
}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg2);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s cubic-bezier(.4,0,.2,1),background .3s,border-color .3s}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b)}
.logo-img{width:38px;height:38px;border-radius:10px;overflow:hidden;border:1px solid var(--card-b);box-shadow:0 0 14px var(--accent-d);flex-shrink:0}
.logo-img img{width:100%;height:100%;object-fit:cover}
.brand-mark{width:38px;height:38px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:#0f172a;color:#fff;font-weight:800;letter-spacing:.04em;border:1px solid rgba(15,23,42,.12);box-shadow:0 8px 24px rgba(15,23,42,.12)}
.brand-mark.small{width:28px;height:28px;border-radius:8px;font-size:10px;flex-shrink:0}
.logo-name{font-size:13.5px;font-weight:700;color:var(--t1)}
.logo-sub{font-size:10px;color:var(--t3);margin-top:1px}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .15s;margin:1px 6px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t2)}
.nav-it.on{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600}
.nav-badge{margin-right:auto;background:rgba(59,130,246,0.15);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.tg-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#0098e6,#0077bb);color:#fff;border-radius:9px;padding:10px;font-size:12.5px;font-weight:600;font-family:inherit;border:none;cursor:pointer;width:100%;transition:.15s}
.tg-btn:hover{filter:brightness(1.1)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.15s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.2);cursor:pointer;width:100%;transition:.15s;margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.2)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--bg2);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px;transition:background .3s}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:28px;height:28px;border-radius:7px;overflow:hidden}
.mob-logo img{width:100%;height:100%;object-fit:cover}
.mob-title{color:var(--t1);font-size:13px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .25s}
.pg{display:none}
.pg.on{display:block;animation:none!important;opacity:1!important;transform:none!important}
@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-.02em}
.tb-title i{color:var(--accent);font-size:20px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:#A78BFA}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:17px 17px 14px;transition:all .2s;position:relative;overflow:hidden;cursor:default}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--accent);opacity:0;transition:.2s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.metric:hover::after{opacity:1}
.metric.suc::after{background:var(--green)}
.metric.dan::after{background:var(--red)}
/* ══════ صفحه ترافیک - ریدیزاین ══════ */
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:13px;margin-bottom:18px}
.traf-main-stat{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:20px;padding:22px 24px;position:relative;overflow:hidden}
.traf-main-stat::before{content:'';position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.traf-main-label{font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:10px;position:relative;z-index:1}
.traf-main-val{font-size:34px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;display:flex;align-items:baseline;gap:6px;position:relative;z-index:1}
.traf-main-val span{font-size:14px;font-weight:500;color:var(--t3)}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 10px;border-radius:20px;margin-top:12px;position:relative;z-index:1}
.traf-trend.up{background:var(--green-bg);color:var(--green-t)}
.traf-trend.down{background:var(--red-bg);color:var(--red-t)}
.traf-mini{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:18px 19px;display:flex;flex-direction:column;justify-content:space-between;transition:.2s}
.traf-mini:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.traf-mini-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:15px}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}
.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.traf-mini-val{font-size:21px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.traf-mini-sub{font-size:9.5px;color:var(--t3);margin-top:3px}

.traf-chart-card{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:22px 24px 18px;box-shadow:var(--shadow);margin-bottom:16px}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:18px}
.traf-chart-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.traf-legend{display:flex;gap:14px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--t2);font-weight:600}
.traf-legend-dot{width:8px;height:8px;border-radius:3px}
.traf-range-tabs{display:flex;gap:4px;background:var(--accent-d);padding:3px;border-radius:10px;border:1px solid var(--card-b)}
.traf-range-tab{padding:6px 13px;border-radius:8px;font-size:10.5px;font-weight:700;color:var(--t3);cursor:pointer;transition:.15s;border:none;background:transparent;font-family:inherit}
.traf-range-tab.on{background:var(--accent);color:#fff;box-shadow:0 2px 8px rgba(59,130,246,.35)}
.traf-chart-body{height:320px;margin-top:14px;position:relative}

@media(max-width:900px){.traf-hero{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.traf-hero{grid-template-columns:1fr}.traf-chart-body{height:260px}}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}
.vless-box{background:linear-gradient(135deg,var(--bg3) 0%,var(--bg2) 100%);border:1px solid var(--card-b);border-radius:18px;padding:20px 22px;margin-bottom:18px;box-shadow:var(--shadow);position:relative;overflow:hidden;transition:background .3s}
.vless-box::before{content:'';position:absolute;top:-50px;left:-50px;width:180px;height:180px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent);font-size:15px}
.vl-code{background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:9px;padding:13px 15px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.8;letter-spacing:.01em}
[data-theme="dark"] .vl-code{background:rgba(0,0,0,.04)}
.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:12px;font-weight:500;border-radius:9px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}
.btn i{font-size:13px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{background:var(--accent);color:#fff;box-shadow:0 2px 12px rgba(59,130,246,.3)}
.btn-p:hover{background:#2563EB;box-shadow:0 4px 18px rgba(59,130,246,.4)}
.btn-o{background:transparent;border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:rgba(59,130,246,.3)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(59,130,246,.15)}
.btn-g:hover{background:rgba(59,130,246,.22)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.2)}
.btn-d:hover{background:rgba(239,68,68,.2)}
.btn-pur{background:var(--purple-bg);color:#A78BFA;border:1px solid rgba(139,92,246,.2)}
.btn-pur:hover{background:rgba(139,92,246,.22)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,.2)}
.btn-amber:hover{background:rgba(245,158,11,.22)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:5px}
.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:border-color .2s,background .3s}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(59,130,246,0.05);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px}
.ch-lg{position:relative;height:330px}
.ch-sm{position:relative;height:185px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:34px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;bottom:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on{background:var(--green)}
.tog.on::after{bottom:18px}
.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.15s;min-width:100px}
[data-theme="dark"] .fi,[data-theme="dark"] .fs{background:rgba(0,0,0,.04)}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:rgba(59,130,246,.45);background:rgba(0,0,0,.25);box-shadow:0 0 0 3px rgba(59,130,246,.08)}
.fs option{background:var(--bg2)}
[data-theme="dark"] .fs option{background:#fff}
.cl{background:var(--accent-d);border:1px solid rgba(59,130,246,.15);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(245,158,11,.2);color:var(--amber-t)}
/* ══════ پنل ساخت کانفیگ - طراحی جدید ══════ */
.create-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 55%);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px;position:relative}
.create-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:220px;height:220px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px;position:relative;z-index:1}
.cp-head-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 18px rgba(59,130,246,.35)}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 24px 22px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px}
[data-theme="dark"] .cp-block{background:rgba(37,99,235,.03)}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:11px}
.cp-block-label i{color:var(--accent);font-size:14px}
.cp-input-full{width:100%;padding:10px 13px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme="dark"] .cp-input-full{background:#fff}
.cp-input-full:focus{border-color:rgba(59,130,246,.5);box-shadow:0 0 0 3px rgba(59,130,246,.1)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:8px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;white-space:nowrap}
.chip:hover{background:rgba(59,130,246,.18);color:var(--accent2)}
.chip.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 10px rgba(59,130,246,.35)}
.proto-tabs{display:flex;gap:8px;flex-wrap:wrap}
.proto-step-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;display:flex;align-items:center;gap:6px;margin-bottom:9px}
.proto-step-label i{color:var(--accent);font-size:14px}

.proto-base-cards{display:grid;grid-template-columns:1fr 1fr;gap:9px}
.proto-base-card{border:1.5px solid var(--card-b);border-radius:13px;padding:14px 12px;cursor:pointer;transition:.18s;text-align:center;position:relative;background:rgba(0,0,0,.1)}
[data-theme="dark"] .proto-base-card{background:#fff}
.proto-base-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.proto-base-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(59,130,246,.1)}
.proto-base-icon{width:34px;height:34px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:17px;margin:0 auto 8px}
.proto-base-card.active .proto-base-icon{background:var(--accent);color:#fff}
.proto-base-title{font-size:12px;font-weight:800;color:var(--t1)}
.proto-base-desc{font-size:9.5px;color:var(--t3);margin-top:3px}

.proto-transport-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.proto-t-card{border:1.5px solid var(--card-b);border-radius:13px;padding:13px 10px;cursor:pointer;transition:.18s;text-align:center;position:relative;background:rgba(0,0,0,.1)}
[data-theme="dark"] .proto-t-card{background:#fff}
.proto-t-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.proto-t-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(59,130,246,.1)}
.proto-t-icon{width:30px;height:30px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:15px;margin:0 auto 7px}
.proto-t-card.active .proto-t-icon{background:var(--accent);color:#fff}
.proto-t-title{font-size:10.5px;font-weight:800;color:var(--t1)}
.proto-t-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.4}

@media(max-width:760px){
  .proto-transport-cards{grid-template-columns:1fr}
}
.proto-tab{flex:1;min-width:120px;display:flex;align-items:center;justify-content:center;gap:7px;
  padding:11px 10px;border-radius:12px;border:1.5px solid var(--card-b);background:rgba(0,0,0,.1);
  color:var(--t2);font-family:inherit;font-size:11.5px;font-weight:700;cursor:pointer;transition:.15s}
.proto-tab.active{border-color:var(--accent);background:var(--accent-d);color:var(--accent2);
  box-shadow:0 0 0 3px rgba(59,130,246,.1)}
.proto-submodes{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.proto-card{border:1.5px solid var(--card-b);border-radius:13px;padding:13px 12px;cursor:pointer;transition:.18s;text-align:center;position:relative;background:rgba(0,0,0,.1)}
[data-theme="dark"] .proto-card{background:#fff}
.proto-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(59,130,246,.1)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-check{position:absolute;top:7px;left:7px;width:16px;height:16px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.18s}
.proto-card-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;margin:0 auto 8px}
.proto-card.active .proto-card-icon{background:var(--accent);color:#fff}
.proto-card-title{font-size:11px;font-weight:800;color:var(--t1)}
.proto-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:15px;flex-shrink:0}
.cp-submit-btn{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;border-radius:13px;padding:13px 26px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(59,130,246,.35);transition:.18s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(59,130,246,.45)}
.cp-submit-btn:active{transform:translateY(0) scale(.98)}
@media(max-width:760px){
  .cp-row{grid-template-columns:1fr}
  .proto-cards{grid-template-columns:1fr}
  .cp-footer{flex-direction:column;align-items:stretch}
  .cp-submit-btn{justify-content:center}
}
/* ══════ پنل اطلاعات سرور ══════ */
.srv-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.srv-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.srv-hero{display:flex;align-items:center;gap:14px;padding:22px 24px;position:relative;z-index:1;border-bottom:1px solid var(--card-b)}
.srv-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(59,130,246,.35)}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:15px;font-weight:800;color:var(--t1);word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px;position:relative;z-index:1}
.srv-tile{display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;transition:.18s}
[data-theme="dark"] .srv-tile{background:rgba(37,99,235,.03)}
.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.srv-tile-icon{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12px;font-weight:700;color:var(--t1);word-break:break-word}

/* ══════ پنل تغییر رمز ══════ */
.pw-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.pw-panel::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--purple-bg),transparent 70%);pointer-events:none}
.pw-hero{display:flex;align-items:center;gap:14px;padding:22px 24px 18px;position:relative;z-index:1}
.pw-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(139,92,246,.35)}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:15px;font-weight:800;color:var(--t1)}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:2px 24px 22px;position:relative;z-index:1}
.pw-field{position:relative;margin-bottom:13px}
.pw-field label{display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}
.pw-input{width:100%;padding:11px 42px 11px 14px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme="dark"] .pw-input{background:#fff}
.pw-input:focus{border-color:rgba(139,92,246,.5);box-shadow:0 0 0 3px rgba(139,92,246,.1)}
.pw-eye{position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.pw-eye:hover{color:var(--purple)}
.pw-strength{height:4px;border-radius:3px;background:var(--accent-d);margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:rgba(100,116,139,.2);transition:.25s}
.pw-strength-label{font-size:9.5px;color:var(--t3);margin-top:5px;display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px}
.pw-req{font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.18s}
.pw-req.met{background:var(--green-bg);color:var(--green-t)}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,var(--purple),#6D48D6);color:#fff;border:none;border-radius:12px;padding:12px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 18px rgba(139,92,246,.32);transition:.18s}
.pw-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(139,92,246,.42)}
.pw-submit:active{transform:translateY(0) scale(.98)}

/* ══════ اتصالات فعال - نسخه پیشرفته ══════ */
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:18px}
.conn-hero-tile{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 18px;position:relative;overflow:hidden;transition:.2s}
.conn-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--green),transparent)}
.conn-hero-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;margin-bottom:10px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-d);color:var(--accent)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.conn-hero-val{font-size:21px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.conn-hero-unit{font-size:11px;color:var(--t3);font-weight:500}

.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}
.conn-toolbar-title i{color:var(--green);font-size:15px}
.conn-live-badge{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--green-t);background:var(--green-bg);padding:5px 12px;border-radius:20px;border:1px solid rgba(16,185,129,.2)}
.conn-live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite}

.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.conn-card-v2{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:0;overflow:hidden;transition:all .22s cubic-bezier(.4,0,.2,1);position:relative}
.conn-card-v2:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 32px rgba(0,0,0,.22)}
.conn-card-v2-glow{position:absolute;top:-40px;left:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(16,185,129,.1),transparent 70%);pointer-events:none}
.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 17px 13px;position:relative;z-index:1}
.conn-avatar{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--green),#0D9668);display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;position:relative;box-shadow:0 4px 14px rgba(16,185,129,.3)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:16px;border:1.5px solid var(--green);opacity:.4;animation:breathe2 2.4s ease-in-out infinite}
@keyframes breathe2{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.12);opacity:0}}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex;transition:.15s}
.conn-ip-copy:hover{color:var(--accent)}
.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:9px;font-weight:800;padding:4px 9px;border-radius:20px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;gap:4px;white-space:nowrap;flex-shrink:0}
.conn-card-v2-divider{height:1px;background:linear-gradient(90deg,transparent,var(--card-b) 15%,var(--card-b) 85%,transparent);margin:0 17px}
.conn-card-v2-body{padding:14px 17px 16px}
.conn-proto-row{margin-bottom:12px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.conn-stat-box{display:flex;align-items:center;gap:8px}
.conn-stat-icon{width:26px;height:26px;border-radius:8px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-text-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.conn-stat-text-val{font-size:11.5px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-duration-track{height:5px;border-radius:4px;background:var(--accent-d);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--green),#3FD79C);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);width:40%;animation:shimmer 1.8s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}

.conn-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:20px}
.conn-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--t3);margin:0 auto 16px}
.conn-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.conn-empty-v2-sub{font-size:11px;color:var(--t3)}

@media(max-width:760px){.conn-hero{grid-template-columns:1fr 1fr}}
@media(max-width:500px){.conn-grid-v2{grid-template-columns:1fr}}

@media(max-width:560px){.srv-tiles{grid-template-columns:1fr}}
.cl.amber i{color:var(--amber)}
.sub-box{background:rgba(139,92,246,.07);border:1px solid rgba(139,92,246,.2);border-radius:10px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:11px}
.sub-url{font-family:ui-monospace,monospace;font-size:10.5px;color:#A78BFA;word-break:break-all;flex:1}
.spbar{height:4px;border-radius:3px;background:var(--accent-d);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1s}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
/* ══════ گروه‌های ساب - ریدیزاین کامل ══════ */
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:11px 40px 11px 15px;border-radius:12px;border:1px solid var(--card-b);background:var(--card);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
.subs-search input:focus{border-color:rgba(139,92,246,.5);box-shadow:0 0 0 3px rgba(139,92,246,.1)}
.subs-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}

.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:18px}
.sub-card{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:0;overflow:hidden;transition:all .25s cubic-bezier(.4,0,.2,1);position:relative}
.sub-card:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:0 16px 36px rgba(0,0,0,.24)}
.sub-card-top{background:linear-gradient(155deg,var(--purple-bg) 0%,transparent 65%);padding:20px 20px 16px;position:relative}
.sub-card-top::before{content:'';position:absolute;top:-30px;left:-30px;width:130px;height:130px;background:radial-gradient(circle,rgba(139,92,246,.14),transparent 70%);pointer-events:none}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:13px;position:relative;z-index:1}
.sub-card-icon{width:46px;height:46px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 16px rgba(139,92,246,.35)}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:15.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}

.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative;z-index:1;margin-top:16px;background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:13px;overflow:hidden}
[data-theme="dark"] .sub-card-stats{background:rgba(124,58,237,.03)}
.sub-card-stat{padding:11px 8px;text-align:center;border-left:1px solid var(--card-b)}
.sub-card-stat:last-child{border-left:none}
.sub-card-stat-val{font-size:15px;font-weight:800;color:var(--t1);line-height:1.2}
.sub-card-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}

.sub-card-url-row{margin:14px 20px 0;background:rgba(139,92,246,.08);border:1px dashed rgba(139,92,246,.25);border-radius:11px;padding:9px 12px;display:flex;align-items:center;gap:8px}
.sub-card-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:#A78BFA;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-url-copy{background:none;border:none;color:var(--purple);cursor:pointer;font-size:13px;padding:3px;display:flex;flex-shrink:0;transition:.15s}
.sub-card-url-copy:hover{color:#A78BFA;transform:scale(1.1)}

.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}

.subs-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:20px;grid-column:1/-1}
.subs-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--purple-bg);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--purple);margin:0 auto 16px}
.subs-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.subs-empty-v2-sub{font-size:11px;color:var(--t3)}

/* ══════ مودال ساخت گروه - نسخه فشرده ══════ */
.modal-v2{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:0;max-width:430px;width:calc(100% - 32px);max-height:92vh;overflow-y:auto;position:relative;animation:fi .2s ease;box-shadow:0 24px 70px rgba(0,0,0,.5)}
.modal-v2-head{background:linear-gradient(155deg,rgba(139,92,246,.14) 0%,transparent 65%);padding:18px 22px 14px;position:relative;overflow:hidden}
.modal-v2-head::before{content:'';position:absolute;top:-50px;left:-50px;width:160px;height:160px;background:radial-gradient(circle,rgba(139,92,246,.2),transparent 70%);pointer-events:none}
.modal-v2-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:9px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:.15s}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(239,68,68,.25)}
.modal-v2-icon{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;margin-bottom:10px;position:relative;z-index:1;box-shadow:0 8px 18px rgba(139,92,246,.4)}
.modal-v2-title{font-size:15.5px;font-weight:800;color:var(--t1);position:relative;z-index:1;letter-spacing:-.01em}
.modal-v2-sub{font-size:10.5px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:16px 22px 20px;border-top:1px solid var(--card-b)}
.modal-v2-field{margin-bottom:11px}
.modal-v2-field label{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.modal-v2-field label i{color:var(--purple);font-size:13px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none;transition:.15s;z-index:1}
.modal-v2-input{width:100%;padding:9px 38px 9px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
[data-theme="dark"] .modal-v2-input{background:rgba(124,58,237,.04)}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-input:focus{border-color:rgba(139,92,246,.55);box-shadow:0 0 0 3px rgba(139,92,246,.12);background:rgba(0,0,0,.28)}
[data-theme="dark"] .modal-v2-input:focus{background:#fff}
.modal-v2-input:focus~i{color:var(--purple)}
.modal-v2-hint{background:rgba(59,130,246,.08);border:1px solid rgba(59,130,246,.18);border-radius:11px;padding:9px 12px;font-size:10px;color:var(--t2);display:flex;gap:7px;align-items:flex-start;line-height:1.6;margin-top:2px}
.modal-v2-hint i{font-size:14px;color:var(--accent);margin-top:1px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:8px;margin-top:15px}
.modal-v2-btn-cancel{flex:.75;justify-content:center;padding:10px;border-radius:11px;background:transparent;border:1px solid var(--card-b);color:var(--t2);font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;transition:.15s;display:flex;align-items:center}
.modal-v2-btn-cancel:hover{background:var(--accent-d);color:var(--t1)}
.modal-v2-btn-submit{flex:1;justify-content:center;padding:10px;border-radius:11px;background:linear-gradient(135deg,var(--purple),#6D48D6);color:#fff;border:none;font-family:inherit;font-size:12px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;box-shadow:0 6px 18px rgba(139,92,246,.4);transition:.18s}
.modal-v2-btn-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(139,92,246,.5)}
.modal-v2-btn-submit:active{transform:translateY(0) scale(.98)}

/* ══════ مودال انتخاب کانفیگ - نسخه پیشرفته ══════ */
.lmodal-head{background:linear-gradient(155deg,var(--accent-d) 0%,transparent 70%);padding:22px 24px 18px;position:relative;border-bottom:1px solid var(--card-b)}
.lmodal-icon-row{display:flex;align-items:center;gap:12px;position:relative;z-index:1}
.lmodal-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;box-shadow:0 6px 16px rgba(59,130,246,.35)}
.lmodal-title-v2{font-size:14.5px;font-weight:800;color:var(--t1)}
.lmodal-sub-v2{font-size:10.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:14px;position:relative}
.lmodal-search input{width:100%;padding:10px 38px 10px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none}
[data-theme="dark"] .lmodal-search input{background:#fff}
.lmodal-search input:focus{border-color:rgba(59,130,246,.5);box-shadow:0 0 0 3px rgba(59,130,246,.1)}
.lmodal-search i{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:11px;position:relative;z-index:1}
.lmodal-qbtn{font-size:10px;font-weight:700;padding:5px 11px;border-radius:8px;background:var(--accent-d);color:var(--accent2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;font-family:inherit}
.lmodal-qbtn:hover{background:rgba(59,130,246,.2)}
.lmodal-count{margin-right:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}

.lmodal-list{padding:10px 14px;max-height:360px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:11px;padding:11px 12px;border-radius:13px;cursor:pointer;transition:.15s;margin-bottom:4px;border:1px solid transparent}
.lrow-v2:hover{background:var(--accent-d)}
.lrow-v2.checked{background:rgba(59,130,246,.1);border-color:rgba(59,130,246,.25)}
.lrow-v2-check{width:20px;height:20px;border-radius:7px;border:2px solid var(--card-b);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s;background:rgba(0,0,0,.14)}
.lrow-v2.checked .lrow-v2-check{background:var(--accent);border-color:var(--accent)}
.lrow-v2-check i{font-size:12px;color:#fff;opacity:0;transform:scale(.5);transition:.15s}
.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}
.lrow-v2-avatar{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.lrow-v2.checked .lrow-v2-avatar{background:var(--accent);color:#fff}
.lrow-v2-info{flex:1;min-width:0}
.lrow-v2-name{font-size:12.5px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-v2-meta{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.lrow-v2-status{font-size:9px;font-weight:800;padding:3px 9px;border-radius:20px;flex-shrink:0;white-space:nowrap}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}
.lrow-v2-status.off{background:var(--red-bg);color:var(--red-t)}

.lmodal-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 24px;border-top:1px solid var(--card-b)}
.lmodal-footer-info{font-size:10.5px;color:var(--t3);display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--accent)}
.lmodal-footer-btns{display:flex;gap:8px}

@media(max-width:500px){.sub-grid{grid-template-columns:1fr}.sub-card-stats{grid-template-columns:repeat(3,1fr)}}

.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:28px 26px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:fi .2s ease}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--accent)}
.lrow{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid rgba(59,130,246,.05)}
.lrow:last-child{border-bottom:none}
.lrow-check{width:16px;height:16px;border-radius:4px;cursor:pointer;accent-color:var(--accent)}
.lrow-label{flex:1;font-size:12px;color:var(--t1)}
.lrow-badge{font-size:9px;padding:2px 7px;border-radius:5px;background:var(--green-bg);color:var(--green-t);font-weight:700}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.3);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.3);background:var(--red-bg);color:var(--red-t)}
/* ══════ نوار اعلان‌های همگانی ══════ */
.ann-banner-wrap{display:flex;flex-direction:column;gap:10px;margin-bottom:18px}
.ann-card{position:relative;display:flex;gap:13px;background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:15px 44px 15px 17px;box-shadow:var(--shadow);animation:fi .25s ease;overflow:hidden}
.ann-card::before{content:'';position:absolute;top:0;right:0;width:4px;height:100%}
.ann-card.news::before{background:var(--accent)}
.ann-card.ad::before{background:var(--purple)}
.ann-card.warning::before{background:var(--amber)}
.ann-card.urgent::before{background:var(--red)}
.ann-icon{width:38px;height:38px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
.ann-card.news .ann-icon{background:var(--accent-d);color:var(--accent2)}
.ann-card.ad .ann-icon{background:var(--purple-bg);color:var(--purple)}
.ann-card.warning .ann-icon{background:var(--amber-bg);color:var(--amber-t)}
.ann-card.urgent .ann-icon{background:var(--red-bg);color:var(--red-t)}
.ann-body{flex:1;min-width:0}
.ann-title{font-size:13px;font-weight:700;color:var(--t1);margin-bottom:4px}
.ann-text{font-size:12px;color:var(--t2);line-height:1.8}
.ann-img{max-width:100%;border-radius:10px;margin-top:10px;border:1px solid var(--card-b);display:block}
.ann-close{position:absolute;top:10px;left:10px;width:24px;height:24px;border-radius:7px;background:var(--accent-d);border:none;color:var(--t3);font-size:13px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.ann-close:hover{background:var(--red-bg);color:var(--red-t)}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}

.info-strip{display:flex;align-items:center;background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 22px;margin-bottom:16px;gap:0;flex-wrap:wrap;box-shadow:var(--shadow)}
.info-item{display:flex;flex-direction:column;gap:6px;flex:1;min-width:130px;padding:0 18px;position:relative}
.info-item:not(:first-child)::before{content:'';position:absolute;right:0;top:2px;bottom:2px;width:1px;background:var(--card-b)}
.info-item-label{font-size:10.5px;color:var(--t3);font-weight:700}
.info-item-val{display:flex;align-items:center;gap:7px;font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.info-item-val i{color:var(--accent);font-size:16px}
.info-item-val .info-badge{font-size:11px;font-weight:800;background:var(--green-bg);color:var(--green-t);padding:2px 9px;border-radius:20px}
@media(max-width:760px){.info-strip{gap:14px}.info-item{min-width:45%;padding:0 0 10px}.info-item:not(:first-child)::before{display:none}}

/* ══════ کانفیگ‌ها - طراحی ردیفی حرفه‌ای ══════ */
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:var(--card);border:1px solid var(--card-b);border-radius:14px;padding:0;transition:all .2s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 6px 24px rgba(0,0,0,.18)}
.cfg-card.is-off{opacity:.6}
.cfg-card.is-exp{opacity:.78}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px}
.cfg-status-dot{width:9px;height:9px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);background:var(--accent-d);padding:2px 7px;border-radius:5px;cursor:pointer;transition:.15s}
.cfg-uuid-mini:hover{background:rgba(59,130,246,.2)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:5px;border-radius:4px;background:rgba(59,130,246,0.1);overflow:hidden}
.ubar-f{height:100%;border-radius:4px;transition:width .4s ease}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.proto-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;white-space:nowrap}
.pc-ws{background:var(--accent-d);color:var(--accent2)}
.pc-xhttp{background:var(--purple-bg);color:#A78BFA}
.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:var(--purple);font-size:11px}
.tog{width:19px;height:30px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;top:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on::after{top:14px}
.tog.on{background:var(--green)}

@media(max-width:880px){
  .cfg-row{flex-wrap:wrap}
  .cfg-divider-v{display:none}
  .cfg-usage-col{min-width:100%;order:5}
}

/* ── زیر ۷۶۸px: تبدیل کامل به کارت موبایل ── */
@media(max-width:768px){
  .cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}
  .cfg-card{border-radius:16px}
  .cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}
  .cfg-row-top{display:flex;align-items:center;justify-content:space-between;gap:10px}
  .cfg-identity{min-width:0;flex:1}
  .cfg-usage-col{min-width:0}
  .cfg-exp-col{min-width:0}
  .cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}
  .cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;margin-top:2px;width:100%}
}

/* ══════ اتصالات فعال با IP ══════ */
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.conn-card{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:15px 17px;transition:.2s;position:relative;overflow:hidden}
.conn-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.conn-card::before{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}
.conn-ip-row{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.conn-ip-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}
.conn-ip{font-family:ui-monospace,monospace;font-size:13px;font-weight:700;color:var(--t1)}
.conn-label{font-size:10.5px;color:var(--t3);margin-top:1px}
.conn-meta{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--t3);padding-top:10px;border-top:1px solid var(--card-b)}

/* ══════ لاگ فعالیت‌ها ══════ */
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid rgba(59,130,246,.05);position:relative}
.log-item:last-child{border-bottom:none}
.log-ic{width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.log-ic.err{background:var(--red-bg);color:var(--red-t)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-ic.info{background:var(--accent-d);color:var(--accent2)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:8.5px;padding:1px 7px;border-radius:10px;background:var(--accent-d);color:var(--accent2);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.erow{padding:9px 0;border-bottom:1px solid rgba(59,130,246,.05)}
.erow:last-child{border-bottom:none}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px;display:flex;align-items:center;gap:4px}
.emsg{color:var(--red-t);font-family:ui-monospace,monospace;background:var(--red-bg);padding:6px 9px;border-radius:6px;word-break:break-all;font-size:10.5px}

@media(max-width:1050px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.4)}
  .sb-close{display:flex}
  .main{margin-right:0;padding-top:70px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:62px 12px 50px}
  .sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}
}
/* ══════ نسخه و بروزرسانی — دیزاین جدید ══════ */
.upd-hero{background:linear-gradient(150deg,var(--bg3) 0%,var(--card) 65%);border:1px solid var(--card-b);border-radius:24px;padding:26px 26px 22px;position:relative;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px}
.upd-hero-glow{position:absolute;top:-70px;left:-70px;width:260px;height:260px;background:radial-gradient(circle,rgba(59,130,246,.14),transparent 70%);pointer-events:none}
.upd-hero-top{display:flex;align-items:flex-start;justify-content:space-between;gap:14px;position:relative;z-index:1;flex-wrap:wrap;margin-bottom:14px}
.upd-hero-cur{display:flex;align-items:center;gap:14px}
.upd-hero-icon{width:52px;height:52px;border-radius:16px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:24px;flex-shrink:0;box-shadow:0 8px 22px rgba(59,130,246,.35)}
.upd-hero-label{font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:4px}
.upd-hero-ver{font-size:26px;font-weight:800;color:var(--t1);letter-spacing:-.02em}
.upd-hero-desc{font-size:12.5px;color:var(--t2);line-height:1.8;position:relative;z-index:1;margin-bottom:14px;background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:12px;padding:12px 14px}
[data-theme="dark"] .upd-hero-desc{background:rgba(37,99,235,.03)}
.upd-hero-meta{display:flex;gap:8px;flex-wrap:wrap;position:relative;z-index:1}
.upd-meta-chip{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--t2);background:var(--accent-d);border:1px solid var(--card-b);padding:6px 12px;border-radius:20px}
.upd-meta-chip i{color:var(--accent);font-size:13px}
.upd-pill{display:inline-flex;align-items:center;gap:6px;font-size:11px;font-weight:800;padding:6px 14px;border-radius:20px}
.upd-pill-blue{background:var(--accent-d);color:var(--accent2)}
.upd-pill-green{background:var(--green-bg);color:var(--green-t)}
.upd-pill-amber{background:var(--amber-bg);color:var(--amber-t)}
.upd-dot{width:6px;height:6px;border-radius:50%;background:currentColor;animation:pulse 1.6s infinite}

.upd-latest-card{background:linear-gradient(120deg,var(--amber) 0%,#D97706 100%);border-radius:22px;padding:20px 24px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:16px;box-shadow:0 12px 32px rgba(245,158,11,.28);position:relative;overflow:hidden}
.upd-latest-card::before{content:'';position:absolute;top:-40px;left:-40px;width:180px;height:180px;background:radial-gradient(circle,rgba(255,255,255,.18),transparent 70%);pointer-events:none}
.upd-latest-left{display:flex;align-items:center;gap:14px;position:relative;z-index:1;min-width:220px}
.upd-latest-icon{width:48px;height:48px;border-radius:14px;background:rgba(255,255,255,.22);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0}
.upd-latest-title{font-size:13px;font-weight:800;color:#fff;opacity:.92}
.upd-latest-ver{font-size:18px;font-weight:800;color:#fff;margin-top:2px}
.upd-latest-desc{font-size:11.5px;color:rgba(255,255,255,.88);margin-top:4px;line-height:1.7;max-width:440px}
.upd-install-btn{background:#fff;color:#B45309;border:none;border-radius:14px;padding:13px 24px;font-family:inherit;font-size:13.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 18px rgba(0,0,0,.18);transition:.18s;position:relative;z-index:1;white-space:nowrap}
.upd-install-btn:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(0,0,0,.24)}
.upd-install-btn:active{transform:translateY(0) scale(.98)}
.upd-install-btn:disabled{opacity:.6;cursor:not-allowed;transform:none}

.upd-progress-card{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:18px 20px;margin-bottom:16px;box-shadow:var(--shadow)}
.upd-progress-head{display:flex;align-items:center;gap:12px;margin-bottom:12px}
.upd-progress-icon{width:38px;height:38px;border-radius:11px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
.upd-progress-title{font-size:13px;font-weight:800;color:var(--t1)}
.upd-progress-txt{font-size:10.5px;color:var(--t3);margin-top:2px}
.upd-progress-pct{font-size:16px;font-weight:800;color:var(--accent2);flex-shrink:0}
.upd-progress-track{height:8px;border-radius:6px;background:var(--accent-d);overflow:hidden}
.upd-progress-fill{height:100%;border-radius:6px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width .4s ease;position:relative;overflow:hidden}
.upd-progress-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.4),transparent);width:40%;animation:shimmer 1.6s linear infinite}

.upd-log-card{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:18px 20px;margin-bottom:20px;box-shadow:var(--shadow)}
.upd-log-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}
.upd-log-title{font-size:12.5px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:7px}
.upd-log-title i{color:var(--accent);font-size:16px}
.upd-log-box{background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:12px;padding:14px 16px;max-height:240px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:2}
[data-theme="dark"] .upd-log-box{background:rgba(0,0,0,.03)}
.upd-log-empty{color:var(--t3)}
.upd-log-line{color:var(--t2);white-space:pre-wrap;word-break:break-all}
.upd-log-line.err{color:var(--red-t)}
.upd-log-line.ok{color:var(--green-t)}

.upd-history-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.upd-history-title{font-size:13px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:7px}
.upd-history-title i{color:var(--accent);font-size:17px}

.upd-timeline{position:relative;display:flex;flex-direction:column;gap:0}
.upd-timeline::before{content:'';position:absolute;top:8px;bottom:8px;right:19px;width:2px;background:linear-gradient(180deg,var(--card-b),transparent)}
.upd-item{display:flex;gap:16px;padding:0 0 20px;position:relative}
.upd-item:last-child{padding-bottom:0}
.upd-item-dot-wrap{position:relative;z-index:1;flex-shrink:0}
.upd-item-dot{width:40px;height:40px;border-radius:13px;background:var(--card);border:2px solid var(--green);display:flex;align-items:center;justify-content:center;color:var(--green-t);font-size:17px;box-shadow:var(--shadow)}
.upd-item.err .upd-item-dot{border-color:var(--red);color:var(--red-t)}
.upd-item-card{flex:1;background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:14px 17px;transition:.18s;min-width:0}
.upd-item-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.upd-item-head{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-bottom:6px}
.upd-item-versions{font-size:13.5px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.upd-item-versions .arrow{color:var(--t3);font-size:14px}
.upd-item-versions .to{color:var(--accent2)}
.upd-item-time{font-size:10px;color:var(--t3);display:flex;align-items:center;gap:5px;white-space:nowrap}
.upd-item-desc{font-size:11.5px;color:var(--t2);line-height:1.8;margin-top:6px}
.upd-item-badge{font-size:9px;font-weight:800;padding:3px 9px;border-radius:20px;flex-shrink:0}
.upd-item-badge.ok{background:var(--green-bg);color:var(--green-t)}
.upd-item-badge.err{background:var(--red-bg);color:var(--red-t)}
.upd-item-err-box{margin-top:8px;background:var(--red-bg);border:1px solid rgba(239,68,68,.2);border-radius:9px;padding:8px 11px;font-size:10.5px;color:var(--red-t);font-family:ui-monospace,monospace;word-break:break-all}
.upd-history-empty{text-align:center;padding:50px 20px;color:var(--t3);background:var(--card);border:1px dashed var(--card-b);border-radius:18px}
.upd-history-empty i{font-size:36px;opacity:.35;margin-bottom:10px;display:block}

/* ══════ بخش حذف‌شده ══════ */
.sup-wrap{max-width:1450px;background:var(--card);border:1px solid var(--card-b);border-radius:24px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.sup-wrap::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none;z-index:0}
.sup-head{display:flex;align-items:center;gap:13px;padding:18px 22px;border-bottom:1px solid var(--card-b);background:linear-gradient(155deg,var(--accent-d) 0%,transparent 75%);position:relative;z-index:1}
.sup-head-icon{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;box-shadow:0 6px 16px rgba(59,130,246,.35);position:relative}
.sup-head-icon::after{content:'';position:absolute;inset:-5px;border-radius:16px;border:1.5px solid var(--accent);opacity:.4;animation:supBreathe 2.4s ease-in-out infinite}
@keyframes supBreathe{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.1);opacity:0}}
.sup-head-text{flex:1;min-width:0}
.sup-head-title{font-size:14.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.sup-head-sub{font-size:10.5px;color:var(--t3);margin-top:3px;display:flex;align-items:center;gap:6px}
.sup-head-sub .sdot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite;flex-shrink:0}
.sup-close-btn{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.2);border-radius:10px;padding:8px 14px;font-family:inherit;font-size:11px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.15s}
.sup-close-btn:hover{background:rgba(239,68,68,.2);transform:translateY(-1px)}
.sup-blocked-banner{background:var(--red-bg);color:var(--red-t);font-size:11.5px;font-weight:700;padding:11px 22px;display:flex;align-items:center;gap:8px;border-bottom:1px solid var(--card-b);position:relative;z-index:1}
 
#support-msgs{height:370px;overflow-y:auto;display:flex;flex-direction:column;gap:2px;padding:20px;background:var(--bg2);position:relative;z-index:1;scroll-behavior:smooth}
#support-msgs::-webkit-scrollbar{width:5px}
#support-msgs::-webkit-scrollbar-thumb{background:var(--card-b);border-radius:3px}
 
.sup-date-sep{text-align:center;font-size:9.5px;color:var(--t3);font-weight:700;margin:14px 0 10px;position:relative}
.sup-date-sep span{background:var(--bg2);padding:0 12px;position:relative;z-index:1}
.sup-date-sep::before{content:'';position:absolute;top:50%;right:0;left:0;height:1px;background:var(--card-b);z-index:0}
 
.sup-msg-row{display:flex;align-items:flex-end;gap:8px;margin-bottom:10px;max-width:100%}
.sup-msg-row.client{margin-right:0;margin-left:auto;flex-direction:row-reverse}
.sup-msg-row.admin{margin-left:0; display: flex; justify-content: left}
.sup-avatar{width:26px;height:26px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0;margin-bottom:2px}
.sup-avatar.admin{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff}
.sup-avatar.client{background:var(--purple-bg);color:var(--purple)}
.sup-msg{padding:10px 15px;border-radius:16px;font-size:12.8px;line-height:1.75;word-break:break-word;position:relative;box-shadow:0 1px 2px rgba(0,0,0,.06)}
.sup-msg.client{background:var(--accent);color:#fff;border-bottom-right-radius:5px}
.sup-msg.admin{background:var(--card);color:var(--t1);border:1px solid var(--card-b);border-bottom-left-radius:5px}
.sup-msg .sup-time{display:flex;align-items:center;gap:4px;font-size:9px;opacity:.68;margin-top:5px;justify-content:flex-end}
.sup-msg .sup-time i{font-size:12px}
.sup-msg.client .sup-time i.seen{color:#fff}
 
.sup-empty{color:var(--t3);font-size:12px;text-align:center;padding:60px 20px;display:flex;flex-direction:column;align-items:center;gap:12px}
.sup-empty i{font-size:38px;opacity:.35}
.sup-empty b{color:var(--t2);font-size:13px;font-weight:700}
 
.sup-input-row{display:flex;gap:10px;padding:16px 18px;background:var(--card);border-top:1px solid var(--card-b);position:relative;z-index:1}
.sup-input-row input{margin-bottom:0;border-radius:13px;padding:12px 16px}
.sup-input-row button{border-radius:13px;padding:0 18px;display:flex;align-items:center;justify-content:center}
.sup-input-row.disabled{opacity:.55;pointer-events:none}
 
.sup-new-badge{display:inline-flex;align-items:center;gap:4px;background:var(--red);color:#fff;font-size:9px;font-weight:800;padding:2px 8px;border-radius:20px;margin-right:6px;animation:pulse 1.6s infinite}

/* ══════ مودال ساخت کانفیگ - نسخه حرفه‌ای ══════ */
.cm-modal{max-width:620px;width:calc(100% - 32px);padding:0;border-radius:24px;overflow:hidden;
  max-height:92vh;display:flex;flex-direction:column}
.cm-head{background:linear-gradient(155deg,rgba(59,130,246,.14) 0%,transparent 70%);
  padding:26px 28px 20px;position:relative;border-bottom:1px solid var(--card-b);flex-shrink:0}
.cm-head::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;
  background:radial-gradient(circle,rgba(59,130,246,.18),transparent 70%);pointer-events:none}
.cm-head-row{display:flex;align-items:center;gap:14px;position:relative;z-index:1}
.cm-head-icon{width:46px;height:46px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));
  display:flex;align-items:center;justify-content:center;color:#fff;font-size:21px;flex-shrink:0;
  box-shadow:0 8px 20px rgba(59,130,246,.35)}
.cm-head-title{font-size:16.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cm-head-sub{font-size:11px;color:var(--t3);margin-top:3px}
.cm-close{position:absolute;top:18px;left:18px;background:rgba(0,0,0,.18);border:1px solid var(--card-b);
  color:var(--t2);width:32px;height:32px;border-radius:10px;font-size:15px;display:flex;align-items:center;
  justify-content:center;cursor:pointer;z-index:2;transition:.15s}
.cm-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(239,68,68,.25)}

.cm-body{padding:22px 28px 8px;overflow-y:auto;flex:1}
.cm-section{margin-bottom:20px}
.cm-section-label{font-size:10.5px;font-weight:800;color:var(--t3);text-transform:uppercase;
  letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:10px}
.cm-section-label i{color:var(--accent);font-size:14px}

.cm-field{margin-bottom:14px}
.cm-field label{display:block;font-size:11px;font-weight:700;color:var(--t2);margin-bottom:7px}
.cm-input{width:100%;padding:11px 14px;border-radius:11px;border:1px solid var(--card-b);
  background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12.8px;outline:none;transition:.15s}
[data-theme="dark"] .cm-input{background:rgba(37,99,235,.03)}
.cm-input:focus{border-color:rgba(59,130,246,.5);box-shadow:0 0 0 3px rgba(59,130,246,.1)}
.cm-input::placeholder{color:var(--t3)}
.cm-row2{display:grid;grid-template-columns:1fr 1fr;gap:12px}

/* ── آکاردئون کشویی انتخاب پروتکل / ترابرد ── */
.cm-dd{border:1px solid var(--card-b);border-radius:14px;overflow:hidden;background:rgba(0,0,0,.1);transition:.18s}
[data-theme="dark"] .cm-dd{background:#fff}
.cm-dd.open{border-color:var(--card-bh);box-shadow:0 0 0 3px rgba(59,130,246,.08)}
.cm-dd-trigger{display:flex;align-items:center;gap:12px;padding:13px 15px;cursor:pointer;user-select:none}
.cm-dd-icon{width:38px;height:38px;border-radius:11px;background:var(--accent-d);color:var(--accent);
  display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;transition:.18s}
.cm-dd-text{flex:1;min-width:0}
.cm-dd-title{font-size:13px;font-weight:800;color:var(--t1)}
.cm-dd-desc{font-size:10px;color:var(--t3);margin-top:2px}
.cm-dd-chev{color:var(--t3);font-size:16px;transition:transform .2s;flex-shrink:0}
.cm-dd.open .cm-dd-chev{transform:rotate(180deg);color:var(--accent)}

.cm-dd-panel{display:grid;grid-template-rows:0fr;transition:grid-template-rows .22s ease}
.cm-dd.open .cm-dd-panel{grid-template-rows:1fr}
.cm-dd-panel-inner{overflow:hidden}
.cm-dd-list{border-top:1px solid var(--card-b);padding:6px}
.cm-opt{display:flex;align-items:center;gap:11px;padding:10px 11px;border-radius:10px;cursor:pointer;transition:.14s;margin-bottom:2px}
.cm-opt:hover{background:var(--accent-d)}
.cm-opt.sel{background:rgba(59,130,246,.12)}
.cm-opt-radio{width:18px;height:18px;border-radius:50%;border:2px solid var(--card-b);flex-shrink:0;
  display:flex;align-items:center;justify-content:center;transition:.14s}
.cm-opt.sel .cm-opt-radio{border-color:var(--accent)}
.cm-opt-radio::after{content:'';width:9px;height:9px;border-radius:50%;background:var(--accent);
  transform:scale(0);transition:.14s}
.cm-opt.sel .cm-opt-radio::after{transform:scale(1)}
.cm-opt-icon{width:30px;height:30px;border-radius:9px;background:var(--accent-d);color:var(--accent);
  display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.cm-opt.sel .cm-opt-icon{background:var(--accent);color:#fff}
.cm-opt-text{flex:1;min-width:0}
.cm-opt-title{font-size:12px;font-weight:700;color:var(--t1)}
.cm-opt-desc{font-size:9.5px;color:var(--t3);margin-top:1px}
.cm-opt-tag{font-size:8.5px;font-weight:800;padding:2px 7px;border-radius:6px;background:var(--green-bg);
  color:var(--green-t);flex-shrink:0}

.cm-pills{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.cm-pill{padding:6px 13px;border-radius:20px;font-size:10.5px;font-weight:700;color:var(--t2);
  background:transparent;border:1px solid var(--card-b);cursor:pointer;transition:.15s;font-family:inherit}
.cm-pill:hover{background:var(--accent-d)}
.cm-pill.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 10px rgba(59,130,246,.3)}

.cm-note{font-size:10.5px;color:var(--t3);display:flex;align-items:flex-start;gap:7px;
  background:var(--accent-d);border-radius:10px;padding:10px 13px;line-height:1.7;margin-top:4px}
.cm-note i{color:var(--accent);font-size:14px;flex-shrink:0;margin-top:1px}

.cm-footer{display:flex;gap:10px;padding:16px 28px;border-top:1px solid var(--card-b);flex-shrink:0;
  background:var(--card)}
.cm-btn-cancel{flex:.55;justify-content:center;padding:12px;border-radius:12px;background:transparent;
  border:1px solid var(--card-b);color:var(--t2);font-family:inherit;font-size:12.5px;font-weight:700;
  cursor:pointer;transition:.15s;display:flex;align-items:center}
.cm-btn-cancel:hover{background:var(--accent-d);color:var(--t1)}
.cm-btn-submit{flex:1;justify-content:center;padding:12px;border-radius:12px;
  background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;
  font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;
  gap:7px;box-shadow:0 6px 18px rgba(59,130,246,.4);transition:.18s}
.cm-btn-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(59,130,246,.5)}
.cm-btn-submit:active{transform:translateY(0) scale(.98)}

/* دسکتاپ بزرگ‌تر */
@media(min-width:900px){
  .cm-modal{max-width:680px}
  .cm-body{padding:24px 34px 8px}
  .cm-head{padding:28px 34px 22px}
  .cm-footer{padding:18px 34px}
}

/* موبایل = باتم‌شیت */
@media(max-width:640px){
  #modal-create-link.modal-bg{align-items:flex-end}
  .cm-modal{max-width:100%;width:100%;border-radius:22px 22px 0 0;max-height:90vh;
    animation:cmSlideUp .28s cubic-bezier(.32,.72,0,1)}
  .cm-row2{grid-template-columns:1fr}
  .cm-head{padding:20px 18px 16px}
  .cm-body{padding:18px 18px 6px}
  .cm-footer{padding:14px 18px 18px}
}
@keyframes cmSlideUp{from{transform:translateY(100%)}to{transform:translateY(0)}}

</style>

<style id="oxnet-dashboard-redesign">
#pg-overview,#pg-overview *{opacity:1!important;filter:none!important}#pg-overview{color:var(--t1)!important}.dash-main-card,.dash-kpi,.dash-protocol,.vless-box,.dash-chart-card,.card{box-shadow:0 12px 36px rgba(15,23,42,.09)!important}
.pc-ss{background:rgba(20,184,166,.12);color:#0F766E}[data-theme="dark"] .pc-ss{color:#5EEAD4}
.dash-hero{display:grid;grid-template-columns:1.35fr .9fr;gap:16px;margin-bottom:18px}.dash-main-card{position:relative;overflow:hidden;border-radius:26px;padding:28px;border:1px solid var(--card-b);background:linear-gradient(145deg,var(--card) 0%,var(--bg3) 100%);box-shadow:0 18px 60px rgba(15,23,42,.08)}.dash-main-card:before{content:'';position:absolute;inset:auto -110px -140px auto;width:340px;height:340px;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.16),transparent 68%)}.dash-eyebrow{font-size:11px;font-weight:800;letter-spacing:.14em;color:var(--t3);text-transform:uppercase;margin-bottom:10px}.dash-title{font-size:34px;font-weight:900;letter-spacing:-.04em;color:var(--t1);line-height:1.2;margin-bottom:8px}.dash-title span{color:var(--accent2)}.dash-desc{max-width:620px;color:var(--t2);font-size:13px;line-height:2}.dash-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}.dash-side{display:grid;grid-template-columns:1fr 1fr;gap:12px}.dash-kpi{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:18px;box-shadow:0 10px 30px rgba(15,23,42,.05)}.dash-kpi-icon{width:36px;height:36px;border-radius:12px;display:flex;align-items:center;justify-content:center;background:var(--accent-d);color:var(--accent2);font-size:18px;margin-bottom:14px}.dash-kpi-label{font-size:10px;color:var(--t3);font-weight:800;text-transform:uppercase;letter-spacing:.08em}.dash-kpi-val{font-size:28px;font-weight:900;color:var(--t1);line-height:1;margin-top:7px}.dash-kpi-sub{font-size:10px;color:var(--t3);margin-top:8px}.dash-chart-grid{display:grid;grid-template-columns:1.45fr .85fr;gap:16px;margin-bottom:16px}.dash-chart-card{background:var(--card);border:1px solid var(--card-b);border-radius:24px;padding:20px 22px;box-shadow:0 12px 36px rgba(15,23,42,.06)}.dash-card-head{display:flex;align-items:flex-start;justify-content:space-between;gap:10px;margin-bottom:12px}.dash-card-title{font-size:14px;font-weight:900;color:var(--t1);display:flex;align-items:center;gap:8px}.dash-card-sub{font-size:10px;color:var(--t3);margin-top:3px}.dash-protocols{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:16px}.dash-protocol{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:16px;display:flex;align-items:center;gap:12px}.dash-protocol i{width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:var(--accent-d);color:var(--accent2);font-size:17px;flex-shrink:0}.dash-protocol b{font-size:12px;color:var(--t1)}.dash-protocol span{display:block;font-size:10px;color:var(--t3);margin-top:2px}.multi-group-card{border:1px solid var(--card-b);border-radius:18px;background:linear-gradient(145deg,var(--card),var(--bg3));padding:16px;margin-bottom:12px}.multi-group-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:12px}.multi-group-title{font-size:14px;font-weight:900;color:var(--t1);display:flex;align-items:center;gap:8px}.multi-protos{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}.multi-protos span{font-size:10px;padding:4px 8px;border-radius:7px;background:var(--accent-d);color:var(--t2);font-weight:700}.db-card{background:linear-gradient(145deg,var(--card),var(--bg3));border:1px solid var(--card-b);border-radius:22px;padding:22px;margin-bottom:16px}.db-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media(max-width:1000px){.dash-hero,.dash-chart-grid,.db-grid{grid-template-columns:1fr}.dash-protocols{grid-template-columns:1fr 1fr}}@media(max-width:560px){.dash-side,.dash-protocols{grid-template-columns:1fr}.dash-title{font-size:26px}}
</style>
</head>
<body>
<div class="toast" id="toast"></div>

<div class="modal-bg" id="modal-create-link">
  <div class="modal-v2 cm-modal">
    <button class="cm-close" onclick="closeModal('modal-create-link')"><i class="ti ti-x"></i></button>
    <div class="cm-head">
      <div class="cm-head-row">
        <div class="cm-head-icon" id="cm-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
        <div>
          <div class="cm-head-title" id="cm-head-title">ساخت کانفیگ جدید</div>
          <div class="cm-head-sub" id="cm-head-sub">تنظیمات کامل پروتکل، ترابرد و محدودیت‌ها در یک صفحه</div>
        </div>
      </div>
    </div>

    <div class="cm-body">

      <!-- اطلاعات پایه -->
      <div class="cm-section">
        <div class="cm-section-label"><i class="ti ti-id-badge-2"></i> اطلاعات پایه</div>
        <div class="cm-field"><label>نام کانفیگ</label>
          <input class="cm-input" id="nl-label" placeholder="مثلاً: PlanAsli">
        </div>
        <div class="cm-field"><label>Path اختصاصی</label>
          <input class="cm-input" id="nl-path" dir="ltr" placeholder="PlanAsli">
          <div class="cm-note" style="margin-top:8px"><i class="ti ti-info-circle"></i> اگر بنویسید PlanAsli، مسیر WebSocket به شکل /ws/PlanAsli ساخته می‌شود.</div>
        </div>
        <div class="cm-row2">
          <div class="cm-field"><label>گروه ساب</label>
            <select class="cm-input" id="nl-sub"><option value="">— بدون گروه —</option></select>
          </div>
          <div class="cm-field"><label>یادداشت (اختیاری)</label>
            <input class="cm-input" id="nl-note" placeholder="توضیح کوتاه">
          </div>
        </div>
      </div>

      <!-- پروتکل و ترابرد: کشویی -->
      <div class="cm-section">
        <div class="cm-section-label"><i class="ti ti-plug-connected"></i> پروتکل و ترابرد</div>

        <div class="cm-dd open" id="dd-base">
          <div class="cm-dd-trigger" onclick="cmToggleDD('dd-base')">
            <div class="cm-dd-icon" id="dd-base-icon"><i class="ti ti-bolt"></i></div>
            <div class="cm-dd-text">
              <div class="cm-dd-title">پروتکل پایه — <span id="dd-base-current">VLESS</span></div>
              <div class="cm-dd-desc" id="dd-base-current-desc">سبک، سریع و پرکاربردترین گزینه</div>
            </div>
            <i class="ti ti-chevron-down cm-dd-chev"></i>
          </div>
          <div class="cm-dd-panel"><div class="cm-dd-panel-inner"><div class="cm-dd-list">
            <div class="cm-opt sel" data-base="vless" onclick="cmSelectBase('vless',this)">
              <div class="cm-opt-radio"></div>
              <div class="cm-opt-icon"><i class="ti ti-bolt"></i></div>
              <div class="cm-opt-text"><div class="cm-opt-title">VLESS</div><div class="cm-opt-desc">سبک، سریع و پرکاربردترین گزینه</div></div>
              <span class="cm-opt-tag">پیشنهادی</span>
            </div>
            <div class="cm-opt" data-base="trojan" onclick="cmSelectBase('trojan',this)">
              <div class="cm-opt-radio"></div>
              <div class="cm-opt-icon"><i class="ti ti-shield-lock"></i></div>
              <div class="cm-opt-text"><div class="cm-opt-title">Trojan</div><div class="cm-opt-desc">شبیه‌سازی ترافیک HTTPS معمولی</div></div>
            </div>
            <div class="cm-opt" data-base="multi" onclick="cmSelectBase('multi',this)">
              <div class="cm-opt-radio"></div>
              <div class="cm-opt-icon"><i class="ti ti-layers-intersect"></i></div>
              <div class="cm-opt-text"><div class="cm-opt-title">Multi Protocol</div><div class="cm-opt-desc">ساخت یک ساب شامل همه پروتکل‌ها، بدون پروکسی تلگرام</div></div>
              <span class="cm-opt-tag">همه در یک ساب</span>
            </div>
            <div class="cm-opt" data-base="shadowsocks" onclick="cmSelectBase('shadowsocks',this)">
              <div class="cm-opt-radio"></div>
              <div class="cm-opt-icon"><i class="ti ti-lock-bolt"></i></div>
              <div class="cm-opt-text"><div class="cm-opt-title">Shadowsocks TLS</div><div class="cm-opt-desc">شادوساکس روی TLS/WebSocket با مسیر اختصاصی</div></div>
              <span class="cm-opt-tag">TLS</span>
            </div>
            <div class="cm-opt" data-base="telproxy" onclick="cmSelectBase('telproxy',this)">
              <div class="cm-opt-radio"></div>
              <div class="cm-opt-icon"><i class="ti ti-brand-telegram"></i></div>
              <div class="cm-opt-text"><div class="cm-opt-title">Telegram Proxy</div><div class="cm-opt-desc">پروکسی MTProto مستقیم روی یک پورت TCP اختصاصی</div></div>
              <span class="cm-opt-tag" style="background:var(--purple-bg);color:var(--purple-t)">MTProto</span>
            </div>
          </div></div></div>
        </div>

        <div style="height:10px"></div>

        <div id="transport-section">
          <div style="height:10px"></div>
        
          <div class="cm-dd" id="dd-transport">
            <div class="cm-dd-trigger" onclick="cmToggleDD('dd-transport')">
              <div class="cm-dd-icon" id="dd-transport-icon"><i class="ti ti-link"></i></div>
              <div class="cm-dd-text">
                <div class="cm-dd-title">نوع ترابرد — <span id="dd-transport-current">WebSocket</span></div>
                <div class="cm-dd-desc" id="dd-transport-current-desc">پایدار و سازگار با همه شرایط شبکه</div>
              </div>
              <i class="ti ti-chevron-down cm-dd-chev"></i>
            </div>
            <div class="cm-dd-panel"><div class="cm-dd-panel-inner"><div class="cm-dd-list">
              <div class="cm-opt sel" data-t="ws" onclick="cmSelectTransport('ws',this)">
                <div class="cm-opt-radio"></div>
                <div class="cm-opt-icon"><i class="ti ti-link"></i></div>
                <div class="cm-opt-text"><div class="cm-opt-title">WebSocket</div><div class="cm-opt-desc">پایدار و سازگار با همه شرایط شبکه</div></div>
              </div>
              <div class="cm-opt" data-t="xhttp-packet-up" onclick="cmSelectTransport('xhttp-packet-up',this)">
                <div class="cm-opt-radio"></div>
                <div class="cm-opt-icon"><i class="ti ti-package"></i></div>
                <div class="cm-opt-text"><div class="cm-opt-title">XHTTP · packet-up</div><div class="cm-opt-desc">سازگاری بالا با CDN و پروکسی‌ها</div></div>
              </div>
              <div class="cm-opt" data-t="xhttp-stream-up" onclick="cmSelectTransport('xhttp-stream-up',this)">
                <div class="cm-opt-radio"></div>
                <div class="cm-opt-icon"><i class="ti ti-rocket"></i></div>
                <div class="cm-opt-text"><div class="cm-opt-title">XHTTP · stream-up</div><div class="cm-opt-desc">تاخیر پایین‌تر برای اتصال‌های پرسرعت</div></div>
              </div>
            </div></div></div>
          </div>
        </div>

        <input type="hidden" id="nl-proto" value="vless-ws">

        <div class="cm-note" style="margin-top:12px" id="transport-note"><i class="ti ti-info-circle"></i> پروتکل و ترابرد پس از ساخت کانفیگ قابل تغییر نیستند.</div>
        <div class="cm-note" style="margin-top:12px;display:none" id="mtproto-note"><i class="ti ti-brand-telegram"></i> برای Telegram Proxy یک پورت TCP اختصاصی به‌صورت خودکار اختصاص داده می‌شود؛ ترابرد WebSocket/XHTTP در این حالت کاربردی ندارد.</div>

        <div class="cm-section" id="mtproto-port-field" style="display:none;margin-bottom:0">
        <div id="auto-domain-box" style="margin-top:10px">
          <div class="cm-note" style="display:flex;justify-content:space-between;align-items:center;gap:10px" id="auto-domain-note">
            <span id="auto-domain-status"><i class="ti ti-route"></i> برای دریافت خودکار دامنه‌ی TCP Proxy از دکمه‌ی کنار استفاده کن.</span>
            <button type="button" class="btn btn-g btn-sm" id="auto-domain-btn" onclick="autoGetMtprotoDomain()"><i class="ti ti-bolt"></i> دریافت دامنه</button>
          </div>
          <div id="auto-domain-token-wrap" style="display:none;margin-top:9px">
            <div class="cm-row2">
              <input class="cm-input" id="auto-domain-token" type="password" placeholder="Railway API Token">
              <button type="button" class="btn btn-p btn-sm" onclick="submitAutoDomainToken()"><i class="ti ti-check"></i> تایید و دریافت</button>
            </div>
          </div>
        </div>
          <div class="cm-row2">
            <div class="cm-field">
              <label><i class="ti ti-route" style="color:var(--accent);margin-left:4px"></i>پورت TCP</label>
              <input class="cm-input" id="nl-mtproto-port" type="number" min="1" max="65535" placeholder="خالی = خودکار">
            </div>
            <div class="cm-field">
              <label><i class="ti ti-server-2" style="color:var(--accent);margin-left:4px"></i>Fake TLS SNI</label>
              <input class="cm-input" id="nl-mtproto-domain" type="text" placeholder="www.cloudflare.com" oninput="cmClearSniPills()">
            </div>
          </div>
          <div class="cm-pills" style="margin-top:-4px;margin-bottom:10px">
            <span class="cm-pill active" onclick="cmSetSni('www.cloudflare.com',this)"><i class="ti ti-brand-cloudflare" style="margin-left:3px"></i>www.cloudflare.com</span>
            <span class="cm-pill" onclick="cmSetSni('www.google.com',this)">www.google.com</span>
            <span class="cm-pill" onclick="cmSetSni('www.microsoft.com',this)">www.microsoft.com</span>
            <span class="cm-pill" onclick="cmSetSni('www.amazon.com',this)">www.amazon.com</span>
          </div>
          <div class="cm-note" style="margin-top:0">
            <i class="ti ti-info-circle"></i>
            پورت خالی = یک پورت آزاد از بازه‌ی ۸۵۰۰–۸۶۰۰ خودکار انتخاب می‌شود. Fake SNI دامنه‌ای است که ترافیک پروکسی پشت آن پنهان می‌شود؛ می‌تونی خودت هر دامنه‌ای بذاری، پیش‌فرض پیشنهادی <b>www.cloudflare.com</b> است.
          </div>
        </div>
        
        <input type="hidden" id="nl-proto" value="vless-ws">
        <div class="cm-note" style="margin-top:12px"><i class="ti ti-info-circle"></i> پروتکل و ترابرد پس از ساخت کانفیگ قابل تغییر نیستند.</div>
      </div>

      <!-- محدودیت‌ها -->
      <div class="cm-section">
        <div class="cm-section-label"><i class="ti ti-adjustments"></i> محدودیت‌ها</div>
        <div class="cm-field">
          <label>سهمیه ترافیک</label>
          <div class="cm-row2">
            <input class="cm-input" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود">
            <select class="cm-input" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
          </div>
          <div class="cm-pills">
            <span class="cm-pill" onclick="cmQuota(0,'GB',this)">نامحدود</span>
            <span class="cm-pill" onclick="cmQuota(500,'MB',this)">۵۰۰MB</span>
            <span class="cm-pill active" onclick="cmQuota(1,'GB',this)">۱GB</span>
            <span class="cm-pill" onclick="cmQuota(5,'GB',this)">۵GB</span>
            <span class="cm-pill" onclick="cmQuota(10,'GB',this)">۱۰GB</span>
            <span class="cm-pill" onclick="cmQuota(50,'GB',this)">۵۰GB</span>
          </div>
        </div>
        <div class="cm-field" style="margin-bottom:4px">
          <label>انقضا</label>
          <input class="cm-input" id="nl-exp" type="number" min="0" step="1" placeholder="روز · 0 = نامحدود">
          <div class="cm-pills">
            <span class="cm-pill" onclick="cmExpiry(0,this)">نامحدود</span>
            <span class="cm-pill" onclick="cmExpiry(7,this)">۷ روز</span>
            <span class="cm-pill active" onclick="cmExpiry(30,this)">۳۰ روز</span>
            <span class="cm-pill" onclick="cmExpiry(90,this)">۹۰ روز</span>
          </div>
        </div>
      </div>

    </div>

    <div class="cm-footer">
      <button class="cm-btn-cancel" onclick="closeModal('modal-create-link')">انصراف</button>
      <button class="cm-btn-submit" id="cm-submit-btn" onclick="createLink()"><i class="ti ti-link-plus" id="cm-submit-icon"></i> <span id="cm-submit-text">ساخت کانفیگ</span></button>    </div>
  </div>
</div>


<div class="modal-bg" id="modal-bot-tcp-proxy">
  <div class="modal-v2 cm-modal" style="max-width:760px">
    <button class="cm-close" onclick="closeModal('modal-bot-tcp-proxy')"><i class="ti ti-x"></i></button>
    <div class="cm-head">
      <div class="cm-head-row">
        <div class="cm-head-icon"><i class="ti ti-server-2"></i></div>
        <div>
          <div class="cm-head-title">ساخت TCP Proxy عمومی</div>
          <div class="cm-head-sub">برای پروکسی تلگرام/MTProto یک دامنه و پورت عمومی از Railway دریافت می‌کند</div>
        </div>
      </div>
    </div>
    <div class="cm-body">
      <div class="cl" style="margin-top:0;margin-bottom:14px">
        <i class="ti ti-info-circle"></i>
        <span>اگر قبلاً توکن Railway ذخیره شده باشد، نیازی به وارد کردن دوباره نیست. در غیر این صورت توکن را وارد کن و فرآیند را شروع کن.</span>
      </div>
      <div class="cm-section" id="btp-token-section">
        <div class="cm-section-label"><i class="ti ti-key"></i> توکن Railway</div>
        <input class="cm-input" id="btp-token" type="password" placeholder="Railway API Token" dir="ltr">
      </div>
      <div class="cm-section" id="btp-token-saved-section" style="display:none">
        <div class="cl" style="margin-top:0;background:var(--green-bg);color:var(--green-t)">
          <i class="ti ti-circle-check"></i>
          <span>توکن Railway قبلاً ذخیره شده است. برای تغییر توکن روی دکمه زیر بزن.</span>
        </div>
        <button type="button" class="btn btn-o btn-sm" onclick="btpChangeToken()"><i class="ti ti-key"></i> تغییر توکن</button>
      </div>
      <div class="cm-section">
        <div class="cm-section-label"><i class="ti ti-route"></i> تنظیمات ساخت</div>
        <div class="cm-row2">
          <div class="cm-field">
            <label>پورت داخلی MTProto</label>
            <input class="cm-input" id="btp-port" type="number" min="1" max="65535" placeholder="خالی = خودکار/پیش‌فرض">
          </div>
          <div class="cm-field">
            <label>حالت جستجو</label>
            <div class="cm-note" style="margin-top:0"><i class="ti ti-route"></i> حالت پیش‌فرض اسکن خودکار است. در صورت نیاز یکی از دامنه‌های پیشنهادی را انتخاب کن.</div>
          </div>
        </div>
        <div class="cm-pills" style="margin-top:10px">
          <span class="cm-pill active" id="btp-isp-auto" onclick="btpSelectIsp(null,'btp-isp-auto')">اسکن خودکار</span>
          <span class="cm-pill" id="btp-isp-cloudflare" onclick="btpSelectIsp('cloudflare.com','btp-isp-cloudflare')">Cloudflare</span>
          <span class="cm-pill" id="btp-isp-google" onclick="btpSelectIsp('google.com','btp-isp-google')">Google</span>
          <span class="cm-pill" id="btp-isp-microsoft" onclick="btpSelectIsp('microsoft.com','btp-isp-microsoft')">Microsoft</span>
        </div>
      </div>
      <div class="cm-section">
        <div class="cm-section-label"><i class="ti ti-activity"></i> وضعیت</div>
        <div class="cl" style="margin-top:0">
          <i class="ti ti-player-play" id="btp-status-icon"></i>
          <span id="btp-status-text">آماده شروع</span>
        </div>
        <div id="btp-log-box" style="display:none;background:rgba(0,0,0,.12);border:1px solid var(--card-b);border-radius:12px;padding:12px;max-height:220px;overflow:auto;font-family:ui-monospace,monospace;font-size:11px;line-height:1.8;margin-top:12px"></div>
      </div>
    </div>
    <div class="cm-footer">
      <button class="cm-btn-cancel" onclick="closeModal('modal-bot-tcp-proxy')">بستن</button>
      <button class="btn btn-d" id="btp-stop-btn" onclick="stopBotTcpProxy()" style="display:none"><i class="ti ti-player-stop"></i> توقف</button>
      <button class="cm-btn-submit" id="btp-start-btn" onclick="startBotTcpProxy()"><i class="ti ti-player-play"></i> شروع ساخت TCP Proxy</button>
    </div>
  </div>
</div>

<!-- مودال بروزرسانی -->
<div class="modal-bg" id="modal-update" style="z-index:9999">
  <div class="modal-v2" style="max-width:460px">
    <div class="modal-v2-head" style="background:linear-gradient(155deg,rgba(59,130,246,.16) 0%,transparent 65%)">
      <button class="modal-v2-close" onclick="closeModal('modal-update')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon" style="background:linear-gradient(135deg,var(--accent),var(--accent2))"><i class="ti ti-cloud-download"></i></div>
      <div class="modal-v2-title">بروزرسانی جدید موجود است</div>
      <div class="modal-v2-sub">نسخه‌ی جدید <span id="update-modal-version">—</span> آماده نصب است</div>
    </div>
    <div class="modal-v2-body">
      <div class="cl" style="margin-top:0">
        <i class="ti ti-info-circle"></i>
        <span id="update-modal-desc">توضیحات بروزرسانی...</span>
      </div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="dismissUpdate()" style="flex:.6">انصراف</button>
        <button class="btn btn-p" onclick="startUpdateFromModal()" style="flex:1;justify-content:center"><i class="ti ti-download"></i> نصب بروزرسانی</button>
      </div>
    </div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <div class="brand-mark small">OX</div>
    <span class="mob-title">OXNET</span>
  </div>
  <div class="mob-right">
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="brand-mark small">OX</div>
    <div><div class="logo-name">oxnet</div><div class="logo-sub">OXNET · v1.2.1</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">پنل</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> گروه‌های ساب <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> سابسکریپشن</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-sec">سیستم</div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> خطاها</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> تست WebSocket</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
  </div>
  <div class="sb-foot">
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">تم روشن</span></button>
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>
<main class="main">
<div class="ann-banner-wrap" id="ann-banner-wrap"></div>
<section class="pg on" id="pg-overview">
  <div class="dash-hero">
    <div class="dash-main-card">
      <div class="dash-eyebrow">OXNET Control Panel</div>
      <div class="dash-title">مدیریت سریع، تمیز و <span>چند پروتکل</span></div>
      <div class="dash-desc">نمای زنده از مصرف، اتصالات، کانفیگ‌ها و سلامت سرویس. از همین صفحه می‌تونی لینک پیش‌فرض رو برداری یا وارد ساخت کانفیگ جدید بشی.</div>
      <div class="dash-actions">
        <button class="btn btn-p" onclick="openModal('modal-create-link')"><i class="ti ti-square-rounded-plus"></i> ساخت کانفیگ</button>
        <button class="btn btn-g" onclick="navTo('traffic')"><i class="ti ti-chart-area"></i> مشاهده ترافیک</button>
        <button class="btn btn-o" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
      </div>
    </div>
    <div class="dash-side">
      <div class="dash-kpi"><div class="dash-kpi-icon"><i class="ti ti-plug-connected"></i></div><div class="dash-kpi-label">اتصالات</div><div class="dash-kpi-val" id="m-conns">—</div><div class="dash-kpi-sub">زنده</div></div>
      <div class="dash-kpi"><div class="dash-kpi-icon"><i class="ti ti-transfer"></i></div><div class="dash-kpi-label">ترافیک</div><div class="dash-kpi-val" id="m-traffic">—</div><div class="dash-kpi-sub">از شروع</div></div>
      <div class="dash-kpi"><div class="dash-kpi-icon"><i class="ti ti-link"></i></div><div class="dash-kpi-label">فعال</div><div class="dash-kpi-val" id="m-alinks">—</div><div class="dash-kpi-sub" id="m-lsub">کانفیگ</div></div>
      <div class="dash-kpi"><div class="dash-kpi-icon"><i class="ti ti-folders"></i></div><div class="dash-kpi-label">ساب‌ها</div><div class="dash-kpi-val" id="m-subs">—</div><div class="dash-kpi-sub">گروه</div></div>
    </div>
  </div>

  <div class="dash-protocols">
    <div class="dash-protocol"><i class="ti ti-bolt"></i><div><b>VLESS WS</b><span>پایدار و سریع</span></div></div>
    <div class="dash-protocol"><i class="ti ti-shield-lock"></i><div><b>Trojan WS</b><span>TLS-ready</span></div></div>
    <div class="dash-protocol"><i class="ti ti-lock-bolt"></i><div><b>Shadowsocks TLS</b><span>مسیر اختصاصی</span></div></div>
    <div class="dash-protocol"><i class="ti ti-package"></i><div><b>XHTTP Fixed</b><span>packet / stream / one</span></div></div>
  </div>

  <div class="vless-box">
    <div class="vl-header">
      <div class="vl-title"><i class="ti ti-link"></i> لینک فعال پیشنهادی</div>
      <span class="badge bg-blue"><span class="dot db"></span> TLS 443</span>
    </div>
    <div class="vl-code" id="vless-main">در حال دریافت...</div>
    <div class="vl-actions">
      <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> کپی</button>
      <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-list"></i> کانفیگ‌ها</button>
    </div>
  </div>

  <div class="dash-chart-grid">
    <div class="dash-chart-card"><div class="dash-card-head"><div><div class="dash-card-title"><i class="ti ti-chart-area"></i> روند ترافیک ساعتی</div><div class="dash-card-sub">مصرف بر اساس MB در ساعت</div></div><span class="badge bg-blue" id="uptime-badge">—</span></div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="dash-chart-card"><div class="dash-card-head"><div><div class="dash-card-title"><i class="ti ti-chart-donut"></i> ترکیب پروتکل‌ها</div><div class="dash-card-sub">نمای تقریبی کانفیگ‌های فعال</div></div></div><div class="ch-sm"><canvas id="ch2"></canvas></div></div>
  </div>

  <div class="g2">
    <div class="card"><div class="card-title"><i class="ti ti-activity"></i> سلامت سرویس</div><div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> Path Auth</span><span class="sr-v" style="color:var(--green-t)">فعال</span></div><div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptime-inline">—</span></div><div class="sr" style="flex-direction:column;align-items:flex-start;gap:4px"><div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> بار نسبی</span><span class="sr-v" id="bw-pct">—%</span></div><div class="spbar" style="width:100%"><div class="spfill" id="bw-bar" style="width:0%"></div></div></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="ml-auto badge bg-blue" id="lsummary-badge">۰</span></div><div id="lsummary">—</div></div>
  </div>
</section>
<section class="pg" id="pg-links">
  <div class="topbar">
    <div style="display:flex;justify-content:flex-end;gap:8px;margin-bottom:16px">
      <button class="btn btn-p" onclick="openModal('modal-create-link')">
        <i class="ti ti-square-rounded-plus"></i> ساخت کانفیگ جدید
      </button>
      <button class="btn btn-g" style="margin-right:14px" onclick="openModal('modal-bot-tcp-proxy');btpCheckTokenState()">
        <i class="ti ti-server-2"></i> ساخت TCP Proxy
      </button>
    </div>
    <div class="tb-right">
      <span class="badge bg-blue" id="links-pg-cnt">۰ کانفیگ</span>
    </div>
  </div>

  <div class="info-strip">
    <div class="info-item">
      <span class="info-item-label">ارسال / دریافت لحظه‌ای</span>
      <span class="info-item-val"><i class="ti ti-arrows-exchange"></i> <span id="info-sent-recv">0 B / 0 B</span></span>
    </div>
    <div class="info-item">
      <span class="info-item-label">مصرف دوره فعلی</span>
      <span class="info-item-val"><i class="ti ti-chart-pie"></i> <span id="info-usage">0 B</span></span>
    </div>
    <div class="info-item">
      <span class="info-item-label">مصرف کل از ابتدا</span>
      <span class="info-item-val"><i class="ti ti-history"></i> <span id="info-alltime">0 B</span></span>
    </div>
    <div class="info-item">
      <span class="info-item-label">تعداد این‌باندها</span>
      <span class="info-item-val"><i class="ti ti-list-details"></i> <span id="info-inbounds">0</span></span>
    </div>
    <div class="info-item">
      <span class="info-item-label">کلاینت‌ها</span>
      <span class="info-item-val"><i class="ti ti-users"></i> <span class="info-badge" id="info-clients">0</span></span>
    </div>
  </div>

  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-folders"></i> گروه‌های ساب</div><div class="tb-sub">هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">۰ گروه</span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> گروه جدید</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="جستجو در گروه‌ها..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>
  </div>
</section>
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> سابسکریپشن</div><div class="tb-sub">لینک‌های اشتراک برای اپ‌های v2ray</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-rss"></i> سابسکریپشن تکی (هر کانفیگ)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:12px">هر کانفیگ URL سابسکریپشن مخصوص دارد. از کارت کانفیگ روی آیکون <i class="ti ti-rss"></i> کلیک کنید.</p>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-database"></i> سابسکریپشن کامل (ادمین)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:4px">شامل تمام کانفیگ‌های فعال.</p>
      <div class="sub-box"><span class="sub-url" id="sub-all-url">در حال دریافت...</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
      <div class="cl amber" style="margin-top:11px"><i class="ti ti-alert-triangle"></i><span>این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).</span></div>
    </div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-folders"></i> لینک سابسکریپشن گروه‌ها</div>
    <div id="sub-groups-list">در حال بارگذاری...</div>
  </div>
</section>
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل و مانیتورینگ مصرف پهنای باند</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>

  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> کل ترافیک مصرفی</div>
      <div class="traf-main-val" id="t-traffic">—<span>MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">میانگین ساعتی</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">پیک مصرف</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">بالاترین ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">کمترین مصرف</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
  </div>

  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک</div>
        <div class="traf-chart-sub">بر اساس مگابایت در هر ساعت</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> مصرف</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> میانگین</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>

  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="conn-hero-label">اتصالات زنده</div>
      <div class="conn-hero-val" id="ch-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-transfer"></i></div>
      <div class="conn-hero-label">مجموع ترافیک لحظه‌ای</div>
      <div class="conn-hero-val" id="ch-traffic">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-clock"></i></div>
      <div class="conn-hero-label">میانگین مدت اتصال</div>
      <div class="conn-hero-val" id="ch-avgdur">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div>
      <div class="conn-hero-label">آی‌پی‌های یکتا</div>
      <div class="conn-hero-val" id="ch-uniq">—</div>
    </div>
  </div>

  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> لیست اتصالات</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> بروزرسانی خودکار هر ۵ ثانیه</div>
  </div>

  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">هیچ اتصال فعالی نیست</div>
    <div class="conn-empty-v2-sub">به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند</div>
  </div>
</section>
<section class="pg" id="pg-security">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> امنیت</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-lock"></i> رمزنگاری</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● فعال (443)</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> پروتکل‌ها</span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> هش رمز</span><span class="sr-v">SHA-256+Salt</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> سشن</span><span class="sr-v">HttpOnly · 7 روز</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-shield-check"></i> کنترل دسترسی</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> Path Auth اختصاصی</span><span class="sr-v" style="color:var(--green-t)">● فعال v1</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> فعال/غیرفعال کانفیگ</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> سهمیه ترافیک</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> تاریخ انقضا</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> رمز صفحه پابلیک ساب</span><span class="sr-v" style="color:var(--green-t)">● اختیاری · SHA-256</span></div>
    </div>
  </div>
</section>
<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div><div class="tb-sub">تاریخچه‌ی کامل رخدادهای پنل</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div></div>
</section>
<section class="pg" id="pg-errors">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> خطاها</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> لاگ خطاها</div><div id="errs-full">—</div></div>
</section>
<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> تست WebSocket</div></div></div>
  <div class="card" style="max-width:660px">
    <div class="cl amber" style="margin-top:0;margin-bottom:12px"><i class="ti ti-alert-triangle"></i><span>فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).</span></div>
    <div class="form-row" style="margin-bottom:12px">
      <div class="fg" style="flex:1"><label>UUID (باید در کانفیگ‌ها وجود داشته باشد)</label><input class="fi" id="ws-uuid" placeholder="UUID یک کانفیگ فعال" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> اتصال</button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> قطع</button>
    </div>
    <div class="form-row" style="margin-bottom:12px">
      <input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> ارسال</button>
    </div>
    <div style="background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:10px;padding:14px;height:250px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log">
      <p style="color:var(--t3)">منتظر اتصال...</p>
    </div>
  </div>
</section>
<section class="pg" id="pg-updates">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-cloud-download"></i> نسخه و بروزرسانی</div><div class="tb-sub">مدیریت نسخه‌ی پنل و تاریخچه‌ی کامل بروزرسانی‌ها</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadVersion()"><i class="ti ti-refresh"></i> بررسی مجدد</button></div>
  </div>

  <div class="upd-hero" id="upd-hero">
    <div class="upd-hero-glow"></div>
    <div class="upd-hero-top">
      <div class="upd-hero-cur">
        <div class="upd-hero-icon"><i class="ti ti-package"></i></div>
        <div>
          <div class="upd-hero-label">نسخه‌ی نصب‌شده</div>
          <div class="upd-hero-ver" id="ver-current">—</div>
        </div>
      </div>
      <div class="upd-hero-status" id="ver-status-badge">
        <span class="upd-pill upd-pill-blue"><span class="upd-dot"></span> در حال بررسی...</span>
      </div>
    </div>
    <div class="upd-hero-desc" id="ver-current-desc">—</div>
    <div class="upd-hero-meta">
      <span class="upd-meta-chip"><i class="ti ti-brand-github"></i> <span id="ver-repo">—</span></span>
      <span class="upd-meta-chip"><i class="ti ti-git-branch"></i> <span id="ver-branch">—</span></span>
    </div>
  </div>

  <div class="upd-latest-card" id="upd-latest-card" style="display:none">
    <div class="upd-latest-left">
      <div class="upd-latest-icon"><i class="ti ti-sparkles"></i></div>
      <div>
        <div class="upd-latest-title">نسخه‌ی جدید موجود است</div>
        <div class="upd-latest-ver">نسخه‌ی <span id="ver-latest-num">—</span></div>
        <div class="upd-latest-desc" id="ver-latest-desc">—</div>
      </div>
    </div>
    <button class="upd-install-btn" id="update-btn" onclick="startUpdate()">
      <i class="ti ti-download"></i> نصب بروزرسانی
    </button>
  </div>

  <div class="upd-progress-card" id="update-progress-wrap" style="display:none">
    <div class="upd-progress-head">
      <div class="upd-progress-icon"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i></div>
      <div style="flex:1">
        <div class="upd-progress-title">در حال نصب بروزرسانی...</div>
        <div class="upd-progress-txt" id="update-progress-txt">در حال آماده‌سازی...</div>
      </div>
      <div class="upd-progress-pct" id="update-progress-pct">0%</div>
    </div>
    <div class="upd-progress-track"><div class="upd-progress-fill" id="update-progress-bar" style="width:0%"></div></div>
  </div>

  <div class="upd-log-card">
    <div class="upd-log-head">
      <div class="upd-log-title"><i class="ti ti-terminal-2"></i> لاگ زنده‌ی نصب</div>
      <button class="btn btn-o btn-sm" onclick="loadUpdateLog()"><i class="ti ti-refresh"></i> بروزرسانی لاگ</button>
    </div>
    <div class="upd-log-box" id="update-log-box">
      <p class="upd-log-empty">لاگی موجود نیست</p>
    </div>
  </div>

  <div class="upd-history-head">
    <div class="upd-history-title"><i class="ti ti-history"></i> تاریخچه‌ی بروزرسانی‌ها</div>
    <span class="badge bg-blue" id="upd-history-count">۰ مورد</span>
  </div>
  <div class="upd-timeline" id="upd-history-list">
    <div class="upd-history-empty"><i class="ti ti-history-toggle"></i><p>هنوز هیچ بروزرسانی‌ای ثبت نشده</p></div>
  </div>
</section>
<section class="pg" id="pg-support">
  <div class="sup-wrap">
    <div class="sup-head">
      <div class="sup-head-icon"><i class="ti ti-headset"></i></div>
      <div class="sup-head-text">
        <div class="sup-head-title">بخش حذف‌شده</div>
        <div class="sup-head-sub"><span class="sdot"></span> معمولاً در کمتر از چند ساعت پاسخ داده می‌شود</div>
      </div>
    </div>
    <div id="sup-blocked-banner" class="sup-blocked-banner" style="display:none">
      <i class="ti ti-lock"></i> این بخش در نسخه مستقل حذف شده است.
    </div>
    <div id="support-msgs"></div>
    <div class="sup-input-row" id="sup-input-row">
      <input class="fi" id="support-inp" placeholder="پیام خود را بنویسید..." style="flex:1" onkeydown="if(event.key==='Enter')sendSupportMsg()">
      <button class="btn btn-p" onclick="sendSupportMsg()"><i class="ti ti-send-2"></i></button>
    </div>
  </div>
</section>
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div></div></div>
  <div class="db-card">
    <div class="card-title"><i class="ti ti-database"></i> دیتابیس خارجی PostgreSQL <span class="ml-auto badge bg-blue" id="db-status-badge">در حال بررسی</span></div>
    <div class="cl" style="margin-top:0;margin-bottom:12px"><i class="ti ti-info-circle"></i><span>Internal URL را وقتی اپ و دیتابیس داخل یک شبکه هستند وارد کن. اگر از بیرون وصل می‌شی External URL را بزن. بعد از اتصال، OXNET جدول خودش را می‌سازد و اطلاعات پنل را در PostgreSQL ذخیره می‌کند.</span></div>
    <div class="db-grid">
      <div class="fg"><label>Internal URL</label><input class="fi" id="db-internal-url" dir="ltr" placeholder="postgresql://user:pass@host:5432/db" style="width:100%"></div>
      <div class="fg"><label>External URL</label><input class="fi" id="db-external-url" dir="ltr" placeholder="postgresql://user:pass@host/db" style="width:100%"></div>
      <div class="fg" style="grid-column:1/-1"><label>URL فعال / وضعیت</label><input class="fi" id="db-current-url" dir="ltr" readonly placeholder="هنوز متصل نیست" style="width:100%"></div>
    </div>
    <div class="vl-actions" style="margin-top:14px">
      <button class="btn btn-p" onclick="connectDatabase('internal')"><i class="ti ti-plug-connected"></i> اتصال با Internal</button>
      <button class="btn btn-g" onclick="connectDatabase('external')"><i class="ti ti-world"></i> اتصال با External</button>
      <button class="btn btn-d" onclick="disconnectDatabase()"><i class="ti ti-plug-x"></i> قطع اتصال</button>
    </div>
  </div>
  <div class="g2">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> آنلاین · Railway</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پورت</div><div class="srv-tile-val">443 (TLS)</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">نسخه</div><div class="srv-tile-val">v1.2.1</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label">فریم‌ورک</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پلتفرم</div><div class="srv-tile-val">Railway</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">ذخیره‌سازی</div><div class="srv-tile-val"><span id="storage-mode-label">JSON File / PostgreSQL</span></div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">تغییر رمز عبور</div>
          <div class="pw-hero-sub">رمز قوی انتخاب کنید و آن را جایی امن نگه دارید</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field">
          <label>رمز فعلی</label>
          <input class="pw-input" type="password" id="cp-cur" placeholder="رمز فعلی را وارد کنید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field" style="margin-bottom:6px">
          <label>رمز جدید</label>
          <input class="pw-input" type="password" id="cp-new" placeholder="حداقل ۴ کاراکتر" oninput="checkPwStrength(this.value)">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-strength" id="pw-strength-bar">
          <div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div>
        </div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> قدرت رمز</div>
        <div class="pw-reqs">
          <span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> حداقل ۴ کاراکتر</span>
          <span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> شامل عدد</span>
          <span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> حروف بزرگ/کوچک</span>
        </div>
        <div class="pw-field" style="margin-bottom:18px">
          <label>تکرار رمز جدید</label>
          <input class="pw-input" type="password" id="cp-cf" placeholder="تکرار رمز جدید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
        </div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> ذخیره رمز جدید</button>
      </div>
    </div>
  </div>
</section>
</main>
<script>
let isDark=localStorage.getItem('oxnet-theme')==='dark';
let updateAvailable = false;
let updateVersion = '';
let updateDescription = '';

function dismissUpdate() {
  sessionStorage.setItem('oxnet-update-dismissed', 'true');
  closeModal('modal-update');
}

function startUpdateFromModal() {
  closeModal('modal-update');
  startUpdate(); // تابع موجود
}
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  const icon=dark?'ti-sun':'ti-moon',label=dark?'تم روشن':'تم تاریک';
  document.getElementById('theme-icon').className='ti '+icon;
  document.getElementById('theme-label').textContent=label;
  const mobI=document.getElementById('theme-mob-icon');if(mobI)mobI.className='ti '+icon;
}

function toggleTheme(){isDark=!isDark;localStorage.setItem('oxnet-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
function toast(msg,type=''){
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
  const d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(d<=3)return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${toFa(d)} روز مانده</span>`;
  return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${toFa(d)} روز مانده</span>`;
}
function protoBadge(p){
  const m={
    'vless-ws':['VLESS · WS','pc-ws'],
    'xhttp-packet-up':['VLESS · XHTTP packet-up','pc-xhttp'],
    'xhttp-stream-up':['VLESS · XHTTP stream-up','pc-xhttp'],
    'xhttp-stream-one':['XHTTP Stream','pc-xh'],
    'trojan-ws':['Trojan · WS','pc-trojan'],
    'trojan-xhttp-packet-up':['Trojan · XHTTP packet-up','pc-trojan'],
    'trojan-xhttp-stream-up':['Trojan · XHTTP stream-up','pc-trojan'],
    'shadowsocks-tls':['Shadowsocks · TLS','pc-ss'],
    'mtproto':['Telegram Proxy · MTProto','pc-trojan'],
  };
  const v=m[p]||['ناشناخته','pc-ws'];
  return `<span class="proto-chip ${v[1]}">${v[0]}</span>`;
}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){
  const r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}
function setQuota(val,unit,el){
  document.getElementById('nl-val').value = val===0?'':val;
  document.getElementById('nl-unit').value = unit;
  document.querySelectorAll('#quota-chips .qc-pill').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setExpiry(days,el){
  document.getElementById('nl-exp').value = days===0?'':days;
  document.querySelectorAll('#exp-chips .qc-pill').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function selectProto(val,el){
  document.getElementById('nl-proto').value = val;
  document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){
  document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));
  document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));
  const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity,settings:loadDbStatus};  if(loaders[name])loaders[name]();
  closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}
let prevTraf=0,ch1,ch2,ch3;
async function fetchStats(){
  try{
    const r=await authF('/stats'),d=await r.json();
    document.getElementById('m-conns').textContent=d.active_connections;
    document.getElementById('conns-nb').textContent=d.active_connections;
    document.getElementById('m-traffic').textContent=d.total_traffic_mb.toFixed(1)+' MB';
    document.getElementById('m-alinks').textContent=d.active_links??'—';
    document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';
    document.getElementById('m-subs').textContent=d.subs_count??'—';
    const errsBadge=document.getElementById('errs-badge'); if(errsBadge) errsBadge.textContent=d.total_errors+' خطا';
    document.getElementById('uptime-inline').textContent=d.uptime;
    document.getElementById('uptime-badge').textContent='Railway · '+d.uptime;
    const lastUpd=document.getElementById('last-upd'); if(lastUpd) lastUpd.textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
    const connsLive=document.getElementById('conns-live'); if(connsLive) connsLive.innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' اتصال';
    const tTraffic=document.getElementById('t-traffic'); if(tTraffic) tTraffic.innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    const delta=d.total_traffic_mb-prevTraf,pct=Math.min(100,Math.round((delta/50)*100));
    document.getElementById('bw-pct').textContent=pct+'%';
    document.getElementById('bw-bar').style.width=pct+'%';
    prevTraf=d.total_traffic_mb;
    if(d.hourly){
      const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));
      [ch1,ch3].forEach(c=>{if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});
      if(ch2){const pc=d.protocol_counts||{};ch2.data.labels=['VLESS WS','Trojan WS','XHTTP','Shadowsocks TLS','MTProto'];ch2.data.datasets[0].data=[pc.vless_ws||0,pc.trojan_ws||0,pc.xhttp||0,pc.shadowsocks_tls||0,pc.mtproto||0];ch2.update();}
      if(vals.length){const avg=vals.reduce((a,b)=>a+b,0)/vals.length,peak=Math.max(...vals);const tAvg=document.getElementById('t-avg'),tPeak=document.getElementById('t-peak');if(tAvg)tAvg.innerHTML=avg.toFixed(2)+'<span class="m-unit">MB</span>';if(tPeak)tPeak.innerHTML=peak.toFixed(2)+'<span class="m-unit">MB</span>';}
    }
    renderErrs(d.recent_errors||[]);
  }catch(e){console.error(e)}
}
function renderErrs(errs){
  const el=document.getElementById('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}
  el.innerHTML=errs.slice().reverse().map(e=>`<div class="erow"><div class="etime"><i class="ti ti-clock"></i>${new Date(e.time).toLocaleString('fa-IR')}</div><div class="emsg">${esc(e.error)}${e.url?' — '+esc(e.url):''}</div></div>`).join('');
}
async function loadActivity(){
  try{
    const r=await authF('/api/activity'),d=await r.json();
    const logs=(d.logs||[]).slice().reverse();
    const el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');
    if(!logs.length){el.innerHTML='';em.style.display='block';return}
    em.style.display='none';
    const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
    const kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};
    el.innerHTML=logs.map(l=>`
      <div class="log-item">
        <div class="log-ic ${l.level}"><i class="ti ${icMap[l.level]||'ti-info-circle'}"></i></div>
        <div class="log-body">
          <div class="log-msg">${esc(l.message)}</div>
          <div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString('fa-IR')} <span class="log-kind">${kindFa[l.kind]||l.kind}</span></div>
        </div>
      </div>
    `).join('');
  }catch(e){console.error(e)}
}
let allSubsList=[],allLinksList=[];
async function loadLinks(){
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links:rawLinks=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    const multiSubs=subs.filter(s=>String(s.desc||'').includes('Multi Protocol'));
    // فقط بچه‌های واقعی مولتی را داخل کارت گروهی مخفی/گروه‌بندی کن؛
    // کانفیگ یا پروکسی معمولی که بعداً داخل همان گروه اضافه شده باید جدا نمایش داده شود.
    const childIds=new Set(rawLinks.filter(l=>l.is_multi_child || l.multi_group_id).map(l=>l.uuid));
    const groupCards=multiSubs.map(s=>{
      const kids=rawLinks.filter(l=>l.is_multi_child && (l.multi_group_id===s.sub_id || (s.link_ids||[]).includes(l.uuid)));
      return {uuid:s.sub_id,label:s.name,protocol:'multi',is_multi_group:true,child_count:kids.length,children:kids,active:kids.some(k=>k.active&&!k.expired),expired:false,used_bytes:kids.reduce((a,k)=>a+(k.used_bytes||0),0),limit_bytes:kids.reduce((a,k)=>a+(k.limit_bytes||0),0),created_at:s.created_at,sub_url:s.sub_url,vless_link:s.sub_url,sub_id:s.sub_id};
    });
    const links=[...groupCards,...rawLinks.filter(l=>!childIds.has(l.uuid))];
    allSubsList=subs;allLinksList=links;window.__rawLinksList=rawLinks;
    document.getElementById('info-inbounds').textContent = toFa(links.length);
    document.getElementById('info-clients').textContent = toFa(links.filter(l=>l.active).length);
    document.getElementById('info-alltime').textContent = fmtB(links.reduce((s,l)=>s+l.used_bytes,0));
    const nlSub=document.getElementById('nl-sub');
    nlSub.innerHTML='<option value="">— بدون گروه —</option>'+subs.map(s=>`<option value="${esc(s.sub_id)}">${esc(s.name)}</option>`).join('');
    document.getElementById('links-nb').textContent=links.length;
    document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' کانفیگ';
    document.getElementById('lsummary-badge').textContent=toFa(links.length);
    const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!links.length){grid.innerHTML='';empty.style.display='block';document.getElementById('lsummary').innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی وجود ندارد</p></div>';return}
    empty.style.display='none';
    const subMap=Object.fromEntries(subs.map(s=>[s.sub_id,s.name]));
    grid.innerHTML=links.map(l=>{
  if(l.is_multi_group){return `<div class="multi-group-card"><div class="multi-group-head"><div><div class="multi-group-title"><i class="ti ti-layers-intersect"></i>${esc(l.label)}</div><div class="multi-protos">${(l.children||[]).map(k=>`<span>${esc((PROTO_MAP[k.protocol]||[k.protocol])[0])}</span>`).join('')}</div></div><div style="display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end"><span class="badge bg-blue">${toFa(l.child_count||0)} پروتکل</span><button class="btn btn-sm btn-p" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('ساب مولتی کپی شد','ok'))"><i class="ti ti-copy"></i> ساب</button><button class="btn btn-sm btn-g" onclick="showQR('${esc(l.sub_url)}')"><i class="ti ti-qrcode"></i></button></div></div><div class="utxt"><span>مصرف کل: ${fmtB(l.used_bytes||0)}</span><span>${esc(l.sub_url||'')}</span></div></div>`}
  const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
  const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
  const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
  const allowed=l.active&&!l.expired;
  const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
  const isMt = l.protocol === 'mtproto';
  const adBtn = isMt
    ? `<button class="btn btn-sm btn-pur btn-icon" onclick="openAdTagModal('${l.uuid}','${esc(l.label)}','${esc(l.ad_tag||'')}')" title="تنظیم تبلیغ کانال"><i class="ti ti-speakerphone"></i></button>`
    : '';
  const idChip = isMt
    ? `<span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${esc(l.mtproto_secret||'')}').then(()=>toast('سکرت کپی شد ','ok'))" title="سکرت کامل: ${esc(l.mtproto_secret||'')}"><i class="ti ti-key"></i> ${esc((l.mtproto_secret||'').slice(0,10))}…</span>`
    : `<span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID کپی شد','ok'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>`;
  return `<div class="cfg-card ${cardCls}">
    <div class="cfg-row">
      <span class="cfg-status-dot ${allowed?'pulse':''}"></span>
      <div class="cfg-identity">
        <div class="cfg-label">${esc(l.label)}</div>
        <div class="cfg-sub-meta">
          ${idChip}
          <span>${new Date(l.created_at).toLocaleDateString('fa-IR')}</span>
        </div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-usage-col">
        <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
        <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>از ${lim}</span></div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-exp-col">${expChip(l.expires_at,l.expired)}</div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-badges-col">
        ${protoBadge(l.protocol)}
        ${isMt && l.mtproto_public_host ? `<span class="cfg-sub-tag"><i class="ti ti-route"></i> ${esc(l.mtproto_public_host)}:${l.mtproto_public_port}</span>` : ''}
        ${isMt && !l.mtproto_public_host && l.mtproto_public_pending ? `<span class="cfg-sub-tag" style="color:var(--amber-t)"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ساخت TCP Proxy عمومی...</span>` : ''}
        ${isMt && !l.mtproto_public_host && !l.mtproto_public_pending && !l.mtproto_manual_port ? `<span class="cfg-sub-tag" style="color:var(--red-t)"><i class="ti ti-alert-triangle"></i> بدون TCP Proxy عمومی — لینک کار نمی‌کند</span>` : ''}
        ${l.sub_id&&allSubsList.find(s=>s.sub_id===l.sub_id)?`<span class="cfg-sub-tag"><i class="ti ti-folder"></i> ${esc(allSubsList.find(s=>s.sub_id===l.sub_id).name)}</span>`:''}
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-actions">
        <div class="cfg-actions">
        <button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="فعال/غیرفعال"></button>
        ${adBtn}
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی لینک"><i class="ti ti-copy"></i></button>
        ${isMt
          ? `<button class="btn btn-sm btn-g btn-icon" onclick="openMtInfoModal('${esc(l.label)}','${esc(l.mtproto_secret||'')}','${esc(l.vless_link)}',${!!l.mtproto_public_host})" title="اطلاعات پروکسی"><i class="ti ti-info-circle"></i></button>`
          : `<button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('Sub کپی شد','ok'))" title="Sub URL"><i class="ti ti-rss"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>`
        }
        <button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')" title="ویرایش"><i class="ti ti-edit"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')" title="ریست مصرف"><i class="ti ti-rotate"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="حذف"><i class="ti ti-trash"></i></button>
      </div>
      </div>
    </div>
  </div>`;
}).join('');
    document.getElementById('lsummary').innerHTML=links.slice(0,6).map(l=>`<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti ${l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x'}" style="color:${l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)'}"></i>${esc(l.label)}</span><span class="sr-v" style="font-size:10px">${fmtB(l.used_bytes)} / ${l.limit_bytes===0?'∞':fmtB(l.limit_bytes)}</span></div>`).join('');
  }catch(e){console.error(e)}
}

let protoBase = 'vless', protoTransport = 'ws';

function qcTab(name, el){
  document.querySelectorAll('.qc-tab').forEach(t=>t.classList.remove('active'));
  el.classList.add('active');
  document.querySelectorAll('.qc-pane').forEach(p=>p.classList.remove('active'));
  document.getElementById('qc-pane-'+name).classList.add('active');
}

let cmBase = 'vless', cmTransport = 'ws';

function cmToggleDD(id){
  const el = document.getElementById(id);
  const isOpen = el.classList.contains('open');
  document.querySelectorAll('.cm-dd').forEach(d => d.classList.remove('open'));
  if(!isOpen) el.classList.add('open');
}

const BASE_INFO = {
  vless:    { icon:'ti-bolt',           title:'VLESS',          desc:'سبک، سریع و پرکاربردترین گزینه' },
  trojan:   { icon:'ti-shield-lock',    title:'Trojan',         desc:'شبیه‌سازی ترافیک HTTPS معمولی' },
  telproxy: { icon:'ti-brand-telegram', title:'Telegram Proxy', desc:'پروکسی MTProto مستقیم روی یک پورت TCP اختصاصی' },
  multi:    { icon:'ti-layers-intersect', title:'Multi Protocol', desc:'یک ساب شامل همه پروتکل‌ها، بدون پروکسی تلگرام' },
  shadowsocks: { icon:'ti-lock-bolt', title:'Shadowsocks TLS', desc:'شادوساکس روی TLS/WebSocket با مسیر اختصاصی' }
};
const TRANSPORT_INFO = {
  'ws':               { icon:'ti-link',    title:'WebSocket',            desc:'پایدار و سازگار با همه شرایط شبکه' },
  'xhttp-packet-up':  { icon:'ti-package', title:'XHTTP · packet-up',    desc:'سازگاری بالا با CDN و پروکسی‌ها' },
  'xhttp-stream-up':  { icon:'ti-rocket',  title:'XHTTP · stream-up',    desc:'تاخیر پایین‌تر برای اتصال‌های پرسرعت' }
};

function cmSelectBase(val, el){
  cmBase = val;
  document.querySelectorAll('#dd-base .cm-opt').forEach(o => o.classList.remove('sel'));
  el.classList.add('sel');
  const info = BASE_INFO[val];
  document.getElementById('dd-base-icon').innerHTML = `<i class="ti ${info.icon}"></i>`;
  document.getElementById('dd-base-current').textContent = info.title;
  document.getElementById('dd-base-current-desc').textContent = info.desc;
  cmToggleDD('dd-base');

  const transportSection = document.getElementById('transport-section');
  const normalNote = document.getElementById('transport-note');
  const mtNote = document.getElementById('mtproto-note');
  const portField = document.getElementById('mtproto-port-field');
  if (val === 'multi') {
    transportSection.style.display = 'none';
    normalNote.style.display = 'flex';
    mtNote.style.display = 'none';
    portField.style.display = 'none';
    document.getElementById('cm-head-title').textContent = 'ساخت ساب مولتی پروتکل';
    document.getElementById('cm-head-sub').textContent = 'همه پروتکل‌ها در یک ساب؛ پروکسی تلگرام جدا می‌ماند';
    document.getElementById('cm-submit-text').textContent = 'ساخت ساب مولتی';
    document.getElementById('cm-head-icon').innerHTML = '<i class="ti ti-layers-intersect"></i>';
    document.getElementById('nl-proto').value = 'multi';
    return;
  }
  if (val === 'shadowsocks') {
    transportSection.style.display = 'none';
    normalNote.style.display = 'flex';
    mtNote.style.display = 'none';
    portField.style.display = 'none';
    document.getElementById('cm-head-title').textContent = 'ساخت Shadowsocks TLS';
    document.getElementById('cm-head-sub').textContent = 'شادوساکس با TLS و مسیر اختصاصی';
    document.getElementById('cm-submit-text').textContent = 'ساخت Shadowsocks';
    document.getElementById('cm-head-icon').innerHTML = '<i class="ti ti-lock-bolt"></i>';
    document.getElementById('nl-proto').value = 'shadowsocks-tls';
    return;
  }
  if (val === 'telproxy') {
    transportSection.style.display = 'none';
    normalNote.style.display = 'none';
    mtNote.style.display = 'flex';
    portField.style.display = 'block';
    document.getElementById('cm-head-title').textContent = 'ساخت پروکسی جدید';
    document.getElementById('cm-head-sub').textContent = 'ساخت پروکسی تلگرام (MTProto) با پورت TCP اختصاصی';
    document.getElementById('cm-submit-text').textContent = 'ساخت پروکسی';
    document.getElementById('cm-head-icon').innerHTML = '<i class="ti ti-brand-telegram"></i>';
  } else {
    transportSection.style.display = '';
    normalNote.style.display = 'flex';
    mtNote.style.display = 'none';
    portField.style.display = 'none';
    document.getElementById('cm-head-title').textContent = 'ساخت کانفیگ جدید';
    document.getElementById('cm-head-sub').textContent = 'تنظیمات کامل پروتکل، ترابرد و محدودیت‌ها در یک صفحه';
    document.getElementById('cm-submit-text').textContent = 'ساخت کانفیگ';
    document.getElementById('cm-head-icon').innerHTML = '<i class="ti ti-square-rounded-plus"></i>';
  }
  cmApplyProto();
}

function cmSelectTransport(val, el){
  cmTransport = val;
  document.querySelectorAll('#dd-transport .cm-opt').forEach(o => o.classList.remove('sel'));
  el.classList.add('sel');
  const info = TRANSPORT_INFO[val];
  document.getElementById('dd-transport-icon').innerHTML = `<i class="ti ${info.icon}"></i>`;
  document.getElementById('dd-transport-current').textContent = info.title;
  document.getElementById('dd-transport-current-desc').textContent = info.desc;
  cmToggleDD('dd-transport');
  cmApplyProto();
}
function cmApplyProto(){
  if (cmBase === 'telproxy') {
    document.getElementById('nl-proto').value = 'mtproto';
    return;
  }
  const val = cmTransport === 'ws'
    ? (cmBase === 'trojan' ? 'trojan-ws' : 'vless-ws')
    : (cmBase === 'trojan' ? `trojan-${cmTransport}` : cmTransport);
  document.getElementById('nl-proto').value = val;
}

/* ── سهمیه ترافیک و انقضا: هم با پیل، هم با تایپ مستقیم قابل تنظیم‌اند ── */
function cmQuota(val, unit, el){
  document.getElementById('nl-val').value = val === 0 ? '' : val;
  document.getElementById('nl-unit').value = unit;
  el.parentElement.querySelectorAll('.cm-pill').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
}
function cmExpiry(days, el){
  document.getElementById('nl-exp').value = days === 0 ? '' : days;
  el.parentElement.querySelectorAll('.cm-pill').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
}

function cmSetSni(domain, el){
  document.getElementById('nl-mtproto-domain').value = domain;
  el.parentElement.querySelectorAll('.cm-pill').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
}
function cmClearSniPills(){
  const wrap = document.getElementById('nl-mtproto-domain').closest('.cm-section').querySelector('.cm-pills');
  wrap?.querySelectorAll('.cm-pill').forEach(c => c.classList.remove('active'));
}

/* وقتی کاربر خودش عدد رو دستی تایپ می‌کنه، انتخاب پیل‌ها برداشته بشه */
document.getElementById('nl-val')?.addEventListener('input', () => {
  document.querySelectorAll('#nl-val').forEach(()=>{});
  const wrap = document.getElementById('nl-val').closest('.cm-field').querySelector('.cm-pills');
  wrap?.querySelectorAll('.cm-pill').forEach(c => c.classList.remove('active'));
});
document.getElementById('nl-exp')?.addEventListener('input', () => {
  const wrap = document.getElementById('nl-exp').closest('.cm-field').querySelector('.cm-pills');
  wrap?.querySelectorAll('.cm-pill').forEach(c => c.classList.remove('active'));
});

async function createLink(){
  const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';
  const val=document.getElementById('nl-val').value;
  const unit=document.getElementById('nl-unit').value;
  const exp=document.getElementById('nl-exp').value;
  const note=document.getElementById('nl-note').value.trim();
  const custom_path=document.getElementById('nl-path').value.trim();
  const sub_id=document.getElementById('nl-sub').value||null;
  const protocol=document.getElementById('nl-proto').value||'vless-ws';
  const isMt = protocol === 'mtproto';
  const mtproto_port = isMt ? (document.getElementById('nl-mtproto-port').value || null) : null;
  const mtproto_domain = isMt ? (document.getElementById('nl-mtproto-domain').value.trim() || null) : null;
  try{
    const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,custom_path,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,protocol,mtproto_port,mtproto_domain})});
    if(!r.ok){
      const d=await r.json().catch(()=>({}));
      throw new Error(d.detail||'failed');
    }
    const d=await r.json().catch(()=>({}));
    const copyTarget = d.sub_url || d.vless_link;
    if(copyTarget && navigator.clipboard) navigator.clipboard.writeText(copyTarget).catch(()=>{});
    ['nl-label','nl-path','nl-val','nl-exp','nl-note','nl-mtproto-port','nl-mtproto-domain'].forEach(id=>document.getElementById(id).value='');
    toast(protocol==='multi' ? 'ساب مولتی ساخته شد و لینک کپی شد' : (isMt ? 'پروکسی ساخته شد و لینک کپی شد' : (protocol==='shadowsocks-tls' ? 'Shadowsocks TLS ساخته شد و لینک کپی شد' : 'کانفیگ ساخته شد')),'ok');
    loadLinks();
  }catch(e){toast(' '+e.message,'err')}
}


function openEditLink(uuid){
  const l=(window.__rawLinksList||allLinksList).find(x=>x.uuid===uuid);
  if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label;
  document.getElementById('el-note').value=l.note||'';
  if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
  else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}
  document.getElementById('el-exp').value='';
  openModal('modal-edit-link');
}
async function saveEditLink(){
  const uuid=document.getElementById('el-uuid').value;
  const label=document.getElementById('el-label').value.trim();
  const note=document.getElementById('el-note').value.trim();
  const val=document.getElementById('el-val').value;
  const unit=document.getElementById('el-unit').value;
  const exp=document.getElementById('el-exp').value;
  const body={label,note,limit_value:val||0,limit_unit:unit};
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('کانفیگ ویرایش شد ','ok');loadLinks();
  }catch(e){toast('خطا در ویرایش','err')}
}
async function toggleActive(uuid,newState){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد ':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function resetUsage(uuid){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف ریست شد ','ok');loadLinks();}catch(e){toast('خطا','err')}
}
let atCurrentUuid = null;

function openAdTagModal(uuid, label, currentTag){
  atCurrentUuid = uuid;
  document.getElementById('at-cfg-name').textContent = label;
  document.getElementById('at-tag').value = currentTag || '';
  openModal('modal-ad-tag');
  setTimeout(()=>document.getElementById('at-tag').focus(), 150);
}

function mtPlainSecret(fullSecret){
  if (!fullSecret) return '';
  // فرمت mtg: "ee" + 32 کاراکتر هگز سکرت + دامنه‌ی fake-TLS به‌صورت هگز
  if (fullSecret.startsWith('ee') && fullSecret.length > 34) {
    return fullSecret.slice(2, 34);
  }
  return fullSecret;
}

function openMtInfoModal(label, secret, fullLink, hasPublicHost){
  document.getElementById('mti-cfg-name').textContent = label;
  document.getElementById('mti-secret').textContent = mtPlainSecret(secret) || '—';
  document.getElementById('mti-link').textContent = fullLink || '—';
  const warnEl = document.getElementById('mti-warn');
  if (warnEl) warnEl.style.display = hasPublicHost ? 'none' : 'flex';
  openModal('modal-mt-info');
}

function cpMtiField(id, msg){
  const el = document.getElementById(id);
  navigator.clipboard.writeText(el.textContent).then(()=>toast(msg,'ok'));
}

async function submitAdTag(){
  if(!atCurrentUuid) return;
  const tag = document.getElementById('at-tag').value.trim();
  if(!tag){ toast('ad_tag نمی‌تواند خالی باشد','err'); return; }

  const btn = document.getElementById('at-submit-btn');
  btn.disabled = true;
  btn.innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال اعمال...';

  try{
    const r = await authF('/api/links/'+atCurrentUuid+'/ad-tag', {
      method:'PATCH', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ad_tag: tag})
    });
    if(!r.ok){ const d = await r.json().catch(()=>({})); throw new Error(d.detail || 'خطا'); }
    closeModal('modal-ad-tag');
    toast('تبلیغ ثبت شد، پروکسی در حال ری‌استارت است...','ok');
    setTimeout(loadLinks, 2000);
  }catch(e){
    toast(' '+e.message,'err');
  }
  btn.disabled = false;
  btn.innerHTML = '<i class="ti ti-check"></i> ذخیره و اعمال';
}
async function deleteLink(uuid){
  if(!confirm('حذف این کانفیگ؟'))return;
  try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ','ok');loadLinks();}catch(e){toast('خطا','err')}
}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
let allSubsRaw=[];
async function loadSubs(){
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-nb').textContent=subs.length;
    document.getElementById('subs-pg-cnt').textContent=toFa(subs.length)+' گروه';
    renderSubsGrid(subs);
  }catch(e){console.error(e)}
}
function renderSubsGrid(subs){
  const grid=document.getElementById('subs-grid');
  if(!subs.length){
    grid.innerHTML='<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>';
    return;
  }
  grid.innerHTML=subs.map(s=>`
    <div class="sub-card">
      <div class="sub-card-top">
        <div class="sub-card-head-v2">
          <div class="sub-card-icon"><i class="ti ti-folder"></i></div>
          <div class="sub-card-titles">
            <div class="sub-card-name-v2">${esc(s.name)}</div>
            ${s.desc?`<div class="sub-card-desc-v2">${esc(s.desc)}</div>`:'<div class="sub-card-desc-v2" style="opacity:.5">بدون توضیحات</div>'}
          </div>
          <div class="sub-card-lock-badge ${s.has_password?'locked':'open'}" title="${s.has_password?'رمزدار':'پابلیک'}">
            <i class="ti ${s.has_password?'ti-lock':'ti-lock-open'}"></i>
          </div>
        </div>
        <div class="sub-card-stats">
          <div class="sub-card-stat"><div class="sub-card-stat-val">${toFa(s.links_count)}</div><div class="sub-card-stat-label">کانفیگ</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">${toFa(s.active_count)}</div><div class="sub-card-stat-label">فعال</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-card-stat-label">مصرف</div></div>
        </div>
      </div>
      <div class="sub-card-url-row">
        <span class="sub-card-url-text">${esc(s.public_url)}</span>
        <button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('لینک پابلیک کپی شد','ok'))" title="کپی"><i class="ti ti-copy"></i></button>
        <button class="sub-card-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')" title="باز کردن"><i class="ti ti-external-link"></i></button>
      </div>
      <div class="sub-card-bottom">
        <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> کانفیگ‌ها</button>
        <button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('لینک ساب کپی شد','ok'))"><i class="ti ti-rss"></i> ساب</button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(s.sub_url)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteSub('${esc(s.sub_id)}')" title="حذف"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  `).join('');
}
function filterSubs(q){
  q=q.trim().toLowerCase();
  if(!q){renderSubsGrid(allSubsRaw);return}
  renderSubsGrid(allSubsRaw.filter(s=>s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q)));
}
async function createSub(){
  const name=document.getElementById('ns-name').value.trim()||'گروه جدید';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  try{
    const r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(id=>document.getElementById(id).value='');
    closeModal('modal-create-sub');
    toast('گروه ساخته شد ','ok');loadSubs();
  }catch(e){toast('خطا در ساخت گروه','err')}
}
async function deleteSub(sub_id){
  if(!confirm('حذف این گروه؟ کانفیگ‌ها حذف نمی‌شوند.'))return;
  try{const r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('گروه حذف شد ','ok');loadSubs();loadLinks();}catch(e){toast('خطا','err')}
}
let lmodalLinks=[],lmodalInSub=new Set();
async function openSubLinks(sub_id,name){
  currentSubId=sub_id;
  document.getElementById('modal-sub-name').textContent=name;
  document.getElementById('modal-links-body').innerHTML='<div style="color:var(--t3);font-size:12px;padding:20px;text-align:center"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite;font-size:20px"></i></div>';
  document.getElementById('lmodal-search-inp').value='';
  openModal('modal-links');
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    const thisSub=subs.find(s=>s.sub_id===sub_id);
    lmodalInSub=new Set(thisSub?.link_ids||[]);
    lmodalLinks=links;
    renderLmodalList(links);
  }catch(e){toast('خطا در بارگذاری','err')}
}
function renderLmodalList(links){
  const body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div class="empty" style="padding:30px"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>';updateLmodalCount();return}
  body.innerHTML=links.map(l=>{
    const checked=lmodalInSub.has(l.uuid);
    const on=l.active&&!l.expired;
    return `<div class="lrow-v2 ${checked?'checked':''}" data-uuid="${l.uuid}" data-name="${esc(l.label).toLowerCase()}" onclick="toggleLrow('${l.uuid}',this)">
      <div class="lrow-v2-check"><i class="ti ti-check"></i></div>
      <div class="lrow-v2-avatar"><i class="ti ti-key"></i></div>
      <div class="lrow-v2-info">
        <div class="lrow-v2-name">${esc(l.label)}</div>
        <div class="lrow-v2-meta"><i class="ti ti-database" style="font-size:10px"></i> ${fmtB(l.used_bytes)}</div>
      </div>
      <span class="lrow-v2-status ${on?'on':'off'}">${on?'فعال':'غیرفعال'}</span>
    </div>`;
  }).join('');
  updateLmodalCount();
}
function toggleLrow(uuid,el){
  if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid);el.classList.remove('checked')}
  else{lmodalInSub.add(uuid);el.classList.add('checked')}
  updateLmodalCount();
}
function lmodalSelectAll(state){
  lmodalLinks.forEach(l=>{if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid)});
  renderLmodalList(lmodalLinks);
}
function updateLmodalCount(){
  const el=document.getElementById('lmodal-count');
  if(el)el.textContent=toFa(lmodalInSub.size)+' انتخاب شده';
}
function filterLmodal(q){
  q=q.trim().toLowerCase();
  document.querySelectorAll('#modal-links-body .lrow-v2').forEach(row=>{
    row.style.display = !q || row.dataset.name.includes(q) ? '' : 'none';
  });
}
async function saveSubLinks(){
  if(!currentSubId)return;
  const link_ids=[...lmodalInSub];
  try{
    const r=await authF('/api/subs/'+currentSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids})});
    if(!r.ok)throw new Error();
    await Promise.all(lmodalLinks.map(l=>
      authF('/api/links/'+l.uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({sub_id:lmodalInSub.has(l.uuid)?currentSubId:null})})
    ));
    closeModal('modal-links');
    toast('کانفیگ‌های گروه ذخیره شدند ','ok');
    loadSubs();loadLinks();
  }catch(e){toast('خطا در ذخیره','err')}
}
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    const el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>هنوز گروهی ندارید</p></div>';return}
    el.innerHTML=subs.map(s=>`
      <div style="padding:13px 15px;background:var(--accent-d);border:1px solid var(--card-b);border-radius:10px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">
        <div>
          <div style="font-weight:700;font-size:13px;margin-bottom:3px">${esc(s.name)}</div>
          <div style="font-family:ui-monospace,monospace;font-size:10px;color:#A78BFA">${esc(s.sub_url)}</div>
          <div style="font-size:10px;color:var(--t3);margin-top:3px">${toFa(s.links_count)} کانفیگ · ${esc(s.total_used_fmt)} مصرف ${s.has_password?'·  رمزدار':''}</div>
        </div>
        <div style="display:flex;gap:5px;flex-wrap:wrap">
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-copy"></i> ساب</button>
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-globe"></i> پابلیک</button>
          <button class="btn btn-sm btn-g" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
        </div>
      </div>
    `).join('');
  }catch(e){}
}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(()=>toast('کپی شد ','ok'))}
function parseBytesFmt(s){
  if(!s)return 0;
  const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);
  if(!m)return 0;
  const n=parseFloat(m[1]),u=m[2].toUpperCase();
  const mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};
  return n*(mult[u]||1);
}
async function loadConns(){
  try{
    const r=await authF('/api/connections'),d=await r.json();
    const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.count+' اتصال';
    document.getElementById('ch-count').textContent=toFa(d.count);
    const conns=d.connections||[];
    if(!d.count){
      grid.innerHTML='';ce.style.display='block';
      document.getElementById('ch-traffic').textContent='—';
      document.getElementById('ch-avgdur').textContent='—';
      document.getElementById('ch-uniq').textContent='—';
      return;
    }
    ce.style.display='none';
    const totalBytes=conns.reduce((s,c)=>s+parseBytesFmt(c.bytes_fmt),0);
    document.getElementById('ch-traffic').textContent=fmtB(totalBytes);
    const uniqIps=new Set(conns.map(c=>c.ip)).size;
    document.getElementById('ch-uniq').textContent=toFa(uniqIps);
    const durs=conns.map(c=>c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0);
    const avgSec=durs.length?Math.floor(durs.reduce((a,b)=>a+b,0)/durs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';
    const maxDur=Math.max(...durs,1);
    grid.innerHTML=conns.map(c=>{
      const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';
      const durPct=Math.min(100,Math.round((secs/maxDur)*100));
      const protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');
      return `<div class="conn-card-v2">
        <div class="conn-card-v2-glow"></div>
        <div class="conn-card-v2-top">
          <div class="conn-avatar"><i class="ti ti-device-desktop"></i></div>
          <div class="conn-card-v2-id">
            <div class="conn-ip-v2">${esc(c.ip)}
              <button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}').then(()=>toast('IP کپی شد','ok'))" title="کپی IP"><i class="ti ti-copy"></i></button>
            </div>
            <div class="conn-label-v2">${esc(c.label)}</div>
          </div>
          <span class="conn-status-pill"><span class="dot dg pulse"></span> زنده</span>
        </div>
        <div class="conn-card-v2-divider"></div>
        <div class="conn-card-v2-body">
          <div class="conn-proto-row">${protoBadge(protoVal)}</div>
          <div class="conn-stat-row">
            <div class="conn-stat-box">
              <div class="conn-stat-icon"><i class="ti ti-transfer"></i></div>
              <div>
                <div class="conn-stat-text-label">ترافیک</div>
                <div class="conn-stat-text-val">${esc(c.bytes_fmt)}</div>
              </div>
            </div>
            <div class="conn-stat-box">
              <div class="conn-stat-icon time"><i class="ti ti-clock"></i></div>
              <div>
                <div class="conn-stat-text-label">مدت اتصال</div>
                <div class="conn-stat-text-val">${dur}</div>
              </div>
            </div>
          </div>
          <div class="conn-duration-track"><div class="conn-duration-fill" style="width:${durPct}%"></div></div>
        </div>
      </div>`;
    }).join('');
  }catch(e){console.error(e)}
}
async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}
async function fetchDefaultVless(){
  try{const r=await authF('/api/links'),d=await r.json();const links=d.links||[];const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'هنوز کانفیگی وجود ندارد';}catch(e){}
}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ','ok'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('رفرش شد','ok')}

async function loadDbStatus(){
  try{
    const r=await authF('/api/database/status'),d=await r.json();
    const badge=document.getElementById('db-status-badge'),cur=document.getElementById('db-current-url'),storage=document.getElementById('storage-mode-label');
    if(badge){badge.className='ml-auto badge '+(d.connected?'bg-green':'bg-amber');badge.textContent=d.connected?'PostgreSQL متصل':(d.configured?'تنظیم شده، قطع':'JSON محلی');}
    if(cur)cur.value=d.url||'';
    if(storage)storage.textContent=d.mode||'JSON File';
  }catch(e){}
}
async function connectDatabase(kind){
  const id=kind==='internal'?'db-internal-url':'db-external-url';
  const url=(document.getElementById(id)?.value||'').trim();
  if(!url){toast('لینک دیتابیس را وارد کنید','err');return}
  try{
    const r=await authF('/api/database/connect',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({url})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'اتصال ناموفق بود');
    toast('دیتابیس متصل شد و اطلاعات ذخیره شد','ok');
    loadDbStatus();
  }catch(e){toast(' '+e.message,'err')}
}
async function disconnectDatabase(){
  try{await authF('/api/database/disconnect',{method:'POST'});toast('اتصال دیتابیس قطع شد','ok');loadDbStatus();}catch(e){toast('خطا در قطع اتصال','err')}
}

async function changePw(){
  const cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;
  if(!cur||!nw||!cf){toast('همه فیلدها را پر کنید','err');return}
  if(nw.length<4){toast('حداقل ۴ کاراکتر','err');return}
  if(nw!==cf){toast('تکرار رمز اشتباه','err');return}
  try{
    const r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'خطا');
    toast('رمز تغییر کرد ','ok');
    ['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='');
  }catch(e){toast(' '+e.message,'err')}
}
function togglePwField(id,btn){
  const inp=document.getElementById(id);
  const icon=btn.querySelector('i');
  const toText=inp.type==='password';
  inp.type=toText?'text':'password';
  icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}
function checkPwStrength(val){
  const segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');
  const label=document.getElementById('pw-strength-label');
  const reqLen=document.getElementById('req-len'),reqNum=document.getElementById('req-num'),reqCase=document.getElementById('req-case');
  const hasLen=val.length>=4,hasNum=/\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;
  reqLen.classList.toggle('met',hasLen);
  reqNum.classList.toggle('met',hasNum);
  reqCase.classList.toggle('met',hasCase);
  let score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;
  const colors=['#EF4444','#F59E0B','#3B82F6','#10B981'],labels=['خیلی ضعیف','ضعیف','متوسط','قوی'];
  segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,116,139,.2)'});
  if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> قدرت رمز';return}
  label.innerHTML=`<i class="ti ti-shield-check" style="color:${colors[Math.max(0,score-1)]}"></i> ${labels[Math.max(0,score-1)]}`;
}
function makeGradient(ctx,color1,color2){
  const g=ctx.createLinearGradient(0,0,0,260);
  g.addColorStop(0,color1);g.addColorStop(1,color2);
  return g;
}
function initCharts(){
  const c1=document.getElementById('ch1').getContext('2d');
  const grad1=makeGradient(c1,'rgba(59,130,246,.38)','rgba(59,130,246,0)');
  const opts={
    responsive:true,maintainAspectRatio:false,
    interaction:{mode:'index',intersect:false},
    plugins:{
      legend:{display:false},
      tooltip:{
        backgroundColor:'rgba(13,27,46,.96)',borderColor:'rgba(59,130,246,.3)',borderWidth:1,
        titleColor:'#E8F4FF',bodyColor:'#7BAED4',padding:11,cornerRadius:10,displayColors:false,
        titleFont:{family:'Vazirmatn',size:11,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
        callbacks:{label:v=>`${v.parsed.y.toFixed(2)} مگابایت`}
      }
    },
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'}}},
      y:{grid:{color:'rgba(59,130,246,.06)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'},callback:v=>v+' MB'}}
    },
    elements:{line:{capBezierPoints:true}}
  };
  const ds1={label:'MB',data:[],borderColor:'#3B82F6',backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:'#3B82F6',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5};
  ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[ds1]},options:opts});

  function makeGradientV2(ctx,c1,c2,c3){
    const g=ctx.createLinearGradient(0,0,0,320);
    g.addColorStop(0,c1);g.addColorStop(.6,c2);g.addColorStop(1,c3);
    return g;
  }
  const c3ctx=document.getElementById('ch3').getContext('2d');
  const gradFill3=makeGradientV2(c3ctx,'rgba(59,130,246,.45)','rgba(59,130,246,.08)','rgba(59,130,246,0)');
  ch3=new Chart(document.getElementById('ch3'),{
    type:'line',
    data:{labels:[],datasets:[
      {label:'مصرف',data:[],borderColor:'#3B82F6',backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#3B82F6',pointHoverBorderWidth:3,borderWidth:3,order:2},
      {label:'میانگین',data:[],borderColor:'#F59E0B',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}
    ]},
    options:{
      responsive:true,maintainAspectRatio:false,
      interaction:{mode:'index',intersect:false},
      plugins:{
        legend:{display:false},
        tooltip:{
          backgroundColor:'rgba(13,27,46,.97)',borderColor:'rgba(59,130,246,.35)',borderWidth:1,
          titleColor:'#E8F4FF',bodyColor:'#9DC3E8',padding:13,cornerRadius:12,displayColors:true,boxPadding:4,
          titleFont:{family:'Vazirmatn',size:11.5,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
          callbacks:{label:v=>` ${v.dataset.label}: ${v.parsed.y.toFixed(2)} MB`}
        }
      },
      scales:{
        x:{grid:{display:false},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},
        y:{grid:{color:'rgba(59,130,246,.05)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9.5,family:'Vazirmatn'},callback:v=>v+' MB'}}
      }
    }
  });

  ch2=new Chart(document.getElementById('ch2'),{
    type:'doughnut',
    data:{labels:['VLESS WS','Trojan WS','XHTTP','Shadowsocks TLS','MTProto'],datasets:[{
      data:[1,1,1,1,1],
      backgroundColor:['#2563EB','#111827','#8B5CF6','#14B8A6','#F59E0B'],
      borderColor:getComputedStyle(document.documentElement).getPropertyValue('--card')||'#0d1b2e',
      borderWidth:4,hoverOffset:10,borderRadius:6,spacing:3
    }]},
    options:{
      responsive:true,maintainAspectRatio:false,cutout:'72%',
      plugins:{
        legend:{position:'bottom',labels:{color:'var(--t2)',font:{size:10,family:'Vazirmatn'},padding:12,usePointStyle:true,pointStyle:'circle'}},
        tooltip:{backgroundColor:'rgba(13,27,46,.96)',borderColor:'rgba(59,130,246,.3)',borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}
      }
    }
  });
}
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log'),p=document.createElement('p');const colors={ok:'#34D399',err:'#F87171',info:'#7BAED4',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('fa-IR')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','اتصال: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok',' متصل - UUID معتبر');ws.onerror=()=>wsLog('err',' خطا - UUID نامعتبر یا غیرفعال');ws.onmessage=m=>wsLog('info','دریافت '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','قطع ('+e.code+')'+(e.code===1008?' - دسترسی رد شد':''))}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}
const ICON_MAP={ad:'ti-speakerphone',news:'ti-news',warning:'ti-alert-triangle',urgent:'ti-alert-octagon'};
const LABEL_MAP={ad:'تبلیغ',news:'خبر',warning:'هشدار',urgent:'فوری'};
async function loadAnnouncements(){
  try{
    const r=await authF('/api/announcements'),d=await r.json();
    const seen=JSON.parse(localStorage.getItem('oxnet-seen-ann')||'[]');
    const list=(d.announcements||[]).filter(a=>!seen.includes(a.id));
    document.getElementById('ann-banner-wrap').innerHTML=list.map(a=>`
      <div class="ann-card ${a.type}" id="ann-${a.id}">
        <button class="ann-close" onclick="dismissAnn('${a.id}')"><i class="ti ti-x"></i></button>
        <div class="ann-icon"><i class="ti ${ICON_MAP[a.type]||'ti-bell'}"></i></div>
        <div class="ann-body">
          <div class="ann-title">${esc(a.title)} <span style="font-size:9px;color:var(--t3)">· ${LABEL_MAP[a.type]||''}</span></div>
          <div class="ann-text">${esc(a.body)}</div>
          ${a.image_url?`<img class="ann-img" src="${esc(a.image_url)}">`:''}
        </div>
      </div>`).join('');
      if (list.length) {
      authF('/api/announcements/view', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ids: list.map(a => a.id) })
      }).catch(() => {});
    }
  }catch(e){}
}
function dismissAnn(id){
  const seen=JSON.parse(localStorage.getItem('oxnet-seen-ann')||'[]');
  seen.push(id);localStorage.setItem('oxnet-seen-ann',JSON.stringify(seen));
  document.getElementById('ann-'+id)?.remove();
}
let lastSupportMsgId = null;
 
function fmtSupTime(ts){
  const d = new Date(ts);
  return d.toLocaleTimeString('fa-IR',{hour:'2-digit',minute:'2-digit'});
}
function fmtSupDate(ts){
  const d = new Date(ts);
  const today = new Date();
  const isToday = d.toDateString() === today.toDateString();
  if (isToday) return 'امروز';
  const y = new Date(today); y.setDate(y.getDate()-1);
  if (d.toDateString() === y.toDateString()) return 'دیروز';
  return d.toLocaleDateString('fa-IR');
}
 
async function loadSupportMsgs() {
  try {
    const r = await authF('/api/support/messages'),
      d = await r.json();
    const msgs = d.messages || [];
    const blocked = !!d.blocked;
    const el = document.getElementById('support-msgs');

    if (el) {
      if (!msgs.length) {
        el.innerHTML =
          '<div class="sup-empty"><i class="ti ti-message-circle-2"></i><b>هنوز گفتگویی نیست</b><span>این بخش در نسخه مستقل حذف شده است</span></div>';
      } else {
        let html = '',
          lastDate = '';
        msgs.forEach((m, idx) => {
          const dateLabel = fmtSupDate(m.created_at);
          if (dateLabel !== lastDate) {
            html +=
              '<div class="sup-date-sep"><span>' + dateLabel + '</span></div>';
            lastDate = dateLabel;
          }
          const isLastClientMsg =
            m.sender === 'client' && idx === msgs.length - 1; // not used, but kept
          const seenTick =
            m.sender === 'client'
              ? m.read_by_admin
                ? '<i class="ti ti-checks seen"></i>'
                : '<i class="ti ti-check"></i>'
              : '';
          //  Fixed: removed backslashes before backticks
          html += `
            <div class="sup-msg-row ${m.sender}">
              <div class="sup-msg ${m.sender}">
                ${esc(m.body)}
                <span class="sup-time">${fmtSupTime(m.created_at)} ${seenTick}</span>
              </div>
              <div class="sup-avatar ${m.sender}"><i class="ti ${m.sender === 'admin' ? 'ti-headset' : 'ti-user'}"></i></div>
            </div>`;
        });
        el.innerHTML = html;
      }
      const shouldScroll =
        !lastSupportMsgId ||
        (msgs.length && msgs[msgs.length - 1].id !== lastSupportMsgId);
      if (shouldScroll) el.scrollTop = el.scrollHeight;
      if (msgs.length) lastSupportMsgId = msgs[msgs.length - 1].id;
    }

    const banner = document.getElementById('sup-blocked-banner');
    const inputRow = document.getElementById('sup-input-row');
    if (banner) banner.style.display = blocked ? 'flex' : 'none';
    if (inputRow) inputRow.classList.toggle('disabled', blocked);

    const nb = document.getElementById('support-nb');
    if (nb) {
      const lastAdmin = [...msgs].reverse().find((m) => m.sender === 'admin');
      const seenId = localStorage.getItem('oxnet-last-seen-support-msg');
      const onSupportPage = document
        .getElementById('pg-support')
        .classList.contains('on');
      const hasNew = lastAdmin && lastAdmin.id !== seenId && !onSupportPage;
      nb.style.display = hasNew ? 'inline-flex' : 'none';
      if (lastAdmin && onSupportPage)
        localStorage.setItem('oxnet-last-seen-support-msg', lastAdmin.id);
    }
  } catch (e) {
    // silent fail
  }
}
 
async function sendSupportMsg(){
  const inp=document.getElementById('support-inp');const msg=inp.value.trim();if(!msg)return;
  inp.disabled = true;
  try{
    const r=await authF('/api/support/send',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:msg})});
    if(r.status===403){toast('این بخش حذف شده است','err');loadSupportMsgs();inp.disabled=false;return}
    if(!r.ok)throw new Error();
    inp.value='';loadSupportMsgs();
  }catch(e){toast('خطا در ارسال پیام','err')}
  inp.disabled = false;
  inp.focus();
}
document.addEventListener('DOMContentLoaded', async () => {
  await checkAuth();
  initCharts();
  document.getElementById('set-host').textContent = location.host;
  document.getElementById('sub-all-url') && (document.getElementById('sub-all-url').textContent = location.protocol + '//' + location.host + '/sub-all');
  
  // ابتدا نسخه را بررسی کن
  // بروزرسانی خودکار در نسخه مستقل حذف شده است

  // بقیه‌ی کدهای اولیه
  fetchStats();
  fetchDefaultVless();
  loadLinks();
  loadSubs();
  loadAnnouncements();
  loadDbStatus();
  // بخش مرکزی حذف شده است

  setInterval(fetchStats, 2000);
  setInterval(() => {
    if (document.getElementById('pg-links').classList.contains('on')) loadLinks();
    if (document.getElementById('pg-subgroups').classList.contains('on')) loadSubs();
    if (document.getElementById('pg-subscriptions').classList.contains('on')) loadSubsPage();
    if (document.getElementById('pg-connections').classList.contains('on')) loadConns();
    if (document.getElementById('pg-logs').classList.contains('on')) loadActivity();
    if (document.getElementById('pg-support').classList.contains('on')) loadSupportMsgs();
    // بروزرسانی خودکار حذف شده است
  }, 5000);
  setInterval(loadAnnouncements, 3000);
});

function timeAgoFa(ts){
  const diff = Math.max(0, (Date.now()/1000) - ts);
  if(diff < 60) return 'همین الان';
  if(diff < 3600) return toFa(Math.floor(diff/60))+' دقیقه پیش';
  if(diff < 86400) return toFa(Math.floor(diff/3600))+' ساعت پیش';
  if(diff < 2592000) return toFa(Math.floor(diff/86400))+' روز پیش';
  return new Date(ts*1000).toLocaleDateString('fa-IR');
}

async function loadVersion(){
  try{
    const r=await authF('/api/version'), d=await r.json();
    const cur=d.current||{}, lat=d.latest||{};

    document.getElementById('ver-current').textContent=cur.version||'—';
    document.getElementById('ver-current-desc').textContent=cur.description||'بدون توضیحات ثبت‌شده برای این نسخه';
    document.getElementById('ver-repo').textContent=d.repo||'تنظیم نشده';
    document.getElementById('ver-branch').textContent=d.branch||'—';

    const badge=document.getElementById('ver-status-badge'), nb=document.getElementById('update-nb');
    const latestCard=document.getElementById('upd-latest-card');

    if(lat.error){
      badge.innerHTML='<span class="upd-pill upd-pill-amber"><i class="ti ti-alert-triangle"></i> '+esc(lat.error)+'</span>';
      latestCard.style.display='none';
      nb.style.display='none';
      updateAvailable = false;
    } else if(d.update_available){
      badge.innerHTML='<span class="upd-pill upd-pill-amber"><span class="upd-dot"></span> بروزرسانی جدید موجود است</span>';
      document.getElementById('ver-latest-num').textContent=lat.version||'—';
      document.getElementById('ver-latest-desc').textContent=lat.description||'بدون توضیحات';
      latestCard.style.display='flex';
      nb.style.display='inline-flex';
      nb.textContent='1';
      // تنظیم متغیرهای سراسری برای مودال
      updateAvailable = true;
      updateVersion = lat.version || '—';
      updateDescription = lat.description || 'بدون توضیحات';
    } else {
      badge.innerHTML='<span class="upd-pill upd-pill-green"><i class="ti ti-circle-check"></i> پنل بروز است</span>';
      latestCard.style.display='none';
      nb.style.display='none';
      updateAvailable = false;
    }
  } catch(e) {
    console.error(e);
    updateAvailable = false;
  }
  loadUpdateHistory();
}

let updatePolling=null, pollTicks=0;
async function startUpdate(){
  if(!confirm('نصب بروزرسانی سرور را چند ثانیه ری‌استارت می‌کند. ادامه می‌دهید؟'))return;
  const btn=document.getElementById('update-btn');
  btn.disabled=true;btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال نصب...';
  document.getElementById('update-progress-wrap').style.display='block';
  pollTicks=0;
  try{
    await authF('/api/update',{method:'POST'});
    toast('بروزرسانی شروع شد','ok');
    updatePolling=setInterval(pollUpdate,900);
  }catch(e){
    toast('خطا در شروع بروزرسانی','err');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-download"></i> نصب بروزرسانی';
  }
}
let btpPolling = null;

function btpSetStatus(icon, color, text, spin){
  const ic = document.getElementById('btp-status-icon');
  ic.className = 'ti ' + icon;
  ic.style.color = color;
  ic.style.animation = spin ? 'spin 1s linear infinite' : '';
  document.getElementById('btp-status-text').textContent = text;
}

function btpToggleButtons(running){
  document.getElementById('btp-start-btn').style.display = running ? 'none' : 'flex';
  document.getElementById('btp-stop-btn').style.display = running ? 'flex' : 'none';
}

function btpChangeToken(){
  document.getElementById('btp-token-section').style.display = '';
  document.getElementById('btp-token-saved-section').style.display = 'none';
}

async function btpCheckTokenState(){
  try{
    const r = await authF('/api/bot-tcp-proxy/status'), d = await r.json();
    if(d.has_token){
      document.getElementById('btp-token-section').style.display = 'none';
      document.getElementById('btp-token-saved-section').style.display = '';
    }else{
      document.getElementById('btp-token-section').style.display = '';
      document.getElementById('btp-token-saved-section').style.display = 'none';
    }
    btpToggleButtons(d.running);
    if(d.running){
      btpPolling = setInterval(pollBotTcpProxy, 1500);
      btpSetStatus('ti-loader-2','var(--accent)', `در حال تلاش... (${d.attempts} تلاش انجام‌شده)`, true);
    }
  }catch(e){}
}

async function startBotTcpProxy(){
  const tokenField = document.getElementById('btp-token');
  const tokenSection=document.getElementById('btp-token-section');
  const token = tokenSection && tokenSection.style.display !== 'none' ? tokenField.value.trim() : '';
  const portVal = document.getElementById('btp-port').value.trim();
  const btn = document.getElementById('btp-start-btn');
  btn.disabled = true;
  btn.innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال اجرا...';
  btpSetStatus('ti-loader-2','var(--accent)','در حال اتصال به Railway...', true);
  document.getElementById('btp-log-box').style.display = 'block';

  const body = { token, port: portVal || undefined };
  if (btpForcedDomain) {
    body.mode = 'whitelist';
    body.target_domains = [btpForcedDomain];
  } else {
    body.mode = 'blacklist';
  }

  try{
    const r = await authF('/api/bot-tcp-proxy/start', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify(body)
    });
    if(!r.ok){ const d = await r.json().catch(()=>({})); throw new Error(d.detail || 'خطا'); }
    document.getElementById('btp-token-section').style.display = 'none';
    document.getElementById('btp-token-saved-section').style.display = '';
    btpToggleButtons(true);
    btpPolling = setInterval(pollBotTcpProxy, 1500);
  }catch(e){
    toast(' '+e.message,'err');
    btpSetStatus('ti-alert-circle','var(--red-t)', e.message, false);
    btn.disabled = false; btn.innerHTML = '<i class="ti ti-player-play"></i> شروع فرآیند';
  }
}
async function stopBotTcpProxy(){
  const btn = document.getElementById('btp-stop-btn');
  btn.disabled = true;
  try{
    await authF('/api/bot-tcp-proxy/stop', {method:'POST'});
    toast('درخواست توقف ارسال شد','ok');
  }catch(e){
    toast('خطا در توقف','err');
  }
  btn.disabled = false;
}

async function pollBotTcpProxy(){
  try{
    const r = await authF('/api/bot-tcp-proxy/status'), d = await r.json();
    const box = document.getElementById('btp-log-box');
    box.innerHTML = (d.logs||[]).map(l=>`<p class="upd-log-line">[${new Date(l.time*1000).toLocaleTimeString('fa-IR')}] ${esc(l.msg)}</p>`).join('') || '<p class="upd-log-empty">لاگی موجود نیست</p>';
    box.scrollTop = box.scrollHeight;

    if(d.running){
      btpToggleButtons(true);
      btpSetStatus('ti-loader-2','var(--accent)', `در حال تلاش... (${d.attempts} تلاش انجام‌شده)`, true);
    }else{
      clearInterval(btpPolling);
      btpToggleButtons(false);
      const btn = document.getElementById('btp-start-btn');
      btn.disabled = false; btn.innerHTML = '<i class="ti ti-player-play"></i> شروع فرآیند';
      if(d.result){
        btpSetStatus('ti-circle-check','var(--green-t)', `موفق — ${d.result.domain}:${d.result.port}`, false);
        toast('پروکسی ساخته شد: '+d.result.domain+':'+d.result.port,'ok');
      } else if(d.stopped_by_user){
        btpSetStatus('ti-player-stop','var(--amber-t)', 'فرآیند متوقف شد', false);
      } else if(d.error){
        btpSetStatus('ti-alert-circle','var(--red-t)', d.error, false);
        toast(' '+d.error,'err');
      }
    }
  }catch(e){}
}
async function pollUpdate(){
  pollTicks++;
  try{
    const r=await fetch('/api/update-log',{credentials:'include'});
    if(r.status===401){clearInterval(updatePolling);location.reload();return}
    const d=await r.json();
    document.getElementById('update-progress-bar').style.width=d.progress+'%';
    document.getElementById('update-progress-pct').textContent=d.progress+'%';
    renderUpdateLog(d.logs);
    if(d.logs && d.logs.length) document.getElementById('update-progress-txt').textContent=d.logs[d.logs.length-1].msg;

    if(!d.running && d.progress>=100){
      document.getElementById('update-progress-txt').textContent='بروزرسانی کامل شد؛ در حال اتصال مجدد...';
      clearInterval(updatePolling);
      let tries=0;
      const reconnect=setInterval(async()=>{
        tries++;
        try{const rr=await fetch('/api/me',{credentials:'include'});if(rr.ok){clearInterval(reconnect);location.reload();}}catch(e){}
        if(tries>40)clearInterval(reconnect);
      },2000);
    }else if(!d.running && pollTicks>3){
      document.getElementById('update-progress-txt').textContent='بروزرسانی متوقف شد (خطا) — لاگ را ببینید';
      document.getElementById('update-btn').disabled=false;
      document.getElementById('update-btn').innerHTML='<i class="ti ti-download"></i> نصب بروزرسانی';
      clearInterval(updatePolling);
    }
  }catch(e){}
}
async function loadUpdateLog(){
  try{const r=await authF('/api/update-log'),d=await r.json();renderUpdateLog(d.logs);}catch(e){}
}
function renderUpdateLog(logs){
  const box=document.getElementById('update-log-box');
  if(!logs||!logs.length){box.innerHTML='<p class="upd-log-empty">لاگی موجود نیست</p>';return}
  box.innerHTML=logs.map(l=>{
    const cls = l.msg.includes('') ? 'err' : (l.msg.includes('') ? 'ok' : '');
    return `<p class="upd-log-line ${cls}">[${new Date(l.time*1000).toLocaleTimeString('fa-IR')}] ${esc(l.msg)}</p>`;
  }).join('');
  box.scrollTop=box.scrollHeight;
}
async function loadUpdateHistory(){
  try{
    const r=await authF('/api/update-history'),d=await r.json();
    const hist=d.history||[];
    document.getElementById('upd-history-count').textContent=toFa(hist.length)+' مورد';
    const el=document.getElementById('upd-history-list');
    if(!hist.length){
      el.innerHTML='<div class="upd-history-empty"><i class="ti ti-history-toggle"></i><p>هنوز هیچ بروزرسانی‌ای ثبت نشده</p></div>';
      return;
    }
    el.innerHTML=hist.map(h=>{
      const isErr = h.status==='err';
      return `
      <div class="upd-item ${isErr?'err':''}">
        <div class="upd-item-dot-wrap"><div class="upd-item-dot"><i class="ti ${isErr?'ti-x':'ti-check'}"></i></div></div>
        <div class="upd-item-card">
          <div class="upd-item-head">
            <div class="upd-item-versions">
              <span>${esc(h.from_version||'—')}</span>
              <i class="ti ti-arrow-left arrow"></i>
              <span class="to">${esc(h.to_version||'—')}</span>
            </div>
            <span class="upd-item-badge ${isErr?'err':'ok'}">${isErr?'ناموفق':'موفق'}</span>
          </div>
          <div class="upd-item-time"><i class="ti ti-clock"></i> ${new Date(h.time*1000).toLocaleString('fa-IR')} · ${timeAgoFa(h.time)}</div>
          ${h.description?`<div class="upd-item-desc">${esc(h.description)}</div>`:''}
          ${isErr && h.error?`<div class="upd-item-err-box"><i class="ti ti-alert-circle"></i> ${esc(h.error)}</div>`:''}
        </div>
      </div>`;
    }).join('');
  }catch(e){console.error(e)}
}
let autoDomainPolling = null;

async function autoGetMtprotoDomain(){
  // اول چک کن توکن ذخیره شده یا نه
  try{
    const r = await authF('/api/bot-tcp-proxy/status'), d = await r.json();
    if(!d.has_token){
      document.getElementById('auto-domain-token-wrap').style.display = 'block';
      document.getElementById('auto-domain-status').innerHTML = '<i class="ti ti-key"></i> برای دریافت خودکار دامنه، ابتدا توکن Railway را وارد کن.';
      return;
    }
    startAutoDomainFetch();
  }catch(e){
    toast('خطا در بررسی وضعیت توکن','err');
  }
}

async function submitAutoDomainToken(){
  const token = document.getElementById('auto-domain-token').value.trim();
  if(!token){ toast('توکن را وارد کن','err'); return; }
  document.getElementById('auto-domain-token-wrap').style.display = 'none';
  startAutoDomainFetch(token);
}

async function startAutoDomainFetch(token){
  const btn = document.getElementById('auto-domain-btn');
  const statusEl = document.getElementById('auto-domain-status');
  btn.disabled = true;
  btn.innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال دریافت...';
  statusEl.innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال دریافت دامنه از Railway...';

  try{
    const body = { mode: 'blacklist' };
    if(token) body.token = token;
    const r = await authF('/api/bot-tcp-proxy/start', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify(body)
    });
    if(!r.ok){
      const d = await r.json().catch(()=>({}));
      throw new Error(d.detail || 'خطا در شروع فرآیند');
    }
    autoDomainPolling = setInterval(pollAutoDomain, 1000);
  }catch(e){
    statusEl.innerHTML = '<i class="ti ti-alert-circle" style="color:var(--red-t)"></i>  '+esc(e.message);
    btn.disabled = false;
    btn.innerHTML = '<i class="ti ti-bolt"></i> دریافت دامنه';
  }
}

async function pollAutoDomain(){
  try{
    const r = await authF('/api/bot-tcp-proxy/status'), d = await r.json();
    const btn = document.getElementById('auto-domain-btn');
    const statusEl = document.getElementById('auto-domain-status');

    if(d.running){
      statusEl.innerHTML = `<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال جستجوی دامنه... (${d.attempts} تلاش)`;
      return;
    }

    clearInterval(autoDomainPolling);
    btn.disabled = false;
    btn.innerHTML = '<i class="ti ti-bolt"></i> دریافت خودکار دامنه';

    if(d.result){
      // پر کردن خودکار فیلدها بدون دخالت کاربر
      document.getElementById('nl-mtproto-domain').value = d.result.domain;
      document.getElementById('nl-mtproto-port').value = ''; // پورت داخلی همان پیش‌فرض می‌ماند؛ این پورت، پورت عمومی TCP است
      statusEl.innerHTML = `<i class="ti ti-circle-check" style="color:var(--green-t)"></i> دامنه دریافت شد: <b>${esc(d.result.domain)}:${d.result.port}</b>`;
      toast('دامنه و پورت خودکار دریافت شد ','ok');
    } else if(d.error){
      statusEl.innerHTML = '<i class="ti ti-alert-circle" style="color:var(--red-t)"></i>  '+esc(d.error);
      toast(' '+d.error,'err');
    }
  }catch(e){}
}

function openDomainScanModal(){
  dsDomains = [];
  dsRenderChips();
  document.getElementById('ds-token-section').style.display = '';
  openModal('modal-domain-scan');
  authF('/api/bot-tcp-proxy/status').then(r=>r.json()).then(d=>{
    if(d.has_token) document.getElementById('ds-token-section').style.display = 'none';
  }).catch(()=>{});
}
async function autoAssignMtprotoDomain(){
  const btn = document.getElementById('auto-domain-btn');
  const statusEl = document.getElementById('auto-domain-status');
  btn.disabled = true;
  btn.innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال دریافت...';
  statusEl.innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال اتصال به Railway و دریافت دامنه...';

  try{
    const r = await authF('/api/bot-tcp-proxy/start', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ mode:'blacklist' }) // توکن ذخیره‌شده خودکار استفاده می‌شود
    });
    if(!r.ok){
      const d = await r.json().catch(()=>({}));
      throw new Error(d.detail || 'خطا در شروع فرآیند');
    }
    autoDomainPolling = setInterval(pollAutoDomain, 1200);
  }catch(e){
    statusEl.innerHTML = '<i class="ti ti-alert-circle" style="color:var(--red-t)"></i>  '+e.message;
    btn.disabled = false;
    btn.innerHTML = '<i class="ti ti-bolt"></i> دریافت خودکار دامنه';
  }
}


function dsAddDomain(){
  const inp = document.getElementById('ds-domain-inp');
  const v = inp.value.trim().toLowerCase().replace(/\.$/, '');
  if(v && !dsDomains.includes(v)) dsDomains.push(v);
  inp.value = '';
  document.querySelectorAll('#modal-domain-scan .cm-opt').forEach(o=>o.classList.remove('sel')); // جدید
  dsRenderChips();
}
function dsRemoveDomain(d){
  dsDomains = dsDomains.filter(x=>x!==d);
  dsRenderChips();
}
function dsRenderChips(){
  document.getElementById('ds-domain-chips').innerHTML = dsDomains.map(d=>
    `<span class="cm-pill active" style="cursor:pointer" onclick="dsRemoveDomain('${d}')">${d} <i class="ti ti-x" style="font-size:10px"></i></span>`
  ).join('') || '<span style="font-size:10.5px;color:var(--t3)">هنوز دامنه‌ای اضافه نشده</span>';
}
async function startDomainScan(){
  if(!dsDomains.length){ toast('حداقل یک دامنه اضافه کن','err'); return; }
  const tokenField = document.getElementById('ds-token');
  const tokenSection=document.getElementById('ds-token-section');
  const token = tokenSection && tokenSection.style.display !== 'none' ? tokenField.value.trim() : '';
  const btn = document.getElementById('ds-start-btn');
  btn.disabled = true; btn.innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال اجرا...';
  document.getElementById('ds-log-box').style.display = 'block';
  try{
    const r = await authF('/api/bot-tcp-proxy/start', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ token, mode:'whitelist', target_domains: dsDomains })
    });
    if(!r.ok){ const d = await r.json().catch(()=>({})); throw new Error(d.detail || 'خطا'); }
    document.getElementById('ds-stop-btn').style.display = 'flex';
    dsPolling = setInterval(pollDomainScan, 1500);
  }catch(e){
    toast(' '+e.message,'err');
    btn.disabled = false; btn.innerHTML = '<i class="ti ti-player-play"></i> شروع اسکن';
  }
}
async function stopDomainScan(){
  await authF('/api/bot-tcp-proxy/stop', {method:'POST'});
  toast('درخواست توقف ارسال شد','ok');
}
async function pollDomainScan(){
  try{
    const r = await authF('/api/bot-tcp-proxy/status'), d = await r.json();
    const box = document.getElementById('ds-log-box');
    box.innerHTML = (d.logs||[]).map(l=>`<p class="upd-log-line">[${new Date(l.time*1000).toLocaleTimeString('fa-IR')}] ${esc(l.msg)}</p>`).join('') || '<p class="upd-log-empty">لاگی موجود نیست</p>';
    box.scrollTop = box.scrollHeight;
    const txt = document.getElementById('ds-status-text');
    if(d.running){
      txt.textContent = `در حال جستجو... (${d.attempts} تلاش)`;
    } else {
      clearInterval(dsPolling);
      document.getElementById('ds-stop-btn').style.display = 'none';
      const btn = document.getElementById('ds-start-btn');
      btn.disabled = false; btn.innerHTML = '<i class="ti ti-player-play"></i> شروع اسکن';
      if(d.result){
        txt.textContent = `پیدا شد: ${d.result.domain}:${d.result.port}`;
        toast('دامنه پیدا شد: '+d.result.domain+':'+d.result.port,'ok');
      } else if(d.error){
        txt.textContent = d.error;
      }
    }
  }catch(e){}
}
let btpForcedDomain = null;

function btpSelectIsp(domain, optId){
  btpForcedDomain = domain; // null یعنی حالت اسکن خودکار قبلی
  document.querySelectorAll('#modal-bot-tcp-proxy .cm-pill,#modal-bot-tcp-proxy .cm-opt').forEach(o=>o.classList.remove('active','sel'));
  const opt=document.getElementById(optId); if(opt) opt.classList.add('active','sel');
}
</script>
</body></html>"""


def get_public_page_html(uuid_key: str) -> str:
    """صفحه پابلیک ساب v3 — طراحی حرفه‌ای‌تر: لینک کانفیگ پنهان با دکمه نمایش، صفحه‌ی رمز با طراحی ویژه"""
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>OXNET Sub · oxnet</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{
  --bg:#060a14;--bg2:#0a1020;--bg3:#0d1428;
  --card:#0c1326;--card-b:rgba(96,148,246,0.12);--card-bh:rgba(96,148,246,0.28);
  --accent:#3B7CF6;--accent2:#6EA3FF;--accent-d:rgba(59,124,246,0.1);
  --green:#1FB87E;--green-bg:rgba(31,184,126,0.1);--green-t:#3FD79C;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#FB8585;
  --amber:#F2A33D;--amber-bg:rgba(242,163,61,0.1);--amber-t:#F9C988;
  --purple:#9D7BF0;--purple-bg:rgba(157,123,240,0.1);--purple-t:#BCA4F7;
  --t1:#EFF4FF;--t2:#8AA0C4;--t3:#48577A;
  --radius:18px;--shadow:0 12px 40px rgba(0,0,0,0.45);
  --serif:'Vazirmatn',sans-serif;
}}
[data-theme="dark"]{{
  --bg:#F0F3FA;--bg2:#E5ECF8;--bg3:#D9E3F4;
  --card:#FFFFFF;--card-b:rgba(59,124,246,0.14);--card-bh:rgba(59,124,246,0.32);
  --accent:#2E63D6;--accent2:#1E4CB8;--accent-d:rgba(46,99,214,0.08);
  --green:#0E9A6A;--green-bg:rgba(14,154,106,0.08);--green-t:#0A7553;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#A51E1E;
  --amber:#C97A12;--amber-bg:rgba(201,122,18,0.08);--amber-t:#8F5A0C;
  --purple:#7350D6;--purple-bg:rgba(115,80,214,0.08);--purple-t:#5A3CAD;
  --t1:#101A30;--t2:#48577A;--t3:#8694B0;
  --shadow:0 12px 36px rgba(20,40,90,0.12);
}}
html,body{{min-height:100%;background:var(--bg);font-family:var(--serif);color:var(--t1);font-size:14px;transition:background .35s,color .35s}}
.bg-fx{{position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(59,124,246,0.13),transparent 62%),var(--bg);z-index:0;pointer-events:none;transition:background .35s}}
.grid-fx{{position:fixed;inset:0;background-image:linear-gradient(rgba(96,148,246,0.025) 1px,transparent 1px),linear-gradient(90deg,rgba(96,148,246,0.025) 1px,transparent 1px);background-size:46px 46px;z-index:0;pointer-events:none}}
.wrap{{position:relative;z-index:10;max-width:800px;margin:0 auto;padding:24px 16px 64px}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:26px;gap:10px}}
.brand{{display:flex;align-items:center;gap:11px;min-width:0}}
.brand-img{{width:40px;height:40px;border-radius:12px;overflow:hidden;border:1px solid var(--card-b);box-shadow:0 0 0 1px rgba(255,255,255,.02);flex-shrink:0}}
.brand-img img{{width:100%;height:100%;object-fit:cover}}
.brand-name{{font-size:14.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em}}
.brand-sub{{font-size:9.5px;color:var(--t3);font-weight:500}}
.top-actions{{display:flex;align-items:center;gap:6px;flex-shrink:0}}
.icon-btn{{width:36px;height:36px;border-radius:11px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;transition:.18s}}
.icon-btn:hover{{background:var(--accent-d);color:var(--accent2);border-color:var(--card-bh)}}

.sub-info{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px 24px 22px;margin-bottom:16px;box-shadow:var(--shadow);position:relative;overflow:hidden}}
.sub-info::before{{content:'';position:absolute;top:0;right:0;width:160px;height:160px;background:radial-gradient(circle at top right,rgba(59,124,246,.1),transparent 70%);pointer-events:none}}
.sub-eyebrow{{font-size:10px;font-weight:700;color:var(--accent2);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.sub-eyebrow i{{font-size:13px}}
.sub-name{{font-size:23px;font-weight:800;color:var(--t1);margin-bottom:6px;letter-spacing:-.02em}}
.sub-desc{{font-size:12.5px;color:var(--t2);line-height:1.8;margin-bottom:14px}}
.sub-meta-row{{font-size:10.5px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:6px}}
.sub-sub-box{{background:var(--accent-d);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;display:flex;align-items:center;gap:9px;flex-wrap:wrap}}
.sub-sub-url{{font-family:ui-monospace,monospace;font-size:10px;color:var(--accent2);word-break:break-all;flex:1;min-width:140px}}

.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}}
.stat-card{{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 17px;transition:.2s}}
.stat-card:hover{{border-color:var(--card-bh);transform:translateY(-1px)}}
.stat-label{{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:7px}}
.stat-val{{font-size:22px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.01em}}
.stat-sub{{font-size:9.5px;color:var(--t3);margin-top:6px}}

.copy-all-bar{{display:flex;align-items:center;gap:12px;background:linear-gradient(120deg,var(--accent) 0%,#2952C8 100%);border-radius:18px;padding:16px 19px;margin-bottom:18px;box-shadow:0 10px 30px rgba(59,124,246,.28);flex-wrap:wrap}}
.copy-all-text{{flex:1;min-width:160px}}
.copy-all-title{{font-size:13.5px;font-weight:800;color:#fff;display:flex;align-items:center;gap:6px}}
.copy-all-sub{{font-size:10px;color:rgba(255,255,255,.78);margin-top:3px}}
.copy-all-btn{{background:#fff;color:#1D4ED8;border:none;border-radius:12px;padding:10px 19px;font-family:inherit;font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.18s;white-space:nowrap}}
.copy-all-btn:hover{{transform:translateY(-1px);box-shadow:0 6px 16px rgba(0,0,0,.22)}}
.copy-all-btn:active{{transform:translateY(0) scale(.98)}}

.cfg-title{{font-size:12px;font-weight:800;color:var(--t2);margin-bottom:13px;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.07em}}
.cfg-title i{{color:var(--accent);font-size:15px}}
.cfg-grid{{display:grid;gap:13px}}


/* ── کارت کانفیگ به‌شکل بلیط دسترسی (signature element) ── */
.cfg-card{{background:var(--card);border:1px solid var(--card-b);border-radius:18px;transition:all .2s;position:relative;overflow:hidden}}
.cfg-card:hover{{border-color:var(--card-bh);box-shadow:var(--shadow)}}
.cfg-top{{padding:17px 19px 15px;position:relative}}
.cfg-top::after{{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-top::after{{background:var(--red)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;flex-wrap:wrap}}
.cfg-label{{font-size:14.5px;font-weight:700;color:var(--t1)}}
.cfg-badges{{display:flex;gap:5px;flex-wrap:wrap;margin-top:6px}}
.proto-chip{{font-size:9px;padding:3px 8px;border-radius:7px;font-weight:800;letter-spacing:.02em}}
.pc-ws{{background:var(--accent-d);color:var(--accent2)}}
.pc-trojan{{background:var(--purple-bg);color:#A78BFA}}
.pc-xhttp{{background:var(--purple-bg);color:var(--purple-t)}}
.pc-ultra{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status{{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;padding:4px 10px;border-radius:20px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red-t)}}
.cfg-usage{{margin-bottom:4px}}
.ubar{{height:6px;border-radius:4px;background:rgba(96,148,246,0.1);overflow:hidden;margin-bottom:5px}}
.ubar-f{{height:100%;border-radius:4px;transition:width .5s ease}}
.utxt{{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}}

/* خط جداکننده‌ی بلیطی با دندانه‌های گرد، شبیه پاره‌خط بُرد بلیط */
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 19px}}
.cfg-tear::before,.cfg-tear::after{{content:'';position:absolute;top:50%;width:18px;height:18px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-b)}}
.cfg-tear::before{{right:-28px}}
.cfg-tear::after{{left:-28px}}

.cfg-bottom{{padding:15px 19px 18px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px dashed var(--card-b);border-radius:11px;padding:10px 13px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:11.5px;font-weight:600;transition:.15s}}
.cfg-link-toggle:hover{{background:var(--accent-d);border-color:var(--card-bh);color:var(--accent2)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:10px;padding:11px 13px;font-size:9.8px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.7;margin-top:9px;max-height:90px;overflow-y:auto}}
[data-theme="dark"] .cfg-vless{{background:rgba(46,99,214,.05)}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap;margin-top:11px}}
.btn{{font-family:inherit;font-size:11.5px;font-weight:700;border-radius:10px;padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-p{{background:var(--accent);color:#fff;box-shadow:0 3px 12px rgba(59,124,246,.3)}}
.btn-p:hover{{background:var(--accent2)}}
.btn-g{{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(96,148,246,.16)}}
.btn-g:hover{{background:rgba(96,148,246,.2)}}
.btn-pur{{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(157,123,240,.2)}}
.btn-pur:hover{{background:rgba(157,123,240,.22)}}
.conn-chip{{display:inline-flex;align-items:center;gap:4px;font-size:9.5px;padding:3px 8px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-weight:700}}
.dot{{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}

/* ── صفحه‌ی قفل / رمز ── */
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:78vh;padding:20px 0}}
.lock-card{{background:var(--card);border:1px solid var(--card-b);border-radius:26px;padding:0;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow);overflow:hidden;position:relative}}
.lock-banner{{background:linear-gradient(150deg,rgba(59,124,246,.16),rgba(59,124,246,.02) 70%);padding:38px 30px 26px;position:relative}}
.lock-shield{{width:64px;height:64px;border-radius:18px;background:var(--accent-d);border:1px solid var(--card-bh);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-7px;border-radius:22px;border:1px solid var(--card-b);animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.5}}50%{{transform:scale(1.08);opacity:0}}}}
.lock-shield i{{font-size:28px;color:var(--accent2)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px;color:var(--t1);letter-spacing:-.01em}}
.lock-sub{{font-size:12px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:24px 30px 30px}}
.lock-field{{position:relative;margin-bottom:13px}}
.lock-inp{{width:100%;padding:13px 44px 13px 44px;border-radius:13px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.14em;transition:.18s}}
[data-theme="dark"] .lock-inp{{background:rgba(46,99,214,.04)}}
.lock-inp:focus{{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}}
.lock-eye{{position:absolute;left:13px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--accent2)}}
.lock-lockicon{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:11.5px;margin-bottom:10px;min-height:16px;display:flex;align-items:center;justify-content:center;gap:5px}}
.lock-btn{{width:100%;justify-content:center;padding:13px;font-size:13px;border-radius:13px}}
.lock-footer{{padding:14px 30px;border-top:1px solid var(--card-b);font-size:10px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}}

.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:38px;display:block;margin-bottom:14px}}

.toast{{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:12px;padding:10px 20px;font-size:12.5px;font-weight:600;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow);white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(31,184,126,.35);background:var(--green-bg);color:var(--green-t)}}

.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.72);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow)}}
.qr-title{{font-size:13.5px;font-weight:800;margin-bottom:16px;color:var(--t1)}}
.qr-img{{border-radius:14px;overflow:hidden;margin-bottom:15px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:10px;border-radius:14px}}

.footer{{text-align:center;padding-top:28px;font-size:10.5px;color:var(--t3)}}
.footer a{{color:var(--accent2);font-weight:700}}

@media(max-width:520px){{
  .stats-bar{{grid-template-columns:1fr 1fr}}
  .stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}
  .sub-name{{font-size:19px}}
  .copy-all-bar{{flex-direction:column;align-items:stretch}}
  .copy-all-btn{{justify-content:center}}
  .wrap{{padding:16px 12px 50px}}
  .lock-banner{{padding:32px 22px 22px}}
  .lock-form{{padding:20px 22px 26px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}



</style>
</head>
<body>
<div class="bg-fx"></div><div class="grid-fx"></div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-mark">OX</div>
      <div><div class="brand-name">oxnet</div><div class="brand-sub">OXNET · v1.2.1</div></div>
    </div>
    <div class="top-actions">
      <button class="icon-btn" id="theme-toggle" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-sun" id="theme-icon"></i></button>
      <a class="icon-btn" href="https://t.me/oxnet_ir" target="_blank" title="کانال تلگرام"><i class="ti ti-brand-telegram"></i></a>
    </div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
  </div>
  <div class="footer">OXNET v1.2.1</div>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';

let isDark=localStorage.getItem('oxnet-pub-theme')==='dark';
function applyTheme(dark){{
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  document.getElementById('theme-icon').className='ti '+(dark?'ti-sun':'ti-moon');
}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('oxnet-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);

function toast(msg,type=''){{
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}}
function protoChip(p){{
  if(p==='xhttp-stream-one')return '<span class="proto-chip pc-xh"><i class="ti ti-bolt"></i> XHTTP Stream</span>';
  if(p&&p.startsWith('trojan'))return '<span class="proto-chip pc-trojan"><i class="ti ti-shield-lock"></i> '+esc(p)+'</span>';
  if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp">'+esc(p)+'</span>';
  return '<span class="proto-chip pc-ws">VLESS · WS</span>';
}}

function showQR(label,link){{
  document.getElementById('qr-label').textContent=label;
  document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);
  document.getElementById('qr-modal').classList.add('open');
}}

function toggleLink(i){{
  const wrap=document.getElementById('vw-'+i);
  const btn=document.getElementById('vt-'+i);
  const open=wrap.classList.toggle('open');
  btn.classList.toggle('open',open);
  btn.querySelector('.ltl span').textContent = open ? 'پنهان کردن لینک' : 'نمایش لینک کانفیگ';
}}

async function loadData(pw=''){{
  const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');
  const r=await fetch(url);
  return r.json();
}}

function renderLock(name,errMsg=''){{
  document.getElementById('root').innerHTML=`
    <div class="lock-stage">
      <div class="lock-card">
        <div class="lock-banner">
          <div class="lock-shield"><i class="ti ti-shield-lock"></i></div>
          <div class="lock-title">${{esc(name)}}</div>
          <div class="lock-sub">این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز رو وارد کنید.</div>
        </div>
        <div class="lock-form">
          <div class="lock-err" id="lock-err">${{errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : ''}}</div>
          <div class="lock-field">
            <i class="ti ti-lock lock-lockicon"></i>
            <input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus>
            <button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button>
          </div>
          <button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود به گروه</button>
        </div>
        <div class="lock-footer"><i class="ti ti-shield-check"></i> اتصال شما رمزنگاری‌شده است</div>
      </div>
    </div>
  `;
  const inp=document.getElementById('lock-pw');
  inp.addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock()}});
}}

function togglePwVis(){{
  const inp=document.getElementById('lock-pw');
  const icon=document.getElementById('lock-eye-icon');
  const toText = inp.type==='password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti '+(toText ? 'ti-eye-off' : 'ti-eye');
}}

async function submitLock(){{
  const pw=document.getElementById('lock-pw').value;
  const data=await loadData(pw);
  if(data.locked){{renderLock(data.name,'رمز اشتباه است');return}}
  savedPw=pw;
  renderContent(data);
}}

function renderContent(d){{
  const activeCount=d.links.filter(l=>l.active).length;
  const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/sub-group/' + UUID_KEY);
  const subUrl = baseSubUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');

  window._oxnetSubUrl  = subUrl;
  window._oxnetSubName = d.name;
  window._oxnetLinks   = d.links.map(l => ({{
    vless : l.vless_link,
    sub   : l.sub_url + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : ''),
    label : l.label,
  }}));

  document.getElementById('root').innerHTML=`
    <div class="sub-info">
      <div class="sub-eyebrow"><i class="ti ti-folders"></i> گروه دسترسی</div>
      <div class="sub-name">${{esc(d.name)}}</div>
      ${{d.desc ? `<div class="sub-desc">${{esc(d.desc)}}</div>` : ''}}
      <div class="sub-meta-row"><i class="ti ti-clock"></i> آخرین بروزرسانی: ${{new Date().toLocaleTimeString('fa-IR')}}</div>
      <div class="sub-sub-box">
        <span class="sub-sub-url">${{esc(subUrl)}}</span>
        <button class="btn btn-pur" style="padding:7px 12px;font-size:10.5px"
          onclick="navigator.clipboard.writeText(window._oxnetSubUrl).then(()=>toast('لینک ساب کپی شد ','ok'))">
          <i class="ti ti-copy"></i> کپی لینک ساب
        </button>
        <button class="btn btn-g" style="padding:7px 12px;font-size:10.5px"
          onclick="showQR(window._oxnetSubName + ' — کل گروه', window._oxnetSubUrl)">
          <i class="ti ti-qrcode"></i> QR کل
        </button>
      </div>
    </div>

    <div class="copy-all-bar">
      <div class="copy-all-text">
        <div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه‌ی کانفیگ‌ها</div>
        <div class="copy-all-sub">تمام لینک‌های فعال این گروه را یک‌جا کپی کن</div>
      </div>
      <button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> کپی همه (${{toFa(activeCount)}})</button>
    </div>

    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-label">کانفیگ‌های فعال</div>
        <div class="stat-val">${{toFa(activeCount)}}</div>
        <div class="stat-sub">از ${{toFa(d.links.length)}} کانفیگ</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">اتصالات زنده</div>
        <div class="stat-val">${{toFa(d.active_connections)}}</div>
        <div class="stat-sub" style="color:var(--green-t);display:flex;align-items:center;gap:4px"><span class="dot"></span> آنلاین</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">کل مصرف</div>
        <div class="stat-val" style="font-size:17px;margin-top:3px">${{esc(d.total_used_fmt)}}</div>
        <div class="stat-sub">همه کانفیگ‌ها</div>
      </div>
    </div>

    <div class="cfg-title"><i class="ti ti-link"></i> کانفیگ‌ها (${{toFa(d.links.length)}} عدد)</div>
    <div class="cfg-grid">
      ${{d.links.map((l, i) => {{
        const pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
        const bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
        const lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
        return `
          <div class="cfg-card${{l.active ? '' : ' inactive'}}">
            <div class="cfg-top">
              <div class="cfg-head">
                <div>
                  <div class="cfg-label">${{esc(l.label)}}</div>
                  <div class="cfg-badges">
                    ${{protoChip(l.protocol)}}
                    ${{l.connections > 0 ? `<span class="conn-chip"><span class="dot"></span> ${{toFa(l.connections)}} اتصال</span>` : ''}}
                  </div>
                </div>
                <span class="cfg-status ${{l.active ? 'ok' : 'no'}}">${{l.active ? '<i class="ti ti-circle-check"></i> فعال' : '<i class="ti ti-circle-x"></i> غیرفعال'}}</span>
              </div>
              <div class="cfg-usage">
                <div class="ubar"><div class="ubar-f" style="width:${{pct}}%;background:${{bc}}"></div></div>
                <div class="utxt"><span>${{esc(l.used_fmt)}} مصرف شده</span><span>سهمیه: ${{lim}}</span></div>
              </div>
            </div>
            <div class="cfg-tear"></div>
            <div class="cfg-bottom">
              <button class="cfg-link-toggle" id="vt-${{i}}" onclick="toggleLink(${{i}})">
                <span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک کانفیگ</span></span>
                <i class="ti ti-chevron-down"></i>
              </button>
              <div class="cfg-vless-wrap" id="vw-${{i}}">
                <div class="cfg-vless-inner">
                  <div class="cfg-vless">${{esc(l.vless_link)}}</div>
                </div>
              </div>
              <div class="cfg-actions">
                <button class="btn btn-p"
                  onclick="navigator.clipboard.writeText(window._oxnetLinks[${{i}}].vless).then(()=>toast('لینک کپی شد ','ok'))">
                  <i class="ti ti-copy"></i> کپی لینک
                </button>
                <button class="btn btn-g"
                  onclick="showQR(window._oxnetLinks[${{i}}].label, window._oxnetLinks[${{i}}].vless)">
                  <i class="ti ti-qrcode"></i> QR
                </button>
              </div>
            </div>
          </div>
        `;
      }}).join('')}}
    </div>
  `;
  setTimeout(() => autoRefresh(), 30000);
}}

function copyAllConfigs(){{
  const links=window._oxnetLinks||[];
  if(!links.length){{toast('کانفیگی برای کپی نیست','');return}}
  const text=links.map(l=>l.vless).join('\\n');
  navigator.clipboard.writeText(text).then(()=>toast('همه‌ی '+toFa(links.length)+' کانفیگ کپی شد ','ok'));
}}

async function autoRefresh(){{
  try{{
    const data = await loadData(savedPw);
    if (!data.locked) renderContent(data);
  }} catch(e) {{}}
}}

async function init(){{
  try{{
    const data = await loadData();
    if (data.locked) {{ renderLock(data.name); return; }}
    renderContent(data);
  }} catch(e) {{
    document.getElementById('root').innerHTML =
      '<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری</div>';
  }}
}}

init();
</script>
</body></html>"""
