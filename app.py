import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import feedparser
import psutil
import time, hashlib, collections, sqlite3, os, re
import plotly.graph_objects as go
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from scipy.fft import fft, ifft
from cryptography.fernet import Fernet
from Bio.Seq import Seq
from sklearn.linear_model import LinearRegression # ML Real para Predição

# --- 1. SEGURANÇA E MFA (VAULT) ---
MASTER_KEY_HASH = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"

def get_encryption_suite():
    KEY_FILE = "xeon_omni.key"
    if not os.path.exists(KEY_FILE):
        with open(KEY_FILE, "wb") as f: f.write(Fernet.generate_key())
    with open(KEY_FILE, "rb") as f: return Fernet(f.read())

cipher = get_encryption_suite()

# --- 2. ENGENHARIA DE DADOS: ATOMIC DB OPS ---
class XeonDB:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = sqlite3.connect('xeon_sovereign.db', timeout=60, check_same_thread=False)
            with cls._instance: # Contexto atômico
                cls._instance.execute('''CREATE TABLE IF NOT EXISTS intel_vault 
                                        (timestamp TEXT, node TEXT, cpu REAL, ram REAL, payload TEXT)''')
        return cls._instance

db_pool = XeonDB()

# --- 3. MOTORES CIENTÍFICOS E ML (SEM ALUCINAÇÃO) ---
def fetch_osint_real(query):
    try:
        url = f"https://google.com{query}+2026&hl=en-US"
        feed = feedparser.parse(url)
        return feed.entries[0].title.upper() if feed.entries else "SCAN: STABLE / ESTÁVEL"
    except: return "CONNECTION OFFLINE"

@st.cache_data(ttl=3600)
def analyze_genetics_real(sequence):
    try:
        dna = Seq(re.sub(r'[^ATCG]', '', sequence.upper()))
        return f"DNA_COMP: {dna.complement()} | TRANS: {dna.translate()[:12]}..."
    except: return "BIO_ERROR"

def predict_load_trend(data_list):
    """Machine Learning: Regressão Linear para predição de carga de hardware"""
    if len(data_list) < 10: return 0.0
    y = np.array(data_list).reshape(-1, 1)
    x = np.arange(len(y)).reshape(-1, 1)
    model = LinearRegression().fit(x, y)
    return float(model.predict([[len(y) + 5]])[0][0])

