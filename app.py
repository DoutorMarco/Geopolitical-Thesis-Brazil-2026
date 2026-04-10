import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from twilio.rest import Client

# --- CONFIGURAÇÃO DE SEGURANÇA ---
TWILIO_SID = st.secrets.get("TWILIO_SID", "")
TWILIO_TOKEN = st.secrets.get("TWILIO_TOKEN", "")

# --- MOTOR DE INTELIGÊNCIA BLINDADO ---
st.title("🛡️ XEON® COMMAND - MONITORAMENTO GLOBAL")

ticker = st.sidebar.selectbox("ATIVO DE REFERÊNCIA", ["BTC-USD", "GC=F", "USDBRL=X", "^GSPC"])
limiar_risco = st.sidebar.slider("LIMIAR DE Z-SCORE (RISCO)", 1.5, 3.0, 2.0)

# Coleta de Dados com Verificação de Integridade
try:
    df = yf.download(ticker, period="2mo", interval="1d", progress=False)
    
    if not df.empty and len(df) > 10:
        # Matemática Senior: Retornos Logarítmicos
        precos = df['Close'].values.flatten()
        returns = np.diff(np.log(precos))
        
        # Cálculo de Z-Score Seguro
        mean_ret = np.mean(returns)
        std_ret = np.std(returns)
        z_score_atual = (returns[-1] - mean_ret) / std_ret if std_ret > 0 else 0
        
        # Exibição de Métricas
        st.metric(label=f"Z-SCORE {ticker}", value=f"{z_score_atual:.2f}")
        st.line_chart(df['Close'])
        
        # Lógica de Alerta
        if abs(z_score_atual) > limiar_risco:
            st.error(f"🚨 ANOMALIA DETECTADA EM {ticker}!")
    else:
        st.warning("⚠️ Aguardando sincronização de dados do servidor financeiro...")
        
except Exception as e:
    st.error(f"Erro de Conectividade: {e}")
