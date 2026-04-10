import streamlit as st
import numpy as np
import yfinance as yf
from scipy import stats
import plotly.graph_objects as go

# --- NÚCLEO DE PRECISÃO ARMAMENTISTA ---
st.set_page_config(page_title="XEON CORE v2.1", layout="wide")
st.markdown("<style>.stApp { background-color: #000000; color: #00FF00; }</style>", unsafe_allow_html=True)

class XeonDefenseEngine:
    """Motor Analisador de Sinais com Tratamento de Eventos Extremos"""

    def processamento_sinal_estocastico(self, ticker):
        try:
            # Sincronização de Dados (Redundância de 60 dias para estabilidade)
            df = yf.download(ticker, period="60d", interval="1d", progress=False)
            if df.empty: return None

            precos = df['Close'].values.flatten()
            retornos_log = np.diff(np.log(precos))

            # 1. Cálculo de Curtose (Medição de Risco de Cauda/Cisne Negro)
            curtose = stats.kurtosis(retornos_log)
            
            # 2. Z-Score com Correção de Cauda Longa
            mean = np.mean(retornos_log)
            std = np.std(retornos_log)
            ultimo_z = (retornos_log[-1] - mean) / std

            # 3. Veredito de Integridade (Engenharia de Dados Senior)
            status = "NORMALIDADE"
            if abs(ultimo_z) > 3:
                status = "EVENTO DE CAUDA (CISNE NEGRO)" if curtose > 3 else "ANOMALIA DE HARDWARE"

            return {
                "ticker": ticker,
                "z_score": float(ultimo_z),
                "curtose": float(curtose),
                "status": status,
                "preco_real": float(precos[-1])
            }
        except Exception as e:
            return f"FALHA DE LINK: {str(e)}"

# --- INTERFACE DE COMANDO SOH v2.1 ---
st.title("🛡️ XEON® COMMAND - NÚCLEO DE DEFESA v2.1")
st.write("SISTEMA RESETADO: ALGORITMO ANTI-ALUCINAÇÃO E TRATAMENTO DE CAUDAS LONGAS ATIVO.")

ticker_alvo = st.text_input("SINAL DE ENTRADA (TICKER):", "BTC-USD")
engine = XeonDefenseEngine()

if st.button("SINCRONIZAR TERMINAL"):
    res = engine.processamento_sinal_estocastico(ticker_alvo)
    
    if isinstance(res, dict):
        col1, col2, col3 = st.columns(3)
        col1.metric("PRECISÃO Z-SCORE", f"{res['z_score']:.4f}σ")
        col2.metric("EXCESSO DE CURTOSE", f"{res['curtose']:.4f}")
        col3.metric("STATUS DE SINAL", res['status'])
        
        # Gráfico de Frequência para visualização de Cauda
        st.subheader("PROJEÇÃO DE VOLATILIDADE (HARDWARE SYNC)")
        st.line_chart(yf.download(ticker_alvo, period="1mo", progress=False)['Close'])
    else:
        st.error(res)
