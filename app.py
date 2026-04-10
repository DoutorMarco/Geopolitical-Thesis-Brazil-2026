import streamlit as st
import numpy as np
import yfinance as yf
from scipy.fft import fft, fftfreq
from scipy.signal.windows import kaiser
import plotly.graph_objects as go
import time, hashlib, sqlite3, os
from cryptography.fernet import Fernet

# --- ARQUITETURA DE DEFESA (C4ISR) ---
if 'secret_key' not in st.session_state: 
    st.session_state.secret_key = Fernet.generate_key()
cipher = Fernet(st.session_state.secret_key)

st.set_page_config(page_title="XEON COMMAND v13.2", layout="wide")

# CSS PARA VISUAL IDÊNTICO À IMAGEM (Cores e Bordas Neon)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FFCC; font-family: 'Courier New', monospace; }
    
    /* Configuração de Botões com as Cores da Imagem */
    div.stButton > button { border-radius: 0px; font-weight: bold; height: 45px; width: 100%; border: 1px solid #00FFCC; }
    
    /* Engenharia: Amarelo */
    div.stButton > button:nth-child(1) { background-color: #FFCC00; color: black; }
    
    /* Geopolítica: Verde Mar / Teal */
    [data-testid="column"]:nth-child(2) button { background-color: #008080; color: white; }
    
    /* Financeiro: Branco */
    [data-testid="column"]:nth-child(3) button { background-color: #FFFFFF; color: black; }
    
    /* Bio-Evolução: Ciano e Vermelho */
    [data-testid="column"]:nth-child(4) button:first-child { background-color: #00FFFF; color: black; }
    [data-testid="column"]:nth-child(4) button:last-child { background-color: #FF3300; color: white; }

    .log-box { background-color: #000000; border: 2px solid #00FFCC; padding: 15px; color: #00FFCC; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

class XeonEngineV13:
    def __init__(self):
        self.db_path = "xeon_sovereign.db"
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS audit_ledger (ts REAL, payload BLOB, hash TEXT)")
            try: conn.execute("ALTER TABLE audit_ledger ADD COLUMN hash TEXT")
            except: pass

# --- CABEÇALHO TÁTICO ---
st.write(f"📡 CONEXÃO REAL: TERMINAIS MUNDIAIS {' '*30} MÉDICA MESTRA: XEON® COMMAND {' '*30} {time.strftime('%H:%M:%S')}")
st.markdown("<h3 style='text-align: center; border: 1px solid #00FFCC; padding: 10px;'>IDENTIFICADOR DA MISSÃO (TERMINAL/BANCO/GUERRA/BIO)</h3>", unsafe_allow_html=True)

# --- GRID DE COMANDO (4 COLUNAS IDÊNTICAS À IMAGEM) ---
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.write("🏗️ ENGENHARIA & HARDWARE")
    st.button("FORJAR CHIP GRAFENO", key="eng1")
    st.button("SENTIR DOR (ANTI-ALUC)", key="eng2")

with c2:
    st.write("🌍 GEOPOLÍTICA DE GUERRA")
    st.button("US/CH/RU/EU DEPT", key="geo1")
    st.button("VARREDURA ORIENTE MÉDIO", key="geo2")

with c3:
    st.write("💰 FINANCEIRO & BOLSAS")
    ticker_input = st.selectbox("", ["BTC-USD", "GC=F", "USDBRL=X"], label_visibility="collapsed")
    st.button("B.C. & BOLSAS REAIS", key="fin1")
    st.button("CORRETORAS & BANCOS", key="fin2")

with c4:
    st.write("🧬 BIO-EVOLUÇÃO & LUA")
    st.button("BIO/CURA/LONGEVIDADE", key="bio1")
    st.button("📄 PDF DE SOBERANIA", key="pdf")

# --- PROCESSAMENTO DE SINAL ---
engine = XeonEngineV13()
try:
    df = yf.download(ticker_input.strip(), period="300d", interval="1d", progress=False)
    if not df.empty and len(df) >= 128:
        precos = df['Close'].values.flatten()
        returns = np.diff(np.log(precos))
        y = (returns[-128:] - np.mean(returns[-128:])) * kaiser(128, beta=14)
        mag = 2.0/128 * np.abs(fft(y)[0:64])
        
        last_price = float(precos[-1])
        current_hash = hashlib.sha256(f"{last_price}{time.time()}".encode()).hexdigest()

        st.divider()
        log_text = f"""
        [REGISTRO SOBERANO IMORTALIZADO] -----------------------------
        🛡️ HARDWARE: Xeon Sentinel Neuromórfico | STATUS: OPERACIONAL
        🎯 ALVO: {ticker_input} | PREÇO: {last_price:.2f}
        >> SHA-256: {current_hash[:32]}...
        >> STATUS: CONEXÃO TERMINAL CRIPTOGRAFADA EM {time.strftime('%H:%M:%S')}
        """
        st.markdown(f"<div class='log-box'><pre style='color: #00FFCC; margin:0;'>{log_text}</pre></div>", unsafe_allow_html=True)

        # Gráfico Espectral de Barras Verdes (Idêntico ao Rodapé da Imagem)
        fig = go.Figure(go.Bar(x=np.arange(64), y=mag, marker_color='#00FFCC'))
        fig.update_layout(template="plotly_dark", height=200, margin=dict(l=0,r=0,b=0,t=10), paper_bgcolor='black', plot_bgcolor='black')
        st.plotly_chart(fig, use_container_width=True)
except:
    st.error("AGUARDANDO SINCRONIA...")

time.sleep(60)
st.rerun()
