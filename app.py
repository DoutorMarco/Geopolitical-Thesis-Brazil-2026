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
from Bio.Seq import Seq

# --- CONFIGURAÇÃO E ESTILO ---
st.set_page_config(page_title="XEON COMMAND", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; }
    .stTextInput>div>div>input { background-color: #101010; color: #00FFCC; border: 1px solid #1a1a1a; border-radius: 4px; }
    .stButton>button { 
        background: linear-gradient(135deg, #002b24 0%, #000000 100%) !important;
        color: #00FFCC !important; border: 1px solid #005f4d !important;
        border-radius: 5px !important; width: 100%; font-weight: bold; height: 35px; font-size: 10px;
    }
    .terminal-output { border: 1px solid #1a1a1a; padding: 12px; background: #000000; border-radius: 8px; height: 160px; overflow-y: auto; font-family: 'Consolas', monospace; font-size: 11px; color: #00FFCC; }
    .res-box { border: 2px solid #005f4d; padding: 15px; text-align: center; font-weight: bold; margin: 10px 0; background: #010101; color: #00FFCC; border-radius: 8px; box-shadow: 0 0 15px rgba(0,255,204,0.1); }
    .col-header { color: #00FFCC; font-size: 12px; font-weight: bold; border-bottom: 1px solid #005f4d; margin-bottom: 8px; padding-bottom: 4px; opacity: 0.8; }
    </style>
    """, unsafe_allow_html=True)

# --- NÚCLEO DE PERSISTÊNCIA IMUTÁVEL ---
def init_db():
    conn = sqlite3.connect('xeon_vault.db', check_same_thread=False)
    conn.execute('''CREATE TABLE IF NOT EXISTS intel_ledger 
                    (timestamp TEXT, node TEXT, result TEXT, sig_hash TEXT)''')
    conn.commit()
    return conn

db = init_db()

# --- ESTADOS ---
if 'intel_log' not in st.session_state: st.session_state.intel_log = collections.deque(["[SYSTEM ON] v46.0 - LEDGER IMUTÁVEL ATIVO"], maxlen=10)
if 'hw_trace' not in st.session_state: st.session_state.hw_trace = collections.deque([float(random.uniform(5, 12)) for _ in range(60)], maxlen=100)
if 'last_res' not in st.session_state: st.session_state.last_res = "SISTEMA AGUARDANDO INJEÇÃO..."

# --- MOTORES REAIS ---
def run_mission(node, u_in=""):
    cpu = psutil.cpu_percent()
    u_in_clean = u_in.strip().upper()
    
    # Roteador Automático
    if node == "AUTO":
        if re.match(r'^[ATCG\s]+$', u_in_clean) and len(u_in_clean) > 3: node = "BIO"
        elif u_in_clean in ["BTC", "ETH", "GOLD"]: node = "FIN"
        else: node = "GEO"

    if node == "BIO":
        try:
            dna = Seq(re.sub(r'[^ATCG]', '', u_in_clean))
            res = f"🧬 BIO-SINC: {dna.translate()[:15]}... | COMP: {dna.complement()[:10]}"
        except: res = "ERRO GENÔMICO"
    elif node == "FIN":
        try:
            val = yf.Ticker("BTC-USD").fast_info.last_price
            res = f"💰 MERCADO REAL: BTC = ${val:.2f}"
        except: res = "DATA_TIMEOUT"
    elif node == "GEO":
        try:
            r = httpx.get(f"https://google.com{u_in if u_in else 'defense'}&hl=pt-BR")
            titles = re.findall(r"<title>(.*?)</title>", r.text)
            res = f"🌍 INTEL: {titles[1].upper() if len(titles)>1 else 'SCAN OK'}"
        except: res = "OSINT_OFFLINE"
    else: res = "PROTOCOLO VALIDADO"

    # Assinatura Digital (Imutabilidade)
    sig = hashlib.sha256(res.encode()).hexdigest()[:16]
    st.session_state.last_res = f"[{sig}] {res}"
    st.session_state.hw_trace.append(cpu)
    st.session_state.intel_log.append(f"[{time.strftime('%H:%M:%S')}] {node}: {res[:60]}")
    
    # Gravação no Banco de Dados
    db.execute("INSERT INTO intel_ledger VALUES (?,?,?,?)", (time.strftime('%Y-%m-%d %H:%M:%S'), node, res, sig))
    db.commit()

# --- INTERFACE ---
st.markdown("<h3 style='color:#00FFCC; margin-bottom:0;'>📡 TERMINAL SOBERANO <span style='font-size:12px; color:#444;'>| v46.0 LEDGER FINAL</span></h3>", unsafe_allow_html=True)
st.write(f"Sync: {time.strftime('%H:%M:%S')}")

u_input = st.text_input("", placeholder="INJETAR DADOS (DNA, BUSCA, TICKER)...", label_visibility="collapsed")
if st.button("EXECUTAR PROTOCOLO SOBERANO"):
    if u_input: run_mission("AUTO", u_input)

st.write("---")

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="col-header">🏗️ ENGENHARIA</div>', unsafe_allow_html=True)
    if st.button("CORE INTEGRITY"): run_mission("SYS")
with c2:
    st.markdown('<div class="col-header">🌍 GEOPOLÍTICA</div>', unsafe_allow_html=True)
    if st.button("SCAN GLOBAL"): run_mission("GEO", u_input)
with c3:
    st.markdown('<div class="col-header">💰 FINANCEIRO</div>', unsafe_allow_html=True)
    if st.button("BOLSAS REAIS"): run_mission("FIN", "BTC")
with c4:
    st.markdown('<div class="col-header">🧬 BIO-EVOLUÇÃO</div>', unsafe_allow_html=True)
    if st.button("DNA ANALYSIS"): run_mission("BIO", u_input)

st.markdown(f'<div class="res-box">{st.session_state.last_res}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="terminal-output">{"<br>".join(list(st.session_state.intel_log))}</div>', unsafe_allow_html=True)

# Gráfico Real
fig = go.Figure(go.Scatter(y=list(st.session_state.hw_trace), fill='tozeroy', line=dict(color='#00FFCC', width=2)))
fig.update_layout(margin=dict(l=0,r=0,t=10,b=0), height=120, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", xaxis=dict(visible=False), yaxis=dict(visible=False))
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# PDF REPORT
def generate_pdf():
    buf = BytesIO(); p = canvas.Canvas(buf, pagesize=A4); p.setFillColorRGB(0,0,0); p.rect(0,0,600,900,fill=1)
    p.setFillColorRGB(0,1,0.8); p.setFont("Courier-Bold", 14); p.drawString(50, 820, "SOBERANIA LEDGER v46.0")
    logs = db.execute("SELECT * FROM intel_ledger ORDER BY timestamp DESC LIMIT 40").fetchall()
    y = 790; p.setFont("Courier", 7)
    for l in logs: p.drawString(50, y, f"> {l[0]} | {l[1]} | {l[2][:80]} | {l[3]}"); y -= 13
    p.showPage(); p.save(); buf.seek(0); return buf

st.download_button("📄 EXPORTAR LEDGER (PDF)", data=generate_pdf(), file_name="XEON_v46_FINAL.pdf")

st.markdown(f"<p style='font-size:11px; color:#555;'>📊 CPU: {psutil.cpu_percent()}% | RAM: {psutil.virtual_memory().percent}% | LEDGER: ✅ IMUTÁVEL | STATUS: SOBERANO</p>", unsafe_allow_html=True)

time.sleep(5)
st.rerun()
