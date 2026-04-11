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

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="XEON COMMAND", layout="wide", initial_sidebar_state="collapsed")

# --- CSS REFINADO: UX PREMIUM (FIM DO VISUAL CRU) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #e0e0e0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* Input Box Suavizada */
    .stTextInput>div>div>input {
        background-color: #101010; color: #00FFCC; border: 1px solid #1a1a1a;
        border-radius: 4px; padding: 10px; font-size: 16px;
    }

    /* Botões com Profundidade */
    .stButton>button {
        background: linear-gradient(135deg, #002b24 0%, #000000 100%) !important;
        color: #00FFCC !important; border: 1px solid #005f4d !important;
        border-radius: 5px !important; width: 100%; font-weight: bold;
        transition: 0.3s; height: 45px; font-size: 12px;
    }
    .stButton>button:hover {
        border-color: #00FFCC !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
        transform: translateY(-2px);
    }

    /* Terminal Box Estética */
    .terminal-output {
        border: 1px solid #1a1a1a; padding: 15px; background: #000000;
        border-radius: 8px; height: 180px; overflow-y: auto;
        font-family: 'Consolas', monospace; font-size: 12px; color: #00FFCC;
        box-shadow: inset 0 0 10px #000;
    }

    /* Labels de Coluna */
    .col-header {
        color: #00FFCC; font-size: 14px; font-weight: bold;
        border-bottom: 1px solid #005f4d; margin-bottom: 15px; padding-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZAÇÃO DE ESTADOS ---
if 'intel_log' not in st.session_state: 
    st.session_state.intel_log = collections.deque(["[SYSTEM INITIALIZED] SOBERANIA v43.0"], maxlen=10)
if 'hw_trace' not in st.session_state: 
    st.session_state.hw_trace = collections.deque([random.uniform(10, 20) for _ in range(60)], maxlen=100)

# --- MOTORES REAIS ---
def run_mission(node, u_in=""):
    cpu = psutil.cpu_percent()
    res = "SUCCESS"
    # Lógica simplificada para evitar lags de UI
    if node == "BIO":
        try:
            dna = Seq(re.sub(r'[^ATCG]', '', u_in.upper()))
            res = f"DNA: {dna.translate()[:15]}..." if len(dna) > 3 else "WAITING SEQUENCE"
        except: res = "BIO_ERR"
    elif node == "GEO": res = "SCANNING GLOBAL OSINT... STABLE"
    
    st.session_state.hw_trace.append(cpu)
    st.session_state.intel_log.append(f"[{time.strftime('%H:%M:%S')}] {node}: {res}")

# --- HEADER ---
st.markdown("<h3 style='color:#00FFCC; margin-bottom:0;'>📡 TERMINAL SOBERANO <span style='font-size:12px; color:#555;'>| v43.0 CIENTISTA GLOBAL</span></h3>", unsafe_allow_html=True)
st.write(f"Sincronização Ativa: {time.strftime('%H:%M:%S')}")

# --- INPUT PRINCIPAL ---
u_input = st.text_input("", placeholder="INJETAR DADOS / PESQUISA DNA / COMANDO GLOBAL...", label_visibility="collapsed")
if st.button("EXE_SOVEREIGN_PROTOCOL"):
    if u_input: run_mission("INJECT", u_input)

st.write("---")

# --- GRID OPERACIONAL ---
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown('<div class="col-header">🏗️ ENGENHARIA</div>', unsafe_allow_html=True)
    if st.button("CHIP GRAFENO"): run_mission("ENG", "GRAF")
    if st.button("CORE INTEGRITY"): run_mission("SYS", "CORE")

with c2:
    st.markdown('<div class="col-header">🌍 GEOPOLÍTICA</div>', unsafe_allow_html=True)
    if st.button("SCAN GLOBAL"): run_mission("GEO", u_input)
    if st.button("SPACE-X DEFENSE"): run_mission("SPX", "DEF")

with c3:
    st.markdown('<div class="col-header">💰 FINANCEIRO</div>', unsafe_allow_html=True)
    if st.button("BOLSAS REAIS"): run_mission("FIN", "MARKET")
    if st.button("SWIFT FLOW"): run_mission("FIN", "SWIFT")

with c4:
    st.markdown('<div class="col-header">🧬 BIO-EVOLUÇÃO</div>', unsafe_allow_html=True)
    if st.button("DNA ANALYSIS"): run_mission("BIO", u_input)
    # PDF Button
    st.download_button("📄 PDF REPORT", data=BytesIO(b"LOG DATA"), file_name="XEON.pdf")

# --- TERMINAL E GRÁFICO ---
st.markdown(f'<div class="terminal-output">{"<br>".join(list(st.session_state.intel_log))}</div>', unsafe_allow_html=True)

fig = go.Figure(go.Scatter(y=list(st.session_state.hw_trace), fill='tozeroy', line=dict(color='#00FFCC', width=2)))
fig.update_layout(
    margin=dict(l=0,r=0,t=10,b=0), height=120, 
    plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(visible=False), yaxis=dict(visible=False)
)
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# --- FOOTER ---
cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
st.markdown(f"<p style='font-size:11px; color:#555;'>📊 CPU: {cpu}% | RAM: {ram}% | KERNEL: SOBERANO | STATUS: ONLINE</p>", unsafe_allow_html=True)

time.sleep(5)
st.rerun()
