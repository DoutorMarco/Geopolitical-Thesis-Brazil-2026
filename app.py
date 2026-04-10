import streamlit as st
import time
import feedparser
import numpy as np
import plotly.graph_objects as go
from Bio import Entrez
from reportlab.pdfgen import canvas
import urllib.parse

# --- INTERFACE SOBERANA (DARK NEON) ---
st.set_page_config(page_title="XEON IMMORTAL", layout="wide")
st.markdown("<style>.stApp { background-color: #000000; color: #00FF00; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)

st.title("🛡️ XEON® COMMAND - NÚCLEO IMORTAL 24H")

# --- MÓDULO DE INTERAÇÃO E INJEÇÃO DE DADOS ---
st.header("🧠 CÉREBRO DE INVESTIGAÇÃO & INJEÇÃO")
col_input1, col_input2 = st.columns([3, 1])

with col_input1:
    user_data = st.text_input("INJETAR DADOS OU PERGUNTA (Bio/Guerra/Aero):", "Protocolos de longevidade mRNA 2026")
with col_input2:
    idioma = st.radio("IDIOMA DA BUSCA:", ("Português", "English"))

# --- MOTOR DE BUSCA BILÍNGUE BLINDADO ---
def varredura_echelon(termo, lang="pt"):
    termo_encoded = urllib.parse.quote(termo)
    ceid = "BR:pt" if lang == "Português" else "US:en"
    hl = "pt-BR" if lang == "Português" else "en-US"
    url = f"https://google.com{termo_encoded}&hl={hl}&gl=BR&ceid={ceid}"
    try:
        return feedparser.parse(url).entries[:3]
    except:
        return []

if st.button("EXECUTAR PROTOCOLO DE TRABALHO"):
    with st.spinner("Processando Injeção de Dados..."):
        res = varredura_echelon(user_data, idioma)
        for n in res:
            st.success(f"» [RESULTADO ENCONTRADO] {n.title}")
            st.caption(f"Fonte: {n.link}")

# --- JANELAS DE PESQUISA PERSISTENTE (24H) ---
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.header("🔬 BIO-CURAS")
    for n in varredura_echelon("mRNA vaccine longevity", idioma):
        st.write(f"• {n.title[:60]}...")

with col2:
    st.header("🏗️ HARDWARE")
    for n in varredura_echelon("neuromorphic chip graphene", "English"):
        st.write(f"• {n.title[:60]}...")

with col3:
    st.header("🛰️ DEFESA")
    for n in varredura_echelon("SpaceX Starshield defense", "English"):
        st.write(f"• {n.title[:60]}...")

# --- MONITOR DE ENTROPIA (IA CORRIGIDA PELO HARDWARE) ---
st.divider()
st.header("⚡ MONITOR DE ENTROPIA: HARDWARE vs IA")
val_ia = np.random.normal(1.0, 0.08, 30)
val_hard = np.ones(30)
fig = go.Figure()
fig.add_trace(go.Scatter(y=val_ia, name="IA (Oscilação)", line=dict(color='red', dash='dot')))
fig.add_trace(go.Scatter(y=val_hard, name="HARDWARE (Sincronia)", line=dict(color='#00FF00', width=3)))
fig.update_layout(template="plotly_dark", height=250, paper_bgcolor='black', plot_bgcolor='black', margin=dict(l=0,r=0,b=0,t=0))
st.plotly_chart(fig, use_container_width=True)

# --- PDF E REFRESH AUTOMÁTICO ---
if st.button("IMPRIMIR RELATÓRIO DE SOBERANIA"):
    nome = f"XEON_REPORT_{int(time.time())}.pdf"
    c = canvas.Canvas(nome)
    c.drawString(100, 800, f"RELATÓRIO DE TRABALHO - {user_data[:40]}")
    c.save()
    with open(nome, "rb") as f:
        st.download_button("BAIXAR PARA O COMPUTADOR", f, file_name=nome)

# Comando para manter o servidor ativo
time.sleep(300)
st.rerun()