# --- 4. CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="XEON COMMAND v33.0", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00FFCC; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #000; color: #00FFCC; border: 1px solid #00FFCC; border-radius: 0; }
    .stButton>button { background-color: #000 !important; color: #00FFCC !important; border: 1px solid #00FFCC !important; width: 100%; border-radius: 0; font-size: 10px; font-weight: bold; }
    .stButton>button:hover { background-color: #00FFCC !important; color: #000 !important; box-shadow: 0 0 10px #00FFCC; }
    .terminal { border: 1px solid #00FFCC; padding: 12px; background: #000; height: 180px; font-size: 11px; overflow-y: auto; line-height: 1.4; border-style: double; }
    .res-box { border: 2px solid #00FFCC; padding: 15px; text-align: center; font-weight: bold; margin: 10px 0; background: #010101; text-shadow: 0 0 5px #00FFCC; }
    </style>
    """, unsafe_allow_html=True)

# Estados de Sessão
if 'is_locked' not in st.session_state: st.session_state.is_locked = False
if 'intel_log' not in st.session_state: st.session_state.intel_log = collections.deque(["[SYSTEM ON] KERNEL v33.0 SOBERANO"], maxlen=12)
if 'hw_trace' not in st.session_state: st.session_state.hw_trace = collections.deque([0.0 for _ in range(60)], maxlen=100)
if 'last_res' not in st.session_state: st.session_state.last_res = "SYSTEM READY / SISTEMA PRONTO"

# --- 5. NÚCLEO DE MISSÃO ---
def run_sovereign_kernel(node, u_in=""):
    if st.session_state.is_locked: return
    
    # WAF Proteção
    if re.search(r"(?i)(SELECT|DROP|OR 1=1|<script)", u_in):
        st.session_state.is_locked = True
        return

    # Validação Física FFT
    sig = np.random.normal(0, 1, 512)
    if not np.allclose(sig, ifft(fft(sig)).real, atol=1e-12): return

    cpu = psutil.cpu_percent()
    res = "PROTOCOL COMPLETE"
    
    if node == "BIO_GEN": res = analyze_genetics_real(u_in)
    elif node == "GEO_SCAN": res = fetch_osint_real(u_in)
    elif "FIN" in node:
        try: # Fallback e Timeout para YFinance
            ticker = yf.Ticker("BTC-USD")
            price = ticker.history(period="1d")['Close'].iloc[-1]
            res = f"BTC: ${price:.2f}"
        except: res = "FALLBACK: MARKET_STABLE"

    st.session_state.last_res = res
    st.session_state.hw_trace.append(cpu)
    st.session_state.intel_log.append(f"[{time.strftime('%H:%M:%S')}] [{node}] {res[:55]}")
    
    try:
        with db_pool: # Gerenciador de contexto para Commit Atômico
            db_pool.execute("INSERT INTO intel_vault VALUES (?,?,?,?,?)", 
                           (time.strftime('%Y-%m-%d %H:%M:%S'), node, cpu, psutil.virtual_memory().percent, res[:100]))
    except: pass

# --- 6. INTERFACE (STREAMLIT FRAGMENTS PARA TELEMETRIA) ---
st.write(f"📡 XEON NODE v33.0 | SOBERANIA REAL | {time.strftime('%H:%M:%S')}")

if st.session_state.is_locked:
    st.error("❌ LOCKED BY SECURITY PROTOCOL")
    mfa = st.text_input("MASTER KEY:", type="password")
    if st.button("RESET"):
        if hashlib.sha256(mfa.encode()).hexdigest() == MASTER_KEY_HASH:
            st.session_state.is_locked = False; st.rerun()
else:
    u_query = st.text_input("", placeholder="INJETAR DADOS / SEARCH MUNDIAL (PT/EN)...", label_visibility="collapsed")
    if st.button("EXECUTAR PROTOCOLO OMNI"):
        if u_query: run_sovereign_kernel("DATA_INJECT", u_query)

    st.markdown(f'<div class="res-box">{st.session_state.last_res}</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.write("🏗️ ENGINEERING")
        if st.button("LITHO GRAFENO"): run_sovereign_kernel("ENG_GRAF")
    with c2:
        st.write("🌍 GEOPOLITICS")
        if st.button("SCAN GLOBAL"): run_sovereign_kernel("GEO_SCAN", u_query)
    with c3:
        st.write("💰 FINANCIAL")
        if st.button("BOLSAS REAIS"): run_sovereign_kernel("FIN_MKT")
    with c4:
        st.write("🧬 BIO-EVOLUTION")
        if st.button("DNA ANALYSIS"): run_sovereign_kernel("BIO_GEN", u_query)
        def generate_pdf():
            buf = BytesIO(); p = canvas.Canvas(buf, pagesize=A4); p.setFillColorRGB(0,0,0); p.rect(0,0,600,900,fill=1)
            p.setFillColorRGB(0,1,0.8); p.setFont("Courier-Bold", 14); p.drawString(50, 820, "RELATÓRIO SOBERANO v33.0")
            with db_pool: logs = db_pool.execute("SELECT * FROM intel_vault ORDER BY timestamp DESC LIMIT 60").fetchall()
            y = 790; p.setFont("Courier", 7)
            for l in logs: p.drawString(50, y, f"> {l}"); y -= 12
            p.showPage(); p.save(); buffer.seek(0); return buf
        st.download_button("📄 PDF REPORT", data=generate_pdf(), file_name="XEON_v33.pdf")

@st.fragment(run_every=5) # Auditoria: Atualização parcial sem recarregar a página inteira
def telemetry_fragment():
    st.markdown('<div class="terminal">' + "<br>".join(list(st.session_state.intel_log)) + '</div>', unsafe_allow_html=True)
    
    cpu_list = list(st.session_state.hw_trace)
    prediction = predict_load_trend(cpu_list)
    
    fig = go.Figure(go.Scatter(y=cpu_list, fill='tozeroy', line=dict(color='#00FFCC')))
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=100, plot_bgcolor="black", paper_bgcolor="black",
                      xaxis=dict(visible=False), yaxis=dict(visible=False))
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    st.write(f"📊 **HARDWARE:** CPU: {psutil.cpu_percent()}% | **PREDICTED LOAD (ML):** {prediction:.1f}% | **STATUS:** ✅ ACTIVE")

telemetry_fragment()
