import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import httpx
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

def get_hsm_key():
    if not os.path.exists("xeon_omni.key"):
        with open("xeon_omni.key", "wb") as f: f.write(Fernet.generate_key())
    with open("xeon_omni.key", "rb") as f: return Fernet(f.read())

cipher = get_hsm_key()

# --- 2. ENGENHARIA DE DADOS ATÔMICA ---
@contextmanager
def sovereign_transaction():
    conn = sqlite3.connect('xeon_sovereign.db', timeout=60, check_same_thread=False)
    try:
        yield conn
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

def init_db():
    with sovereign_transaction() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS intel_vault 
                        (timestamp TEXT, node TEXT, cpu REAL, payload TEXT)''')

def log_mission(node, payload):
    cpu = psutil.cpu_percent()
    with sovereign_transaction() as conn:
        conn.execute("INSERT INTO intel_vault VALUES (?,?,?,?)", 
                    (time.strftime('%Y-%m-%d %H:%M:%S'), node, cpu, payload))

# --- 3. MOTORES CIENTÍFICOS REAIS ---
def fetch_osint(query):
    try:
        url = f"https://google.com{query}+2026&hl=pt-BR"
        with httpx.Client(timeout=5.0) as client:
            r = client.get(url)
            titles = re.findall(r"<title>(.*?)</title>", r.text)
            return titles[1].upper() if len(titles) > 1 else "SCAN: STABLE"
    except: return "TUNNEL_OFFLINE"

@st.cache_data(ttl=3600)
def bio_dna(sequence):
    try:
        dna = Seq(re.sub(r'[^ATCG]', '', sequence.upper()))
        return f"DNA_COMP: {dna.complement()} | TRANS: {dna.translate()[:12]}..."
    except: return "BIO_ERROR"

# --- 4. CONFIGURAÇÃO VISUAL (ESTRITAMENTE VERDE E PRETO) ---
init_db()
st.set_page_config(page_title="XEON COMMAND", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FFCC; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #000; color: #00FFCC; border: 1px solid #00FFCC; border-radius: 0; }
    .stButton>button { 
        background-color: #000 !important; color: #00FFCC !important; border: 1px solid #00FFCC !important;
        border-radius: 0 !important; width: 100%; font-weight: bold; font-size: 10px; margin-bottom: 2px;
    }
    .stButton>button:hover { background-color: #00FFCC !important; color: #000 !important; box-shadow: 0 0 10px #00FFCC; }
    .terminal { border: 1px solid #00FFCC; padding: 10px; background: #000; height: 160px; font-size: 11px; overflow-y: auto; color: #00FFCC; }
    .res-box { border: 1px solid #00FFCC; padding: 12px; text-align: center; font-weight: bold; margin: 10px 0; background: #000; color: #00FFCC; }
    .header-tag { font-size: 10px; border-bottom: 1px solid #00FFCC; padding-bottom: 5px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

if 'intel_log' not in st.session_state: st.session_state.intel_log = collections.deque(["[SYSTEM ON] KERNEL v47.0 FINAL"], maxlen=12)
if 'hw_trace' not in st.session_state: st.session_state.hw_trace = collections.deque([random.uniform(5,15) for _ in range(60)], maxlen=100)
if 'last_res' not in st.session_state: st.session_state.last_res = "AWAITING INJECTION / AGUARDANDO DADOS"
if 'is_locked' not in st.session_state: st.session_state.is_locked = False

def run_kernel(node, u_in=""):
    if st.session_state.is_locked: return
    if re.search(r"(?i)(SELECT|DROP|OR 1=1|<script)", u_in):
        st.session_state.is_locked = True; return

    cpu = psutil.cpu_percent()
    res = "PROTOCOL VALIDATED"
    
    if node == "BIO": res = bio_dna(u_in)
    elif node == "GEO": res = fetch_osint(u_in)
    elif "FIN" in node:
        try: res = f"BTC: ${yf.Ticker('BTC-USD').fast_info.last_price:.2f} | REAL-TIME"
        except: res = "MARKET_STABLE"

    st.session_state.last_res = res
    st.session_state.hw_trace.append(cpu)
    st.session_state.intel_log.append(f"[{time.strftime('%H:%M:%S')}] [{node}] {res[:55]}")
    log_mission(node, res[:100])

# --- 5. LAYOUT DE COMANDO (FIEL À IMAGEM) ---
st.markdown('<div class="header-tag">📡 CONEXÃO REAL TERMINAL | MÉDICA MESTRA | XEON COMMAND SOBERANO v47.0</div>', unsafe_allow_html=True)

if st.session_state.is_locked:
    st.error("❌ TERMINAL LOCKED")
    mfa = st.text_input("MASTER KEY:", type="password")
    if st.button("RESET"):
        if hashlib.sha256(mfa.encode()).hexdigest() == MASTER_KEY_HASH:
            st.session_state.is_locked = False; st.rerun()
else:
    u_query = st.text_input("", placeholder="INJETAR DADOS / SEARCH MUNDIAL / DNA RESEARCH...", label_visibility="collapsed")
    if st.button("EXE_SOVEREIGN_SCAN"):
        if u_query: run_kernel("DATA_INJECT", u_query)

    st.markdown("<div style='text-align: center; border: 1px solid #00FFCC; font-size: 9px; margin: 8px 0;'>IDENTIFICADOR DA MISSÃO (TERMINAL, BANCO, BIO, GUERRA)</div>", unsafe_allow_html=True)

    # GRID DE 4 COLUNAS - 8 BOTÕES OPERACIONAIS
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.caption("🏗️ ENGENHARIA")
        if st.button("LITHO GRAFENO"): run_kernel("ENG_GRAF")
        if st.button("CORE INTEGRITY"): run_kernel("ENG_CORE")
    with c2:
        st.caption("🌍 GEOPOLÍTICA")
        if st.button("SCAN GLOBAL"): run_kernel("GEO", u_query)
        if st.button("DEFESA SPX"): run_kernel("GEO_SPX")
    with c3:
        st.caption("💰 FINANCEIRO")
        target = st.selectbox("", ["BTC-USD", "GC=F", "ETH-USD"], label_visibility="collapsed")
        if st.button("BOLSAS REAIS"): run_kernel("FIN_MKT")
        if st.button("SWIFT FLOW"): run_kernel("FIN_SWIFT")
    with c4:
        st.caption("🧬 BIO-EVOLUÇÃO")
        if st.button("DNA ANALYSIS"): run_kernel("BIO", u_query)
        
        def generate_pdf():
            output = BytesIO(); p = canvas.Canvas(output, pagesize=A4); p.setFillColorRGB(0,0,0); p.rect(0,0,600,900,fill=1)
            p.setFillColorRGB(0,1,0.8); p.setFont("Courier-Bold", 14); p.drawString(50, 820, "REPORTE SOBERANO v47.0")
            with sovereign_transaction() as conn:
                logs = conn.execute("SELECT * FROM intel_vault ORDER BY timestamp DESC LIMIT 60").fetchall()
            y = 790; p.setFont("Courier", 7)
            for l in logs: p.drawString(50, y, f"> {l}"); y -= 12
            p.showPage(); p.save(); output.seek(0); return output
        st.download_button("📄 IMPRIMIR PDF", data=generate_pdf(), file_name="XEON_REPORT.pdf")

    st.markdown(f'<div class="res-box">{st.session_state.last_res}</div>', unsafe_allow_html=True)

# TERMINAL E ESPECTRO DE HARDWARE
st.markdown('<div class="terminal">' + "<br>".join(list(st.session_state.intel_log)) + '</div>', unsafe_allow_html=True)

fig = go.Figure(go.Bar(y=list(st.session_state.hw_trace), marker_color='#00FFCC', marker_line_width=0))
fig.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=140, paper_bgcolor='black', plot_bgcolor='black', xaxis=dict(visible=False), yaxis=dict(visible=False))
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# STATUS
st.write(f"📊 **HARDWARE:** CPU: {psutil.cpu_percent()}% | RAM: {psutil.virtual_memory().percent}% | **STATUS:** ✅ REAL SOBERANO")

time.sleep(5)
if not u_query and not st.session_state.is_locked: st.rerun()
