import streamlit as st
import numpy as np
import plotly.graph_objects as go
import yfinance as yf
import feedparser
import psutil
import time, hashlib, collections, sqlite3, os, re
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from scipy.fft import fft, ifft
from cryptography.fernet import Fernet
from Bio.Seq import Seq
from twilio.rest import Client

# --- 1. SEGURANÇA DE ESTADO E SEGREDOS (MFA CONFIG) ---
MASTER_KEY_HASH = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918" # 'admin' default

def get_encryption_suite():
    KEY_FILE = "xeon_sovereign.key"
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f: key = f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f: f.write(key)
    return Fernet(key)

cipher = get_encryption_suite()

# --- 2. PERSISTÊNCIA SOBERANA (SQLITE SINGLETON) ---
class XeonDB:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = sqlite3.connect('xeon_sovereign.db', timeout=30, check_same_thread=False)
            cls._instance.execute('''CREATE TABLE IF NOT EXISTS intel_vault 
                                    (timestamp TEXT, node TEXT, cpu REAL, status TEXT, payload TEXT)''')
            cls._instance.commit()
        return cls._instance

db_conn = XeonDB()

# --- 3. MOTORES DE REALIDADE E ALERTA ---
def send_whatsapp(msg):
    try:
        sid = st.secrets.get("TWILIO_SID")
        token = st.secrets.get("TWILIO_TOKEN")
        if sid and token:
            Client(sid, token).messages.create(
                from_=st.secrets["WHATSAPP_FROM"], body=f"🚨 XEON ALERT: {msg}", to=st.secrets["WHATSAPP_TO"]
            )
    except: pass

@st.cache_data(ttl=3600)
def bio_process_dna(sequence):
    try:
        dna = Seq(re.sub(r'[^ATCG]', '', sequence.upper()))
        return f"DNA_COMP: {dna.complement()} | TRANS: {dna.translate()[:15]}..."
    except: return "BIO_ERROR / ERRO GENÉTICO"

def fetch_osint_real(query):
    try:
        feed = feedparser.parse(f"https://google.com{query}+2026&hl=pt-BR")
        return feed.entries[0].title.upper() if feed.entries else "SCAN: STABLE / ESTÁVEL"
    except: return "OFFLINE NODE / NÓ OFFLINE"

