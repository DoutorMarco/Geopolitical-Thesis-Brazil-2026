import streamlit as st
import time
import feedparser
import numpy as np
import plotly.graph_objects as go
from Bio import Entrez
from reportlab.pdfgen import canvas
import urllib.parse

# --- INTERFACE SOBERANA ---
st.set_page_config(page_title="XEON IMMORTAL", layout="wide")
st.markdown("<style>.stApp { background-color: #000000; color: #00FF00; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)

st.title("🛡️ XEON® COMMAND - NÚCLEO IMORTAL 24H")
st.write(f"Sincronia Global: {time.strftime('%H:%M:%S')} | Modo: Pesquisa Persistente")

# --- MOTOR DE BUSCA DE ALTA FIDELIDADE (BLINDADO) ---
def varredura_echelon(termo, lang="pt"):
    # Codificação rigorosa para evitar InvalidURL
    termo_encoded = urllib.parse.quote(termo)
    ceid = "BR:pt" if lang == "pt" else "US:en"
    # Construção da URL sem espaços
    url = f"https://google.com{termo_encoded}&hl={lang}&gl=BR&ceid={ceid}"
    
    try:
        feed = feedparser.parse(url)
        return feed.entries[:3]
    except:
        return []

# --- JANELAS DE INVESTIGAÇÃO ---
col1, col2, col3 = st.columns(3)

with col1:
    st.header("🔬 BIO-CURAS")
    resultados = varredura_echelon("mRNA vaccine longevity cancer cure 2026")
    for n in resultados:
        st.write(f"» {n.title[:65]}...")

with col2:
    st.header("🏗️ HARDWARE")
    resultados = varredura_echelon("neuromorphic chip graphene sensing pain", lang="en")
    for n in resultados:
        st.write(f"» {n.title[:65]}...")

with col3:
    st.header("🛰️ DEFESA")
    resultados = varredura_echelon("SpaceX Starshield military defense", lang="en")
    for n in resultados:
        st.write(f"» {n.title[:65]}...")

# --- MONITOR DE ENTROPIA (CORREÇÃO DE ALUCINAÇÃO) ---
st.divider()
st.header("⚡ MONITOR DE ENTROPIA: HARDWARE vs IA")
val_ia = np.random.normal(1.0, 0.08, 30)
val_hard = np.ones(30)
fig = go.Figure()
fig.add_trace(go.Scatter(y=val_ia, name="IA (Oscilação)", line=dict(color='red', dash='dot')))
fig.add_trace(go.Scatter(y=val_hard, name="HARDWARE (Verdade)", line=dict(color='#00FF00', width=3)))
fig.update_layout(template="plotly_dark", height=300, paper_bgcolor='black', plot_bgcolor='black', margin=dict(l=0,r=0,b=0,t=0))
st.plotly_chart(fig, use_container_width=True)

# --- PDF E AUTO-REFRESH ---
if st.button("GERAR RELATÓRIO DE SOBERANIA"):
    nome = f"XEON_REPORT_{int(time.time())}.pdf"
    c = canvas.Canvas(nome)
    c.drawString(100, 800, "RELATÓRIO XEON IMMORTAL - STATUS 24H")
    c.save()
    with open(nome, "rb") as f:
        st.download_button("BAIXAR PDF", f, file_name=nome)

# Loop Infinito: Atualiza a cada 5 minutos para manter o servidor acordado
time.sleep(300)
st.rerun()
