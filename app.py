import streamlit as st
import pandas as pd
import yfinance as yf
import feedparser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import time
from Bio import Entrez

# --- CONFIGURAÇÃO DE INTERFACE NEON ---
st.set_page_config(page_title="XEON COMMAND", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF00; }
    h1, h2, h3, p, span { color: #00FF00 !important; font-family: 'Courier New', monospace; }
    .stButton>button { background-color: #000000; color: #00FF00; border: 1px solid #00FF00; width: 100%; }
    .stTextInput>div>div>input { background-color: #111111; color: #00FF00; border: 1px solid #00FF00; }
    </style>
    """, unsafe_allow_html=True)

# --- CÉREBRO E LÓGICA DE INVESTIGAÇÃO ---
def gerar_relatorio_pdf(dados_mkt, dados_med, investigacao):
    nome_pdf = f"Relatorio_Soberania_{int(time.time())}.pdf"
    c = canvas.Canvas(nome_pdf, pagesize=A4)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 800, "XEON® COMMAND - RELATÓRIO DE SOBERANIA MUNDIAL")
    c.setFont("Helvetica", 10)
    c.drawString(50, 780, f"DATA: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, 750, f"INVESTIGAÇÃO REALIZADA: {investigacao[:50]}...")
    c.drawString(50, 730, f"RESULTADOS ENCONTRADOS: {len(dados_med)} REFERÊNCIAS.")
    c.save()
    return nome_pdf

# --- INTERFACE PRINCIPAL ---
st.title("🛡️ XEON® COMMAND - NÚCLEO SOBERANO")

# 1. MÓDULO DE INTERAÇÃO COM O CÉREBRO
st.header("🧠 CÉREBRO DE INVESTIGAÇÃO & SOLUÇÕES")
idioma = st.radio("Selecione o Idioma da Investigação:", ("Português", "English"))
query = st.text_input("Pergunte ao Cérebro (Bio/Guerra/Aero):", "Protocolos de longevidade celular mRNA 2026")

if st.button("EXECUTAR INVESTIGAÇÃO E PROPOR SOLUÇÕES"):
    with st.spinner("Processando lógica senior..."):
        # Busca Bilíngue (PubMed e News)
        prefixo = "cure protocol " if idioma == "English" else "protocolo de cura "
        resultados = feedparser.parse(f"https://google.com{prefixo + query.replace(' ', '+')}&hl=pt-BR&gl=BR")
        
        st.subheader("💡 Soluções e Insights Identificados:")
        for n in resultados.entries[:3]:
            st.success(f"» PROPOSTA: {n.title}")
            st.info(f"Link de Verificação: {n.link}")
        
        # Gerar o PDF para Download Imediato
        pdf_path = gerar_relatorio_pdf(None, resultados.entries, query)
        with open(pdf_path, "rb") as f:
            st.download_button("📥 IMPRIMIR RELATÓRIO PDF PARA O COMPUTADOR", f, file_name=pdf_path)

# 2. STATUS DE MERCADO (DASHBOARD)
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.subheader("💰 Mercado Financeiro")
    ticker = st.selectbox("Ativo:", ["BTC-USD", "GC=F", "USDBRL=X"])
    data = yf.download(ticker, period="1mo", progress=False)
    st.line_chart(data['Close'])

with col2:
    st.subheader("🔬 Bio-Avanços (PubMed)")
    handle = Entrez.esearch(db="pubmed", term=query, retmax=2)
    record = Entrez.read(handle)
    handle.close()
    st.write(f"Protocolos encontrados: {record['IdList']}")
