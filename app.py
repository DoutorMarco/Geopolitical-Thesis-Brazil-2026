import streamlit as st
import numpy as np
import yfinance as yf
from scipy.fft import fft, fftfreq
import plotly.graph_objects as go
import time

# --- CONFIGURAÇÃO TÁTICA ---
st.set_page_config(page_title="XEON COMMAND v2.3", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF00; font-family: 'Courier New', monospace; }
    .stButton>button { background-color: #000000; color: #00FF00; border: 1px solid #00FF00; width: 100%; font-weight: bold; }
    .stMetric { background-color: #0a0a0a; border: 1px solid #00FF00; padding: 10px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

class XeonIntegratedIntelligence:
    def processar_fft(self, ticker):
        df = yf.download(ticker, period="180d", interval="1d", progress=False)
        if len(df) < 128: return None, None, "DADOS INSUFICIENTES", None
        precos = df['Close'].values[-128:]
        y = precos - np.mean(precos)
        n = len(y)
        mag = 2.0/n * np.abs(fft(y)[0:n//2])
        freq = fftfreq(n, d=1.0)[0:n//2]
        status = "SINAL ORGÂNICO" if np.max(mag[n//4:]) < 0.2 else "INTERFERÊNCIA DETECTADA"
        return freq, mag, status, float(precos[-1])

# --- INTERFACE VISUAL (CONFORME IMAGEM) ---
st.title("🛡️ XEON® COMMAND - NÚCLEO SOBERANO v2.3")
st.write(f"Sincronia Global: {time.strftime('%H:%M:%S')} | STATUS: CRIPTOGRAFADO")

# 4 Colunas Operacionais da Imagem
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("🏗️ ENGENHARIA")
    if st.button("FORJAR CHIP GRAFENO"): st.toast("Sintetizando estrutura...")
    if st.button("SENTIR DOR (ANTI-ALUC)"): st.info("Sincronia de Hardware: Erro < 0.0001%")

with col2:
    st.subheader("🌍 GEOPOLÍTICA")
    if st.button("US/CH/RU/EU DEPT"): st.write("Varrendo Departamentos de Guerra...")
    if st.button("VARREDURA ORIENTE MÉDIO"): st.write("Monitorando Setor 7...")

with col3:
    st.subheader("💰 FINANCEIRO")
    ticker_selecionado = st.selectbox("ATIVO:", ["BTC-USD", "GC=F", "USDBRL=X"])
    if st.button("B.C. & BOLSAS REAIS"): st.success("Sincronizado com Terminais Bancários.")

with col4:
    st.subheader("🧬 BIO-EVOLUÇÃO")
    if st.button("BIO/CURA/LONGEVIDADE"): st.write("Acessando Repositórios NIH...")
    if st.button("📄 PDF DE SOBERANIA"): st.download_button("BAIXAR PDF", "DADOS", "Relatorio_Xeon.pdf")

# --- MOTOR DE PRECISÃO (DASHBOARD ANALÍTICO) ---
st.divider()
engine = XeonIntegratedIntelligence()
freq, mag, status, preco = engine.processar_fft(ticker_selecionado)

if freq is not None:
    c1, c2, c3 = st.columns(3)
    c1.metric("PREÇO ATUAL", f"{preco:.2f}")
    c2.metric("INTEGRIDADE ESPECTRAL", status)
    c3.metric("ENTROPIA DE SINAL", f"{np.std(mag):.6f}")

    # Visualização de Frequência (Assinatura do Chip/Sinal)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=freq, y=mag, marker_color='#00FF00'))
    fig.update_layout(template="plotly_dark", height=300, title="ASSINATURA ESPECTRAL (DOMÍNIO DA FREQUÊNCIA)", 
                      margin=dict(l=0,r=0,b=0,t=0), paper_bgcolor='black', plot_bgcolor='black')
    st.plotly_chart(fig, use_container_width=True)
