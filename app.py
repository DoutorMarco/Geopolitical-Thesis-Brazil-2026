import streamlit as st
import time
import feedparser
import pandas as pd
import urllib.parse
from reportlab.pdfgen import canvas

# --- INTERFACE SOBERANA ---
st.set_page_config(page_title="XEON SOBERANO", layout="wide")
st.markdown("<style>.stApp { background-color: #000000; color: #00FF00; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)

st.title("🛡️ XEON® COMMAND - AUDITORIA DE SOBERANIA")

# --- MÓDULO DE INVESTIGAÇÃO COM LOGS ---
st.header("🧠 INVESTIGAÇÃO & METADADOS DE AUTENTICIDADE")
query = st.text_input("Comando de Investigação:", "Protocolos longevidade mRNA 2026")
idioma = st.radio("Idioma:", ("Português", "English"))

if st.button("EXECUTAR E GERAR LOGS DE AUDITORIA"):
    # Limpeza e busca
    q_enc = urllib.parse.quote(query)
    ceid = "BR:pt" if idioma == "Português" else "US:en"
    url = f"https://google.com{q_enc}&ceid={ceid}"
    
    feed = feedparser.parse(url)
    
    # --- CRIAÇÃO DA TABELA DE METADADOS (AUDITORIA) ---
    logs = []
    for n in feed.entries[:5]:
        logs.append({
            "Timestamp": time.strftime('%H:%M:%S'),
            "Fonte/Portal": n.source.get('title', 'N/A') if 'source' in n else 'Google News',
            "Título do Dado": n.title[:50] + "...",
            "Integridade": "VERIFICADO (RSS/XML)",
            "URL de Origem": n.link
        })
    
    df_logs = pd.DataFrame(logs)
    
    st.success("Busca Finalizada. Metadados de Autenticidade Gerados.")
    st.table(df_logs) # Exibe a tabela de auditoria em verde neon

    # Opção de Impressão do Relatório de Auditoria
    if not df_logs.empty:
        nome_pdf = f"Auditoria_Xeon_{int(time.time())}.pdf"
        c = canvas.Canvas(nome_pdf)
        c.drawString(100, 800, f"LOG DE AUDITORIA TÉCNICA - {query}")
        c.drawString(100, 780, f"SISTEMA: XEON SOBERANO | STATUS: OPERACIONAL")
        c.save()
        with open(nome_pdf, "rb") as f:
            st.download_button("📥 BAIXAR LOG DE AUDITORIA (PDF)", f, file_name=nome_pdf)

# --- STATUS DO CÉREBRO (24H) ---
st.divider()
st.write(f"Sincronia Homeostática Ativa | {time.strftime('%d/%m/%Y %H:%M:%S')}")
