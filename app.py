import streamlit as st
import numpy as np
import yfinance as yf
from scipy.fft import fft, fftfreq
from scipy.signal.windows import kaiser
import plotly.graph_objects as go
import time, hashlib, sqlite3, os, urllib.parse, feedparser
from cryptography.fernet import Fernet

# --- ARQUITETURA DE DEFESA (C4ISR) ---
if 'secret_key' not in st.session_state: 
    st.session_state.secret_key = Fernet.generate_key()
cipher = Fernet(st.session_state.secret_key)

st.set_page_config(page_title="XEON COMMAND v13.3", layout="wide")

# CSS PARA VISUAL IDÊNTICO (Cores Neon e Botões da Imagem)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FFCC; font-family: 'Courier New', monospace; }
    div.stButton > button { border-radius: 0px; font-weight: bold; height: 45px; width: 100%; border: 1px solid #00FFCC; }
    /* Estilização por Cores de Missão */
    div.stButton > button:first-child { background-color: #FFCC00; color: black; } /* Engenharia */
    [data-testid="column"]:nth-child(2) button { background-color: #008080; color: white; } /* Geopolítica */
    [data-testid="column"]:nth-child(3) button { background-color: #FFFFFF; color: black; } /* Financeiro */
    [data-testid="column"]:nth-child(4) button:first-child { background-color: #00FFFF; color: black; } /* Bio */
    [data-testid="column"]:nth-child(4) button:last-child { background-color: #FF3300; color: white; } /* PDF */
    .log-box { background-color: #000000; border: 2px solid #00FFCC; padding: 15px; color: #00FFCC; font-size: 13px; }
    .stTextInput>div>div>input { background-color: #050505; color: #00FFCC; border: 1px solid #00FFCC; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO TÁTICO E CÉLULA DE INTERAÇÃO ---
st.write(f"📡 CONEXÃO REAL: TERMINAIS MUNDIAIS | MÉDICA MESTRA: XEON® COMMAND | {time.strftime('%H:%M:%S')}")

# NOVA ÁREA: INSERÇÃO E PESQUISA (OSINT)
col_in1, col_in2 = st.columns([3, 1])
with col_in1:
    user_input = st.text_input("INJETAR DADOS / PESQUISA PROFUNDA (BIO/GUERRA/AERO):", placeholder="Neuralink Starshield 2026...")
with col_in2:
    idioma = st.selectbox("SISTEMA:", ["Português", "English"], label_visibility="collapsed")

# MOTOR DE RESPOSTA E PESQUISA
if user_input:
    try:
        q_enc = urllib.parse.quote(user_input)
        hl = "pt-br" if idioma == "Português" else "en-us"
        url = f"https://google.com{q_enc}&hl={hl}&gl=BR&ceid=BR:{hl[:2]}"
        feed = feedparser.parse(url).entries[:2]
        for n in feed:
            st.info(f"» [INTEL] {n.title}")
    except: st.error("FALHA NA INGESTÃO DE DADOS EXTERNOS.")

st.markdown("<h3 style='text-align: center; border: 1px solid #00FFCC; padding: 10px;'>IDENTIFICADOR DA MISSÃO (TERMINAL/BANCO/GUERRA/BIO)</h3>", unsafe_allow_html=True)

# --- GRID DE COMANDO (4 COLUNAS IDÊNTICAS À IMAGEM) ---
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.write("🏗️ ENGENHARIA & HARDWARE")
    st.button("FORJAR CHIP GRAFENO", key="e1")
    st.button("SENTIR DOR (ANTI-ALUC)", key="e2")
with c2:
    st.write("🌍 GEOPOLÍTICA DE GUERRA")
    st.button("US/CH/RU/EU DEPT", key="g1")
    st.button("VARREDURA ORIENTE MÉDIO", key="g2")
with c3:
    st.write("💰 FINANCEIRO & BOLSAS")
    t_in = st.selectbox("", ["BTC-USD", "GC=F", "USDBRL=X"], label_visibility="collapsed")
    st.button("B.C. & BOLSAS REAIS", key="f1")
    st.button("CORRETORAS & BANCOS", key="f2")
with c4:
    st.write("🧬 BIO-EVOLUÇÃO & LUA")
    st.button("BIO/CURA/LONGEVIDADE", key="b1")
    st.button("📄 PDF DE SOBERANIA", key="p1")

# --- PROCESSAMENTO ESPECTRAL ---
try:
    df = yf.download(t_in.strip(), period="300d", interval="1d", progress=False)
    if not df.empty and len(df) >= 128:
        precos = df['Close'].values.flatten()
        y = (np.diff(np.log(precos))[-128:] - 0) * kaiser(128, beta=14)
        mag = 2.0/128 * np.abs(fft(y)[0:64])
        
        st.divider()
        log_txt = f"""
        [REGISTRO SOBERANO IMORTALIZADO] -----------------------------
        🛡️ HARDWARE: Xeon Sentinel Neuromórfico | STATUS: OPERACIONAL
        🎯 ALVO: {t_in} | PREÇO: {precos[-1]:.2f}
        >> INVESTIGAÇÃO ATIVA: {user_input[:40]}...
        >> STATUS: CONEXÃO TERMINAL CRIPTOGRAFADA EM {time.strftime('%H:%M:%S')}
        """
        st.markdown(f"<div class='log-box'><pre style='color:#00FFCC; margin:0;'>{log_txt}</pre></div>", unsafe_allow_html=True)
        
        fig = go.Figure(go.Bar(x=np.arange(64), y=mag, marker_color='#00FFCC'))
        fig.update_layout(template="plotly_dark", height=200, margin=dict(l=0,r=0,b=0,t=10), paper_bgcolor='black', plot_bgcolor='black')
        st.plotly_chart(fig, use_container_width=True)
except: st.error("AGUARDANDO SINCRONIA...")

time.sleep(60)
st.rerun()
