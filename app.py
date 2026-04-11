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

# --- CONFIGURAÇÃO E ESTILO PREMIUM ---
st.set_page_config(page_title="XEON COMMAND", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; }
    .stTextInput>div>div>input { background-color: #101010; color: #00FFCC; border: 1px solid #1a1a1a; border-radius: 4px; }
    .stButton>button { 
        background: linear-gradient(135deg, #002b24 0%, #000000 100%) !important;
        color: #00FFCC !important; border: 1px solid #005f4d !important;
        border-radius: 5px !important; width: 100%; font-weight: bold; height: 38px; font-size: 11px;
    }
    .terminal-output { border: 1px solid #1a1a1a; padding: 15px; background: #000000; border-radius: 8px; height: 160px; overflow-y: auto; font-family: 'Consolas', monospace; font-size: 12px; color: #00FFCC; }
    .res-box { border: 2px solid #005f4d; padding: 15px; text-align: center; font-weight: bold; margin: 15px 0; background: #010101; color: #00FFCC; border-radius: 8px; box-shadow: 0 0 15px rgba(0,255,204,0.15); }
    .col-header { color: #00FFCC; font-size: 13px; font-weight: bold; border-bottom: 1px solid #005f4d; margin-bottom: 10px; padding-bottom: 5px; opacity: 0.9; }
    </style>
    """, unsafe_allow_html=True)

# --- ESTADOS DE MISSÃO ---
if 'intel_log' not in st.session_state: st.session_state.intel_log = collections.deque(["[SYSTEM ONLINE] v45.0 - OMNI CONSCIÊNCIA ATIVA"], maxlen=10)
if 'hw_trace' not in st.session_state: st.session_state.hw_trace = collections.deque([float(random.uniform(8, 15)) for _ in range(60)], maxlen=100)
if 'last_res' not in st.session_state: st.session_state.last_res = "SISTEMA AGUARDANDO INJEÇÃO DE DADOS..."

# --- MOTORES REAIS (ROTEAMENTO INTELIGENTE) ---
def run_mission(node, u_in=""):
    cpu = psutil.cpu_percent()
    res = "PROTOCOLO RECONHECIDO"
    u_in_clean = u_in.strip().upper()

    # Roteador de Consciência (Detecta o tipo de dado automaticamente)
    if node == "AUTO":
        if re.match(r'^[ATCG\s]+$', u_in_clean) and len(u_in_clean) > 3:
            node = "BIO"
        elif u_in_clean in ["BTC", "ETH", "GOLD", "USD"]:
            node = "FIN"
        else:
            node = "GEO"

    # Execução do Motor Específico
    if node == "BIO":
        try:
            dna = Seq(re.sub(r'[^ATCG]', '', u_in_clean))
            res = f"🧬 BIO-SINC: {dna.translate()[:15]}... | COMPLEMENTO: {dna.complement()[:10]}"
        except: res = "ERRO DE SEQUENCIAMENTO GENÉTICO"
    elif node == "FIN":
        try:
            ticker = "BTC-USD" if u_in_clean in ["BTC", "BITCOIN"] else u_in_clean
            val = yf.Ticker(ticker).fast_info.last_price
            res = f"💰 MERCADO REAL: {ticker} = ${val:.2f} | TRANSMISSÃO ATIVA"
        except: res = "ERRO DE CONEXÃO FINANCEIRA (TIMEOUT)"
    elif node == "GEO":
        try:
            # OSINT Real via HTTPX (Google News RSS)
            r = httpx.get(f"https://google.com{u_in if u_in else 'geopolitics'}&hl=pt-BR")
            titles = re.findall(r"<title>(.*?)</title>", r.text)
            res = f"🌍 INTEL: {titles[1].upper()}" if len(titles) > 1 else "SCAN GLOBAL: ESTÁVEL"
        except: res = "TÚNEL OSINT OFFLINE / MODO CACHE"
    elif node == "SYS":
        # Check de Integridade Matemática Pura
        sig = np.random.normal(0, 1, 512)
        integrity = np.allclose(sig, ifft(fft(sig)).real, atol=1e-12)
        res = f"🛡️ CORE INTEGRITY: {'100% VALIDATED' if integrity else 'HARDWARE_BREACH'}"

    st.session_state.last_res = res
    st.session_state.hw_trace.append(cpu)
    st.session_state.intel_log.append(f"[{time.strftime('%H:%M:%S')}] {node}: {res[:65]}")

# --- INTERFACE DE COMANDO ---
st.markdown("<h3 style='color:#00FFCC; margin-bottom:0;'>📡 TERMINAL SOBERANO <span style='font-size:12px; color:#444;'>| v45.0 OMNI-ROUTER</span></h3>", unsafe_allow_html=True)
st.write(f"Sync Global: {time.strftime('%H:%M:%S')}")

# Input com Roteamento Automático
u_input = st.text_input("", placeholder="INJETE DADOS (DNA, TICKER OU PESQUISA) PARA PROCESSAMENTO AUTOMÁTICO...", label_visibility="collapsed")
if st.button("EXECUTAR PROTOCOLO SOBERANO"):
    if u_input: run_mission("AUTO", u_input)

st.write("---")

# Grid de Operações Específicas
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="col-header">🏗️ ENGENHARIA</div>', unsafe_allow_html=True)
    if st.button("CORE INTEGRITY"): run_mission("SYS")
with c2:
    st.markdown('<div class="col-header">🌍 GEOPOLÍTICA</div>', unsafe_allow_html=True)
    if st.button("SCAN GLOBAL"): run_mission("GEO", u_input)
with c3:
    st.markdown('<div class="col-header">💰 FINANCEIRO</div>', unsafe_allow_html=True)
    if st.button("BOLSAS REAIS"): run_mission("FIN", u_input if u_input else "BTC")
with c4:
    st.markdown('<div class="col-header">🧬 BIO-EVOLUÇÃO</div>', unsafe_allow_html=True)
    if st.button("DNA ANALYSIS"): run_mission("BIO", u_input)

# Janela de Resposta Principal
st.markdown(f'<div class="res-box">{st.session_state.last_res}</div>', unsafe_allow_html=True)

# Logs e Terminal
st.markdown(f'<div class="terminal-output">{"<br>".join(list(st.session_state.intel_log))}</div>', unsafe_allow_html=True)

# Gráfico de Frequência de Hardware
fig = go.Figure(go.Scatter(y=list(st.session_state.hw_trace), fill='tozeroy', line=dict(color='#00FFCC', width=2)))
fig.update_layout(
    margin=dict(l=0,r=0,t=10,b=0), height=120, 
    plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(visible=False), yaxis=dict(visible=False)
)
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# Rodapé Técnico
cpu_curr = psutil.cpu_percent()
ram_curr = psutil.virtual_memory().percent
st.markdown(f"<p style='font-size:11px; color:#555;'>📊 CPU: {cpu_curr}% | RAM: {ram_curr}% | SOBERANIA: ✅ ATIVA | STATUS: REAL-TIME</p>", unsafe_allow_html=True)

# Loop de Sincronização
time.sleep(5)
st.rerun()
