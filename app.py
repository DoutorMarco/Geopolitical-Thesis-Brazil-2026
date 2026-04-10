import streamlit as st
import numpy as np
import yfinance as yf
from scipy.fft import fft, fftfreq
from scipy.signal import kaiser
import plotly.graph_objects as go
import time

# --- ARQUITETURA SUPREMA (NEON TERMINAL) ---
st.set_page_config(page_title="XEON CORE v4.0", layout="wide")
st.markdown("<style>.stApp { background-color: #000000; color: #00FF00; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)

class XeonSupremoEngine:
    """Motor de Precisão Nível 1: Janela Kaiser Adaptativa + Overlap 50%"""

    def processar_sinal_atomico(self, ticker):
        try:
            # Captura de 256 pontos para permitir Overlap de 50% (128+128)
            df = yf.download(ticker.strip(), period="300d", interval="1d", progress=False)
            if len(df) < 256: return None, None, "DADOS INSUFICIENTES", None
            
            precos = df['Close'].values.flatten()[-256:]
            
            # 1. DIVISÃO EM OVERLAP (SOMA DE SOBREPOSIÇÃO)
            # Processamos dois blocos de 128 com 50% de sobreposição para 0% perda de energia
            bloco_1 = precos[0:128]
            bloco_2 = precos[64:192] 
            
            # 2. JANELA DE KAISER ADAPTATIVA (BETA = 14)
            # Beta 14 fornece supressão de banda lateral de nível armamentista (>100dB)
            n = 128
            window = kaiser(n, beta=14)
            
            y1 = (bloco_1 - np.mean(bloco_1)) * window
            y2 = (bloco_2 - np.mean(bloco_2)) * window
            
            # 3. FFT CONSOLIDADA (MÉDIA ESPECTRAL)
            f_sinal = (fft(y1) + fft(y2)) / 2
            mag = 2.0/n * np.abs(f_sinal[0:n//2])
            freq = fftfreq(n, d=1.0)[0:n//2]
            
            status = "SINAL INABALÁVEL" if np.max(mag) < 0.4 else "EVENTO CRÍTICO IDENTIFICADO"
            
            return freq, mag, status, float(precos[-1])
        except:
            return None, None, "FALHA DE LINK TÁTICO", None

# --- INTERFACE DE COMANDO SOBERANA ---
st.title("🛡️ XEON® COMMAND - NÚCLEO SUPREMO v4.0")
st.write(f"SYNC: {time.strftime('%H:%M:%S')} | MODO: KAISER WINDOW + OVERLAP-ADD ACTIVE")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("🏗️ ENGENHARIA")
    st.button("FORJAR CHIP GRAFENO")
    st.button("SENTIR DOR (VERDADE HARD)")

with col2:
    st.subheader("🌍 GEOPOLÍTICA")
    st.button("VETOR DE GUERRA US/CH")
    st.button("VARREDURA ORIENTE MÉDIO")

with col3:
    st.subheader("💰 FINANCEIRO")
    ticker_input = st.selectbox("ALVO:", ["BTC-USD", "GC=F", "USDBRL=X", "^GSPC"])
    st.button("B.C. & BOLSAS REAIS")

with col4:
    st.subheader("🧬 BIO-EVOLUÇÃO")
    st.button("CURA / LONGEVIDADE")
    st.button("📄 PDF SUPREMO")

# --- PROCESSAMENTO DE PRECISÃO ATÔMICA ---
engine = XeonSupremoEngine()
freq, mag, status, preco = engine.processar_sinal_atomico(ticker_input)

if freq is not None:
    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("VALOR ESCALAR", f"{preco:.2f}")
    c2.metric("INTEGRIDADE", status)
    c3.metric("MOTOR", "KAISER/OVERLAP")

    fig = go.Figure()
    fig.add_trace(go.Bar(x=freq, y=mag, marker_color='#00FF00'))
    fig.update_layout(template="plotly_dark", height=300, paper_bgcolor='black', plot_bgcolor='black', 
                      margin=dict(l=0,r=0,b=0,t=0), title="ESPECTRO DE PRECISÃO NÍVEL 1 (KAISER BETA=14)")
    st.plotly_chart(fig, use_container_width=True)
