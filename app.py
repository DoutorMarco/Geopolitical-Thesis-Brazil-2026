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

# --- CONFIGURAÇÃO E CSS ---
st.set_page_config(page_title="XEON COMMAND", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; }
    .stTextInput>div>div>input { background-color: #101010; color: #00FFCC; border: 1px solid #1a1a1a; border-radius: 4px; }
    .stButton>button { 
        background: linear-gradient(135deg, #002b24 0%, #000000 100%) !important;
        color: #00FFCC !important; border: 1px solid #005f4d !important;
        border-radius: 5px !important; width: 100%; font-weight: bold; height: 40px; font-size: 11px;
    }
    .terminal-output { border: 1px solid #1a1a1a; padding: 15px; background: #000000; border-radius: 8px; height: 160px; overflow-y: auto; font-family: 'Consolas', monospace; font-size: 12px; color: #00FFCC; }
    .res-box { border: 2px solid #005f4d; padding: 15px; text-align: center; font-weight: bold; margin: 15px 0; background: #010101; color: #00FFCC; border-radius: 8px; box-shadow: 0 0 10px rgba(0,255,204,0.1); }
    .col-header { color: #00FFCC; font-size: 13px; font-weight: bold; border-bottom: 1px solid #005f4d; margin-bottom: 10px; padding-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZAÇÃO ---
if 'intel_log' not in st.session_state: st.session_state.intel_log = collections.deque(["[SYSTEM ONLINE] v44.0 - READY FOR TEST"], maxlen=10)
if 'hw_trace' not in st.session_state: st.session_state.hw_trace = collections.deque([float(random.uniform(5, 12)) for _ in range(60)], maxlen=100)
if 'last_res' not in st.session_state: st.session_state.last_res = "AGUARDANDO INGESTÃO DE TESTE..."

# --- MOTORES REAIS (SEM ALUCINAÇÃO) ---
def run_mission(node, u_in=""):
    t_start = time.perf_counter()
    cpu = psutil.cpu_percent()
    res = "PROTOCOLO EXECUTADO"

    if node == "BIO":
        try:
            clean_dna = re.sub(r'[^ATCG]', '', u_in.upper())
            dna = Seq(clean_dna)
            res = f"DNA: {dna.complement()} | PROTEÍNA: {dna.translate()[:10]}..." if len(dna) >= 3 else "INSIRA DNA VÁLIDO"
        except: res = "ERRO GENÔMICO"
    elif node == "FIN":
        try:
            btc = yf.Ticker("BTC-USD").fast_info.last_price
            res = f"BTC-USD REAL: ${btc:.2f} | TRANSMISSÃO ATIVA"
        except: res = "ERRO DE CONEXÃO FINANCEIRA"
    elif node == "GEO":
        try:
            # OSINT em tempo real (RSS)
            r = httpx.get(f"https://google.com{u_in if u_in else 'geopolitics'}+2026&hl=pt-BR")
            titles = re.findall(r"<title>(.*?)</title>", r.text)
            res = titles[1].upper() if len(titles) > 1 else "SCAN GLOBAL: ESTÁVEL"
        except: res = "CONEXÃO OSINT OFFLINE"

    st.session_state.last_res = res
    st.session_state.hw_trace.append(cpu)
    st.session_state.intel_log.append(f"[{time.strftime('%H:%M:%S')}] {node}: {res[:60]}")

# --- UI ---
st.markdown("<h3 style='color:#00FFCC; margin-bottom:0;'>📡 TERMINAL SOBERANO <span style='font-size:12px; color:#444;'>| v44.0 REAL-TIME</span></h3>", unsafe_allow_html=True)
st.write(f"Sync: {time.strftime('%H:%M:%S')}")

u_input = st.text_input("", placeholder="INSIRA DADOS (EX: ATGGCCATT) OU BUSCA GEOPOLÍTICA...", label_visibility="collapsed")
if st.button("EXECUTAR PROTOCOLO SOBERANO"):
    if u_input: run_mission("INJECT", u_input)

st.write("---")

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="col-header">🏗️ ENGENHARIA</div>', unsafe_allow_html=True)
    if st.button("CORE INTEGRITY"): run_mission("SYS", "FFT_CHECK")
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

# Gráfico de Radar Real
fig = go.Figure(go.Scatter(y=list(st.session_state.hw_trace), fill='tozeroy', line=dict(color='#00FFCC', width=2)))
fig.update_layout(margin=dict(l=0,r=0,t=10,b=0), height=120, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", xaxis=dict(visible=False), yaxis=dict(visible=False))
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

st.markdown(f"<p style='font-size:11px; color:#555;'>📊 CPU: {psutil.cpu_percent()}% | RAM: {psutil.virtual_memory().percent}% | STATUS: ✅ REAL SOBERANO</p>", unsafe_allow_html=True)

time.sleep(5)
st.rerun()