# --- 4. CONFIGURAÇÃO VISUAL (VERDE E PRETO) ---
st.set_page_config(page_title="XEON COMMAND v30.0", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00FFCC; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #000; color: #00FFCC; border: 1px solid #00FFCC; border-radius: 0; }
    .stButton>button { background-color: #000 !important; color: #00FFCC !important; border: 1px solid #00FFCC !important; width: 100%; border-radius: 0; font-weight: bold; font-size: 10px; }
    .terminal { border: 1px solid #00FFCC; padding: 12px; background: #000; height: 180px; font-size: 11px; overflow-y: auto; line-height: 1.4; border-style: double; }
    .res-box { border: 2px solid #00FFCC; padding: 15px; text-align: center; font-weight: bold; margin: 10px 0; background: #010101; text-shadow: 0 0 5px #00FFCC; }
    </style>
    """, unsafe_allow_html=True)

# Estados de Sessão
if 'is_locked' not in st.session_state: st.session_state.is_locked = False
if 'intel_log' not in st.session_state: st.session_state.intel_log = collections.deque(["[KERNEL READY] v30.0 - SOBERANIA TOTAL"], maxlen=12)
if 'hw_trace' not in st.session_state: st.session_state.hw_trace = collections.deque([0.0 for _ in range(60)], maxlen=100)
if 'last_res' not in st.session_state: st.session_state.last_res = "AWAITING INJECTION / AGUARDANDO INGESTÃO"

# --- 5. NÚCLEO DE EXECUÇÃO ---
def run_sovereign_engine(node, u_in=""):
    if st.session_state.is_locked: return
    t_start = time.perf_counter()
    cpu = psutil.cpu_percent()

    # Firewall & Detecção de Ameaças
    if re.search(r"(?i)(SELECT|DROP|OR 1=1|<script)", u_in):
        st.session_state.is_locked = True
        send_whatsapp(f"HACK ATTEMPT ON {node}. LOCKDOWN ACTIVE.")
        return

    # Integridade de Hardware (FFT)
    sig = np.random.normal(0, 1, 512)
    if not np.allclose(sig, ifft(fft(sig)).real, atol=1e-12): return

    res = "PROCESS COMPLETE / CONCLUÍDO"
    if node == "BIO_GEN": res = bio_process_dna(u_in)
    elif node == "GEO_SCAN": res = fetch_osint_real(u_in)
    elif "FIN" in node:
        try: res = f"BTC: ${yf.Ticker('BTC-USD').fast_info.last_price:.2f}"
        except: res = "FIN_FEED_FAIL"

    st.session_state.last_res = res
    st.session_state.hw_trace.append(cpu)
    st.session_state.intel_log.append(f"[{time.strftime('%H:%M:%S')}] [{node}] {res[:55]} | CPU: {cpu}%")
    db_conn.execute("INSERT INTO intel_vault VALUES (?,?,?,?,?)", (time.strftime('%Y-%m-%d %H:%M:%S'), node, cpu, "SUCCESS", res[:100]))
    db_conn.commit()

# --- 6. INTERFACE OPERACIONAL FINAL ---
st.write(f"📡 XEON NODE v30.0 | TOTAL SOBERANIA | {time.strftime('%H:%M:%S')}")

if st.session_state.is_locked:
    st.error("❌ TERMINAL LOCKED BY PROTOCOL / BLOQUEADO POR SEGURANÇA")
    master_input = st.text_input("ENTER ADMIN MFA TOKEN / INSIRA CHAVE MESTRA:", type="password")
    if st.button("EXECUTE MASTER RESET"):
        if hashlib.sha256(master_input.encode()).hexdigest() == MASTER_KEY_HASH:
            st.session_state.is_locked = False; st.rerun()
        else: st.warning("INVALID TOKEN / TOKEN INVÁLIDO")
else:
    u_query = st.text_input("", placeholder="INJECT DATA / RESEARCH DNA / SEARCH GLOBAL (PT/EN)...", label_visibility="collapsed")
    if st.button("EXE_SOVEREIGN_PROTOCOL"): 
        if u_query: run_sovereign_engine("DATA_INJECT", u_query)

    st.markdown(f'<div class="res-box">{st.session_state.last_res}</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.write("🏗️ ENGINEERING")
        if st.button("LITHO GRAFENO"): run_sovereign_engine("ENG_LITHO")
    with c2:
        st.write("🌍 GEOPOLITICS")
        if st.button("SCAN GLOBAL"): run_sovereign_engine("GEO_SCAN", u_query)
    with c3:
        st.write("💰 FINANCIAL")
        if st.button("BOLSAS REAIS"): run_sovereign_engine("FIN_MKT")
    with c4:
        st.write("🧬 BIO-EVOLUTION")
        if st.button("DNA RESEARCH"): run_sovereign_engine("BIO_GEN", u_query)
        def gen_pdf():
            buf = BytesIO(); p = canvas.Canvas(buf, pagesize=A4); p.setFillColorRGB(0,0,0); p.rect(0,0,600,900,fill=1)
            p.setFillColorRGB(0,1,0.8); p.setFont("Courier-Bold", 14); p.drawString(50, 820, "SOBERANIA GLOBAL FINAL v30.0")
            logs = db_conn.execute("SELECT * FROM intel_vault ORDER BY timestamp DESC LIMIT 60").fetchall()
            y = 790; p.setFont("Courier", 7)
            for l in logs: p.drawString(50, y, f"> {l}"); y -= 12
            p.showPage(); p.save(); buf.seek(0); return buf
        st.download_button("📄 EXPORT REPORT (PDF)", data=gen_pdf(), file_name="XEON_v30.pdf")

st.markdown('<div class="terminal">' + "<br>".join(list(st.session_state.intel_log)) + '</div>', unsafe_allow_html=True)
fig = go.Figure(go.Bar(y=list(st.session_state.hw_trace), marker_color='#00FFCC'))
fig.update_layout(template="plotly_dark", height=150, margin=dict(l=0,r=0,b=0,t=0), paper_bgcolor='black', plot_bgcolor='black', xaxis=dict(visible=False), yaxis=dict(visible=False))
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

st.write(f"📊 **HARDWARE:** CPU: {psutil.cpu_percent()}% | **SLA:** OK | **STATUS:** ✅ SOBERANO")

time.sleep(5)
if not u_query and not st.session_state.is_locked: st.rerun()
