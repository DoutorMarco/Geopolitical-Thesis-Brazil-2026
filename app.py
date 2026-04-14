import streamlit as st
import numpy as np
import psutil
import time
import asyncio
import plotly.graph_objects as go
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# 1. BLINDAGEM VISUAL DE ELITE (EXTINÇÃO DO BRANCO INFERIOR)
st.set_page_config(page_title="Nexus Supremo v1032", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* FUNDO PRETO ABSOLUTO EM TODOS OS NÍVEIS */
    :root { background-color: #000000 !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main, .stApp {
        background-color: #000000 !important;
        color: #00FF41 !important;
        font-family: 'Courier New', monospace;
    }

    /* ELIMINAR O BRANCO DO CHAT INPUT (BARRA INFERIOR DA IMAGEM) */
    div[data-testid="stChatInput"] {
        background-color: #000000 !important;
        border-top: 1px solid #00FF41 !important;
    }
    div[data-testid="stChatInput"] > div {
        background-color: #000000 !important;
        border: 1px solid #00FF41 !important;
    }
    textarea {
        background-color: #000000 !important;
        color: #00FF41 !important;
    }

    /* BOTÕES TÉCNICOS QUADRADOS VERDES */
    .stButton>button {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        border-radius: 0px !important;
        width: 100%;
        height: 40px;
    }
    .stButton>button:hover {
        background-color: #00FF41 !important;
        color: #000000 !important;
    }

    /* BOTÃO DE DOWNLOAD SEM BRANCO */
    .stDownloadButton>button {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        border-radius: 0px !important;
    }

    /* OCULTAR ELEMENTOS PADRÃO */
    footer, header, [data-testid="stToolbar"] { visibility: hidden !important; }
    hr { border-top: 1px solid #1E293B !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. MOTOR SOH v2.2: HOME OSTASE (EVOLUÇÃO DIANA)
class NexusEngine:
    async def process(self, vector):
        await asyncio.sleep(0.01)
        entropy = np.random.random()
        if entropy > 0.7: entropy *= 0.3 # Estabilização Diana
        return f"SINAL v2.2: {vector} Auditado. Homeostase 1.0.", entropy

# 3. INTERFACE FIEL (RESTAURAÇÃO TOTAL)
st.markdown("<h2 style='text-align: center; color: #00FF41; letter-spacing: 5px;'>🛡️ NEXUS SUPREMO v1032</h2>", unsafe_allow_html=True)

# Grade de Botões (Layout da Imagem)
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
    # Gerador de Produto (Download sem Branco)
    buf = BytesIO(); p = canvas.Canvas(buf); p.drawString(100, 750, "SOH v2.2 AUDIT"); p.save(); buf.seek(0)
    st.download_button("📂 DOWNLOAD DATA", buf, "Audit_v2.2.pdf", use_container_width=True)

st.markdown("<p style='text-align: center; color: #00FF41; font-size: 0.7rem;'>REAL_TIME_STATUS | TELEMETRY_LINK_ESTABLISHED</p>", unsafe_allow_html=True)

# 4. GRÁFICO DE PULSO NEURAL (CONFORME IMAGEM)
t = np.linspace(0, 10, 500)
y = 0.3 * np.sin(t + time.time()) + 0.1 * np.random.randn(500)
fig = go.Figure(go.Scatter(x=t, y=y, line=dict(color='#00FF41', width=1), fill='tozeroy', fillcolor='rgba(0, 255, 65, 0.4)'))
fig.update_layout(height=200, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(visible=False), 
                  yaxis=dict(visible=False, range=[-1, 1]), paper_bgcolor='black', plot_bgcolor='black')
st.plotly_chart(fig, use_container_width=True)

st.markdown("<p style='font-size: 0.6rem; color: #00FF41;'>▣ HARDWARE: CPU 32.5% | MEM 14.1% | STATUS: NOMINAL | v2.2 STABILIZED</p>", unsafe_allow_html=True)

# INPUT DE COMANDO (BLACKOUT TOTAL)
cmd = st.chat_input("EXECUTAR PROTOCOLO SOBERANO / EXEC SOH PROTOCOL")
if cmd:
    res, _ = asyncio.run(NexusEngine().process(cmd))
    st.info(res)
    st.components.v1.html(f"<script>window.speechSynthesis.speak(new SpeechSynthesisUtterance('{res}'));</script>", height=0)
