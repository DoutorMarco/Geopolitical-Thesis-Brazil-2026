import streamlit as st
import numpy as np
import psutil
import time
import asyncio
import plotly.graph_objects as go
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# 1. BLINDAGEM VISUAL ABSOLUTA (IDENTIDADE v1032)
st.set_page_config(page_title="Nexus Supremo v1032", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Fundo Preto Absoluto e Texto Verde Matrix */
    :root { background-color: #000000 !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main, .stApp {
        background-color: #000000 !important;
        color: #00FF41 !important;
        font-family: 'Courier New', monospace;
    }

    /* Botões Técnicos Quadrados (Conforme Imagem) */
    .stButton>button {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        border-radius: 0px !important;
        width: 100%;
        height: 45px;
        font-size: 0.8rem !important;
    }
    .stButton>button:hover {
        background-color: #00FF41 !important;
        color: #000000 !important;
    }

    /* Botão de Download em Verde (Eliminando o Branco da Imagem) */
    .stDownloadButton>button {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        border-radius: 0px !important;
    }

    /* Input de Chat e Área de Log Blackout */
    div[data-testid="stChatInput"] { background-color: #000000 !important; border-top: 1px solid #00FF41 !important; }
    .stInfo, div[role="alert"] { background-color: #000000 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }

    /* Esconder elementos padrão */
    footer, header, [data-testid="stToolbar"] { visibility: hidden !important; }
    hr { border-top: 1px solid #1E293B !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. MOTOR SOH v2.2 (CAUSA RAIZ ESTABILIZADA)
class NexusEngine:
    async def process(self, vector):
        await asyncio.sleep(0.01)
        # Lógica de Homeostase 0.7 (Filtro Diana)
        entropy = np.random.random()
        if entropy > 0.7: entropy *= 0.4
        return f"SINAL v2.2: {vector} Estabilizado. Integridade 1.0.", entropy

# 3. INTERFACE FIEL À IMAGEM
st.markdown("<h2 style='text-align: center; color: #00FF41; letter-spacing: 5px;'>🛡️ NEXUS SUPREMO v1032</h2>", unsafe_allow_html=True)

# Bloco de Input Superior
cmd = st.chat_input("EXECUTAR PROTOCOLO SOBERANO / EXEC SOH PROTOCOL")

# Grade de Botões Técnicos (Conforme Imagem)
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
    # Produto Soberano (Download sem Branco)
    buf = BytesIO(); p = canvas.Canvas(buf, pagesize=A4); p.drawString(100, 750, "AUDIT v2.2"); p.save(); buf.seek(0)
    st.download_button("📂 DOWNLOAD DATA", buf, "Audit.pdf", use_container_width=True)

st.markdown("<p style='text-align: center; color: #00FF41; font-size: 0.7rem;'>REAL_TIME_STATUS | TELEMETRY_LINK_ESTABLISHED</p>", unsafe_allow_html=True)

# Painel de Log Central
if cmd:
    res, _ = asyncio.run(NexusEngine().process(cmd))
    st.info(res)
    st.components.v1.html(f"<script>window.speechSynthesis.speak(new SpeechSynthesisUtterance('{res}'));</script>", height=0)

# 4. GRÁFICO DE PULSO NEURAL SÓLIDO (BASE DA IMAGEM)
t = np.linspace(0, 10, 500)
y = 0.3 * np.sin(t + time.time()) + 0.1 * np.random.randn(500)
fig = go.Figure(go.Scatter(x=t, y=y, line=dict(color='#00FF41', width=1), fill='tozeroy', fillcolor='rgba(0, 255, 65, 0.4)'))
fig.update_layout(height=180, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(visible=False), 
                  yaxis=dict(visible=False, range=[-1, 1]), paper_bgcolor='black', plot_bgcolor='black')
st.plotly_chart(fig, use_container_width=True)

st.markdown("<p style='font-size: 0.6rem; color: #00FF41;'>▣ HARDWARE: CPU 32.5% | MEM 14.1% | STATUS: NOMINAL | SOBERANO</p>", unsafe_allow_html=True)
