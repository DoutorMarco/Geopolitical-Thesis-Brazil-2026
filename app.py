import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from twilio.rest import Client

# --- CONFIGURAÇÃO DE SEGURANÇA (ESTADO DE DEFESA) ---
# No Streamlit Cloud, estas chaves ficam em 'Settings > Secrets'
TWILIO_SID = st.secrets.get("TWILIO_SID", "SEU_SID_AQUI")
TWILIO_TOKEN = st.secrets.get("TWILIO_TOKEN", "SEU_TOKEN_AQUI")
WHATSAPP_DE = "whatsapp:+14155238886" # Número padrão do Sandbox Twilio
WHATSAPP_PARA = "whatsapp:+55XXXXXXXXXXX" # SEU NÚMERO REAL

def disparar_alerta_whatsapp(mensagem):
    try:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(
            body=f"⚠️ ALERTA XEON SOBERANIA: {mensagem}",
            from_=WHATSAPP_DE,
            to=WHATSAPP_PARA
        )
        return True
    except:
        return False

# --- MOTOR DE INTELIGÊNCIA ---
st.title("🛡️ XEON® COMMAND - MONITORAMENTO GLOBAL")

ticker = st.sidebar.selectbox("ATIVO DE REFERÊNCIA", ["BTC-USD", "GC=F", "USDBRL=X"])
limiar_risco = st.sidebar.slider("LIMIAR DE Z-SCORE (RISCO)", 1.5, 3.0, 2.0)

# Coleta de Dados em Tempo Real
df = yf.download(ticker, period="1mo", interval="1d", progress=False)
returns = np.diff(np.log(df['Close'].values.flatten()))
z_score_atual = (returns[-1] - np.mean(returns)) / np.std(returns)

# Interface de Dashboard
st.metric(label=f"Z-SCORE {ticker}", value=f"{z_score_atual:.2f}", delta="ANOMALIA" if abs(z_score_atual) > limiar_risco else "ESTÁVEL")
st.line_chart(df['Close'])

# --- LÓGICA DE ALERTA ATIVA (FUNCIONA NA NUVEM) ---
if abs(z_score_atual) > limiar_risco:
    st.error("🚨 ANOMALIA DETECTADA. DISPARANDO PROTOCOLO WHATSAPP...")
    sucesso = disparar_alerta_whatsapp(f"Desvio Crítico detectado em {ticker}. Z-Score: {z_score_atual:.2f}")
    if sucesso:
        st.success("WhatsApp enviado com sucesso.")
    else:
        st.warning("Falha no envio. Verifique as chaves da Twilio.")
