import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from twilio.rest import Client
from Bio import Entrez
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import time
import os

# --- IDENTIDADE E SEGURANÇA ---
TWILIO_SID = st.secrets.get("TWILIO_SID", "")
TWILIO_TOKEN = st.secrets.get("TWILIO_TOKEN", "")
CELULAR_DESTINO = "whatsapp:+5521964316825"
WHATSAPP_ORIGEM = "whatsapp:+14155238886" # Sandbox Twilio
Entrez.email = "xeon.terminal@command.gov"

# --- FUNÇÃO DE COMUNICAÇÃO ---
def enviar_alerta_whatsapp(txt):
    if TWILIO_SID and TWILIO_TOKEN:
        try:
            client = Client(TWILIO_SID, TWILIO_TOKEN)
            client.messages.create(body=f"🛡️ XEON ALERTA: {txt}", from_=WHATSAPP_ORIGEM, to=CELULAR_DESTINO)
            return True
        except Exception as e:
            st.error(f"Erro Twilio: {e}")
    return False

# --- MOTOR DE RELATÓRIOS (PDF DE SOBERANIA) ---
def gerar_pdf_soberania(ticker, z_score, med_id):
    nome_arq = f"Relatorio_Soberania_{time.strftime('%Y%m%d')}.pdf"
    c = canvas.Canvas(nome_arq, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "XEON® COMMAND - RELATÓRIO DE SOBERANIA MUNDIAL")
    c.setFont("Helvetica", 12)
    c.drawString(100, 770, f"DATA: {time.strftime('%d/%m/%Y %H:%M:%S')}")
    c.drawString(100, 750, f"ATIVO ANALISADO: {ticker}")
    c.drawString(100, 735, f"STATUS ESTATÍSTICO (Z-SCORE): {z_score:.2f}")
    c.drawString(100, 720, f"ÚLTIMA REFERÊNCIA MÉDICA NIH: {med_id}")
    c.drawString(100, 680, "SISTEMA OPERANDO EM REGIME DE INDEPENDÊNCIA NA NUVEM.")
    c.save()
    return nome_arq

# --- INTERFACE DE COMANDO ---
st.title("🛡️ XEON® COMMAND - ECHELON INTERFACE")

# Módulo Financeiro
ticker = st.sidebar.selectbox("ATIVO DE REFERÊNCIA", ["BTC-USD", "GC=F", "USDBRL=X", "^GSPC"])
df = yf.download(ticker, period="2mo", interval="1d", progress=False)
precos = df['Close'].values.flatten()
returns = np.diff(np.log(precos))
z_score = (returns[-1] - np.mean(returns)) / np.std(returns)

st.metric(f"Z-SCORE {ticker}", f"{z_score:.2f}", delta="ANOMALIA" if abs(z_score) > 2 else "ESTÁVEL")
st.line_chart(df['Close'])

# Módulo Médico e Relatório
st.header("🔬 BIO-AVANÇOS E SOBERANIA")
if st.button("GERAR RELATÓRIO E VARREDURA"):
    # 1. Busca Médica
    handle = Entrez.esearch(db="pubmed", term="cancer aids longevity cure 2026", retmax=1)
    record = Entrez.read(handle)
    med_id = record["IdList"][0] if record["IdList"] else "Nenhum novo"
    
    # 2. PDF
    pdf_path = gerar_pdf_soberania(ticker, z_score, med_id)
    
    # 3. Alerta WhatsApp
    msg = f"Relatório de hoje gerado. Ativo: {ticker} (Z:{z_score:.2f}). Novo Protocolo Médico: {med_id}"
    enviar_alerta_whatsapp(msg)
    
    with open(pdf_path, "rb") as f:
        st.download_button("BAIXAR PDF DE SOBERANIA", f, file_name=pdf_path)
    st.success("Relatório processado e alerta enviado para seu WhatsApp.")
