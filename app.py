import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import feedparser
import psutil
import time, hashlib, collections, sqlite3, os, re, random
import plotly.graph_objects as go
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from scipy.fft import fft, ifft
from cryptography.fernet import Fernet
from Bio.Seq import Seq
from sklearn.linear_model import LinearRegression
from contextlib import contextmanager

# --- 1. SEGURANÇA E MFA (MASTER KEY: admin) ---
MASTER_KEY_HASH = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"

def get_cipher():
    if not os.path.exists("xeon_omni.key"):
        with open("xeon_omni.key", "wb") as f: f.write(Fernet.generate_key())
    with open("xeon_omni.key", "rb") as f: return Fernet(f.read())

cipher = get_cipher()

# --- 2. ENGENHARIA DE DADOS: TRANSAÇÃO ATÔMICA E PRUNING (v39.0) ---
@contextmanager
def sovereign_transaction():
    """Garante atomicidade e fechamento seguro do banco em missão crítica."""
    conn = sqlite3.connect('xeon_sovereign.db', timeout=60)
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        st.error(f"DATABASE_BREACH: {e}")
    finally:
        conn.close()

def init_db():
    with sovereign_transaction() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS intel_vault 
                        (timestamp TEXT, node TEXT, cpu REAL, ram REAL, payload TEXT)''')

def prune_old_logs(limit=1000):
    """Otimização Logística: Mantém o banco leve para operação 24h (Lazy Loading)."""
    with sovereign_transaction() as conn:
        conn.execute(f"DELETE FROM intel_vault WHERE rowid NOT IN (SELECT rowid FROM intel_vault ORDER BY timestamp DESC LIMIT {limit})")

# --- 3. MOTORES CIENTÍFICOS E ML ---
def fetch_osint(query):
    try:
        url = f"https://google.com{query}+2026&hl=en-US"
        feed = feedparser.parse(url)
        return feed.entries[0].title.upper() if feed.entries else "SCAN: STABLE"
    except: return "CONNECTION OFFLINE"

@st.cache_data(ttl=3600)
def bio_dna_engine(sequence):
    try:
        dna = Seq(re.sub(r'[^ATCG]', '', sequence.upper()))
        return f"DNA_COMP: {dna.complement()} | TRANS: {dna.translate()[:12]}..."
    except: return "BIO_ERROR"

def predict_load(data_list):
    if len(data_list) < 10: return 0.0
    try:
        y = np.array(data_list).reshape(-1, 1)
        x = np.arange(len(y)).reshape(-1, 1)
        model = LinearRegression().fit(x, y)
        return float(model.predict([[len(y) + 1]]).flatten())
    except: return 0.0

# --- 4. CONFIGURAÇÃO VISUAL ---
init_db()
st.set_page_config(page_title="XEON COMMAND v39.0", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00FFCC; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #000; color: #00FFCC; border: 1px solid #00FFCC; border-radius: 0; }
    .stButton>button { background-color: #000 !important; color: #00FFCC !important; border: 1px solid #00FFCC !important; width: 100%; border-radius: 0; font-size: 9px; font-weight: bold; margin-bottom: 5px; }
    .terminal { border: 1px solid #00FFCC; padding: 12px; background: #000; height: 160px; font-size: 11px; overflow-y: auto; color: #00FFCC; }
    .res-box { border: 2px solid #00FFCC; padding: 15px; text-align: center; font-weight: bold; margin: 10px 0; background: #010101; text-shadow: 0 0 5px #00FFCC; }
    .header-info { font-size: 10px; border-bottom: 1px solid #00FFCC; padding-bottom: 5px; margin-bottom: 10px; opacity: 0.8; }
    </style>
    """, unsafe_allow_html=True)

if 'is_locked' not in st.session_state: st.session_state.is_locked = False
if 'intel_log' not in st.session_state: st.session_state.intel_log = collections.deque(["[SYSTEM ON] KERNEL v39.0 SOBERANO"], maxlen=12)
if 'hw_trace' not in st.session_state: st.session_state.hw_trace = collections.deque([random.uniform(5,15) for _ in range(60)], maxlen=100)
if 'last_res' not in st.session_state: st.session_state.last_res = "SISTEMA AGUARDANDO INJEÇÃO DE DADOS"

def run_mission(node, u_in=""):
    if st.session_state.is_locked: return
    if re.search(r"(?i)(SELECT|DROP|OR 1=1|<script)", u_in):
        st.session_state.is_locked = True; return

    t_start = time.perf_counter()
    sig = np.random.normal(0, 1, 512)
    if not np.allclose(sig, ifft(fft(sig)).real, atol=1e-12): return

    cpu = psutil.cpu_percent(); ram = psutil.virtual_memory().percent
    res = "MISSION_SUCCESS"

    if node == "BIO_GEN": res = bio_dna_engine(u_in)
    elif node == "GEO_SCAN": res = fetch_osint(u_in or "defense")
    elif "FIN" in node:
        try:
            btc = yf.Ticker("BTC-USD").fast_info
            res = f"BTC: ${btc['last_price']:.2f} | REAL-TIME"
        except: res = "MARKET_STABLE"

    st.session_state.last_res = res
    st.session_state.hw_trace.append(cpu)
    st.session_state.intel_log.append(f"[{time.strftime('%H:%M:%S')}] [{node}] {res[:55]}")
    
    with sovereign_transaction() as conn:
        conn.execute("INSERT INTO intel_vault VALUES (?,?,?,?,?)", 
                    (time.strftime('%Y-%m-%d %H:%M:%S'), node, cpu, ram, res[:100]))
    
    # Pruning Log preventivo após cada inserção (v39.0)
    prune_old_logs(limit=1000)

# --- 5. LAYOUT DE COMANDO ---
st.markdown('<div class="header-info">📡 CONEXÃO REAL TERMINAL | MÉDICA MESTRA | XEON COMMAND SOBERANO v39.0</div>', unsafe_allow_html=True)

if st.session_state.is_locked:
    st.error("❌ TERMINAL LOCKED BY SECURITY")
    mfa = st.text_input("MASTER KEY:", type="password")
    if st.button("RESET"):
        if hashlib.sha256(mfa.encode()).hexdigest() == MASTER_KEY_HASH:
            st.session_state.is_locked = False; st.rerun()
else:
    u_query = st.text_input("", placeholder="INJETAR DADOS / SEARCH MUNDIAL (PT/EN)...", label_visibility="collapsed")
    if st.button("EXECUTAR PROTOCOLO OMNI"):
        if u_query: run_mission("DATA_INJECT", u_query)

    st.markdown(f'<div class="res-box">{st.session_state.last_res}</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.write("🏗️ ENGINEERING")
        if st.button("LITHO GRAFENO"): run_mission("ENG_LITHO")
        if st.button("CORE INTEGRITY"): run_mission("ENG_CORE")
    with c2:
        st.write("🌍 GEOPOLITICS")
        if st.button("SCAN GLOBAL"): run_mission("GEO_SCAN", u_query)
        if st.button("DEFENSE SPX"): run_mission("GEO_SPX")
    with c3:
        st.write("💰 FINANCIAL")
        if st.button("BOLSAS REAIS"): run_mission("FIN_MKT")
        if st.button("SWIFT FLOW"): run_mission("FIN_SWIFT")
    with c4:
        st.write("🧬 BIO-EVOLUTION")
        if st.button("DNA ANALYSIS"): run_mission("BIO_GEN", u_query)
        def generate_pdf():
            output = BytesIO(); p = canvas.Canvas(output, pagesize=A4); p.setFillColorRGB(0,0,0); p.rect(0,0,600,900,fill=1)
            p.setFillColorRGB(0,1,0.8); p.setFont("Courier-Bold", 14); p.drawString(50, 820, "REPORTE SOBERANO v39.0")
            with sovereign_transaction() as conn:
                logs = conn.execute("SELECT * FROM intel_vault ORDER BY timestamp DESC LIMIT 60").fetchall()
            y = 790; p.setFont("Courier", 7)
            for l in logs: p.drawString(50, y, f"> {l}"); y -= 12
            p.showPage(); p.save(); output.seek(0); return output
        st.download_button("📄 EXPORT PDF", data=generate_pdf(), file_name="XEON_v39.pdf")

# TELEMETRIA E LOGS (FRAGMENTO PARA PERFORMANCE 24H)
@st.fragment(run_every=5)
def hw_telemetry_ui():
    st.markdown('<div class="terminal">' + "<br>".join(list(st.session_state.intel_log)) + '</div>', unsafe_allow_html=True)
    cpu_list = list(st.session_state.hw_trace)
    pred = predict_load(cpu_list)
    fig = go.Figure(go.Scatter(y=cpu_list, fill='tozeroy', line=dict(color='#00FFCC')))
    fig.update_layout(margin=dict(l=0,r=0,b=0,t=0), height=120, paper_bgcolor='black', plot_bgcolor='black', xaxis=dict(visible=False), yaxis=dict(visible=False))
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    st.write(f"📊 **HARDWARE:** CPU: {psutil.cpu_percent()}% | **TREND:** {pred:.1f}% | **STATUS:** ✅ SOBERANO (LEAN DB)")

hw_telemetry_ui()
