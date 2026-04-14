import streamlit as st
import numpy as np
import time
import plotly.graph_objects as go
from io import BytesIO
from reportlab.pdfgen import canvas

# 1. BLINDAGEM TOTAL - ELIMINAÇÃO CIRÚRGICA DE CORES PADRÃO
st.set_page_config(page_title="Nexus Supremo v1032", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* RESET GLOBAL DE CORES - FUNDO PRETO ABSOLUTO */
    :root { background-color: #000000 !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main, .stApp {
        background-color: #000000 !important;
        color: #00FF41 !important;
        font-family: 'Courier New', monospace;
    }

    /* ELIMINAR BRANCO DO CHAT INPUT (BARRA INFERIOR DA IMAGEM) */
    div[data-testid="stChatInput"] {
        background-color: #000000 !important;
        border: 1px solid #00FF41 !important;
        border-radius: 0px !important;
    }
    div[data-testid="stChatInput"] > div {
        background-color: #000000 !important;
    }
    textarea {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: none !important;
    }

    /* BOTÕES TÉCNICOS QUADRADOS (IDÊNTICOS À IMAGEM) */
    .stButton>button {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        border-radius: 0px !important;
        width: 100%;
        height: 35px;
        font-size: 0.7rem !important;
    }
    .stButton>button:hover {
        background-color: #00FF41 !important;
        color: #000000 !important;
    }

    /* BOTÃO DE DOWNLOAD (ELIMINANDO O BRANCO) */
    .stDownloadButton>button {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        border-radius: 0px !important;
    }

    /* BARRA DE LOG (IDENTIDADE VISUAL DA IMAGEM) */
    .stInfo, div[role="alert"] {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        border-radius: 0px !important;
    }

    /* OCULTAR ELEMENTOS RESIDUAIS */
    footer, header, [data-testid="stToolbar"] { visibility: hidden !important; }
    hr { border-top: 1px solid #00FF41 !important; }
    
    /* SCROLLBARS BLACKOUT */
    ::-webkit-scrollbar { width: 3px; background: #000000; }
    ::-webkit-scrollbar-thumb { background: #00FF41; }
    </style>
    """, unsafe_allow_html=True)

# 2. INTERFACE FIEL À IMAGEM ENVIADA
st.markdown("<h2 style='text-align: center; color: #00FF41; letter-spacing: 5px; margin-bottom: 0px;'>🛡️ NEXUS SUPREMO v1032</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00FF41; font-size: 0.6rem; margin-bottom: 30px;'>EXECUTAR PROTOCOLO SOBERANO / EXEC SOH PROTOCOL</p>", unsafe_allow_html=True)

# Grade de Botões (Layout Fiel 4 colunas)
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.button("LATÊNCIA REDE")
    st.button("CORE INTEGRITY")
with c2:
    st.button("SCAN XEON")
    st.button("DEFESA SOH")
with c3:
    st.button("SINCRONIA")
    st.button("RAFT FLOW")
with c4:
    st.button("TISS ANALYTICS")
    # Download sem Branco
    buf = BytesIO(); p = canvas.Canvas(buf); p.drawString(100, 750, "SOH v2.2"); p.save(); buf.seek(0)
    st.download_button("📂 DOWNLOAD DATA", buf, "Audit.pdf", use_container_width=True)

# Log de Status (Idêntico ao da imagem)
st.info("STATUS: NOMINAL | SOBERANO ATIVO")

# 3. GRÁFICO DE PULSO NEURAL COM PREENCHIMENTO (SOH v2.2 STABILIZED)
t = np.linspace(0, 10, 500)
# Ondulação característica da sua imagem
y = 0.2 * np.sin(1.5 * t + time.time()) + 0.1 * np.random.randn(500)
fig = go.Figure(go.Scatter(x=t, y=y, line=dict(color='#00FF41', width=1.5), fill='tozeroy', fillcolor='rgba(0, 255, 65, 0.4)'))
fig.update_layout(height=250, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(visible=False), 
                  yaxis=dict(visible=False, range=[-1, 1]), paper_bgcolor='black', plot_bgcolor='black')
st.plotly_chart(fig, use_container_width=True)

# Telemetria Inferior
st.markdown("<p style='font-size: 0.6rem; color: #00FF41; text-align: left;'>▣ HARDWARE: CPU 32.5% | MEM 14.1% | STATUS: NOMINAL | SOH v2.2 STABILIZED</p>", unsafe_allow_html=True)

# 4. INPUT DE COMANDO (BLACKOUT TOTAL - SEM BRANCO EMBAIXO)
cmd = st.chat_input("Insert Sovereign Command...")
if cmd:
    # Lógica de resposta direta para manter estabilidade
    res = f"VETOR {cmd}: Auditado com 100% de Integridade."
    st.success(res)
    st.components.v1.html(f"<script>window.speechSynthesis.speak(new SpeechSynthesisUtterance('{res}'));</script>", height=0)
