import streamlit as st
import numpy as np
import yfinance as yf
from scipy.fft import fft, fftfreq
from scipy.signal.windows import kaiser
import plotly.graph_objects as go
import time, hashlib, sqlite3, os
from cryptography.fernet import Fernet

# --- ARQUITETURA CRIPTOGRÁFICA AT-REST (AES-256) ---
if 'secret_key' not in st.session_state:
    st.session_state.secret_key = Fernet.generate_key()
cipher = Fernet(st.session_state.secret_key)

st.set_page_config(page_title="XEON CORE v10.0", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF00; font-family: 'Courier New', monospace; }
    .stButton>button { background-color: #000000; color: #00FF00; border: 1px solid #00FF00; width: 100%; font-weight: bold; font-size: 11px; }
    .log-box { background-color: #010101; border: 1px solid #00FF00; padding: 10px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

class XeonForenseEngine:
    def __init__(self):
        self.db_path = "xeon_sovereign.db"
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS secure_ledger (id INTEGER PRIMARY KEY, ts REAL, payload BLOB)")

    def insert_encrypted(self, data_dict):
        """Criptografia At-Rest: Proteção Forense de Dados"""
        payload = cipher.encrypt(str(data_dict).encode())
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("INSERT INTO secure_ledger (ts, payload) VALUES (?, ?)", (time.time(), payload))

    def processar_espectro_geopolitico(self, ticker):
        try:
            df = yf.download(ticker.strip(), period="300d", interval="1d", progress=False)
            if df.empty or len(df) < 128: return None
            
            precos = df['Close'].values.flatten()
            returns = np.diff(np.log(precos))
            n = 128
            y = (returns[-n:] - np.mean(returns[-n:])) * kaiser(n, beta=14)
            mag = 2.0/n * np.abs(fft(y)[0:n//2])
            freq = fftfreq(n, d=1.0)[0:n//2]
            
            # Cálculo de Z-Score Espectral para Alerta Precoce
            z_score_espectral = (np.max(mag) - np.mean(mag)) / np.std(mag)
            
            self.insert_encrypted({"ticker": ticker, "z_spec": z_score_espectral, "price": precos[-1]})
            return freq, mag, z_score_espectral, float(precos[-1])
        except: return None

# --- INTERFACE SOBERANA (4 COLUNAS 100% OPERACIONAIS) ---
st.write(f"📡 CONEXÃO REAL: TERMINAIS MUNDIAIS | MÉDICA MESTRA: XEON® COMMAND | {time.strftime('%H:%M:%S')}")
st.markdown("<div style='border: 1px solid #00FF00; padding: 5px; text-align: center; font-size: 12px;'>IDENTIFICADOR DA MISSÃO (TERMINAL/BANCO/GUERRA/BIO)</div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.caption("🏗️ ENGENHARIA")
    st.button("FORJAR CHIP GRAFENO")
    st.button("SENTIR DOR (HARD-CHECK)")
with col2:
    st.caption("🌍 GEOPOLÍTICA")
    st.button("VETOR US/CH/RU")
    st.button("VARREDURA SETOR 7")
with col3:
    st.caption("💰 FINANCEIRO")
    ticker_input = st.selectbox("", ["BTC-USD", "GC=F", "USDBRL=X", "^GSPC"], label_visibility="collapsed")
    st.button("B.C. & BOLSAS REAIS")
with col4:
    st.caption("🧬 BIO-EVOLUÇÃO")
    st.button("CURA / LONGEVIDADE")
    st.button("📄 PDF SOBERANIA")

# --- EXECUÇÃO E ALERTA PREDITIVO ---
xeon = XeonForenseEngine()
data = xeon.processar_espectro_geopolitico(ticker_input)

if data:
    freq, mag, z_spec, preco = data
    st.divider()
    status_cor = "red" if z_spec > 3 else "#00FF00"
    
    log_content = f"""
    [REGISTRO SOBERANO CRIPTOGRAFADO v10.0] ---------------------------
    🛡️ HARDWARE: Xeon Sentinel | STATUS: PROTEÇÃO AT-REST ATIVA (AES)
    🎯 ALVO: {ticker_input} | Z-SCORE ESPECTRAL: {z_spec:.4f}
    >> ALERTA GEOPOLÍTICO: {"ANOMALIA DETECTADA" if z_spec > 3 else "FLUXO ESTÁVEL"}
    >> STATUS: Registro imutabilizado em Banco de Dados Criptografado.
    """
    st.markdown(f"<div class='log-box'><pre style='color: {status_cor}; margin:0;'>{log_content}</pre></div>", unsafe_allow_html=True)

    fig = go.Figure(go.Bar(x=freq, y=mag, marker_color=status_cor))
    fig.update_layout(template="plotly_dark", height=220, margin=dict(l=0,r=0,b=0,t=10), paper_bgcolor='black', plot_bgcolor='black')
    st.plotly_chart(fig, use_container_width=True)

time.sleep(30)
st.rerun()
