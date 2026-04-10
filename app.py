import streamlit as st
import numpy as np
import yfinance as yf
from scipy.fft import fft, fftfreq
import plotly.graph_objects as go
import time
from urllib.parse import quote

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="XEON COMMAND", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF00; font-family: 'Courier New', monospace; }
    .stButton>button { background-color: #000000; color: #00FF00; border: 1px solid #00FF00; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE INTELIGÊNCIA ---
class XeonEngine:
    def processar_fft(self, ticker):
        # Correção: download seguro sem caracteres inválidos
        df = yf.download(ticker.strip(), period="180d", interval="1d", progress=False)
        if len(df) < 128: return None, None, "DADOS INSUFICIENTES", None
        precos = df['Close'].values.flatten()[-128:]
        y = precos - np.mean(precos)
        n = len(y)
        mag = 2.0/n * np.abs(fft(y)[0:n//2])
        freq = fftfreq(n, d=1.0)[0:n//2]
        status = "SINAL ORGÂNICO" if np.max(mag) < 0.5 else "INTERFERÊNCIA"
        return freq, mag, status, float(precos[-1])

# --- INTERFACE (CONFORME IMAGEM) ---
st.title("🛡️ XEON® COMMAND - NÚCLEO SOBERANO")
st.write(f"Sincronia Global: {time.strftime('%H:%M:%S')}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("🏗️ ENGENHARIA")
    st.button("FORJAR CHIP GRAFENO")
    st.button("SENTIR DOR (ANTI-ALUC)")

with col2:
    st.subheader("🌍 GEOPOLÍTICA")
    st.button("US/CH/RU/EU DEPT")
    st.button("VARREDURA ORIENTE MÉDIO")

with col3:
    st.subheader("💰 FINANCEIRO")
    # Ticker limpo para evitar InvalidURL
    ticker_input = st.selectbox("ATIVO:", ["BTC-USD", "GC=F", "USDBRL=X"])
    st.button("B.C. & BOLSAS REAIS")

with col4:
    st.subheader("🧬 BIO-EVOLUÇÃO")
    st.button("BIO/CURA/LONGEVIDADE")
    st.button("📄 PDF DE SOBERANIA")

# --- EXECUÇÃO MATEMÁTICA ---
engine = XeonEngine()
freq, mag, status, preco = engine.processar_fft(ticker_input)

if freq is not None:
    st.divider()
    c1, c2 = st.columns(2)
    c1.metric("PREÇO ATUAL", f"{preco:.2f}")
    c1.metric("STATUS SINAL", status)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=freq, y=mag, marker_color='#00FF00'))
    fig.update_layout(template="plotly_dark", height=300, paper_bgcolor='black', plot_bgcolor='black', margin=dict(l=0,r=0,b=0,t=0))
    st.plotly_chart(fig, use_container_width=True)
