import streamlit as st
import numpy as np
import psutil
import time
import asyncio
import plotly.graph_objects as go
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import datetime

# ==========================================
# 1. BLINDAGEM VISUAL TOTAL (ZERO BRANCO)
# ==========================================
st.set_page_config(page_title="Nexus Supremo v1032", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    :root { background-color: #000000 !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main {
        background-color: #000000 !important;
        color: #00FF41 !important;
        font-family: 'Courier New', monospace;
    }
    div[data-testid="stChatInput"] { background-color: #050505 !important; border-top: 1px solid #1E293B !important; }
    textarea { background-color: #000000 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    [data-testid="stMetricValue"] { color: #38BDF8 !important; font-size: 2rem !important; }
    [data-testid="stMetricLabel"] { color: #00FF41 !important; }
    .stButton>button {
        background-color: #000000 !important;
        color: #38BDF8 !important;
        border: 1px solid #38BDF8 !important;
        height: 45px;
        transition: 0.3s;
        border-radius: 0px;
    }
    .stButton>button:hover { border-color: #00FF41 !important; color: #00FF41 !important; box-shadow: 0 0 15px #00FF41; }
    footer, header, #MainMenu { visibility: hidden !important; }
    hr { border-top: 1px solid #1E293B !important; }
    </style>
    """, unsafe_allow_html=True)

def speak(text):
    st.components.v1.html(f"<script>window.speechSynthesis.speak(new SpeechSynthesisUtterance('{text}'));</script>", height=0)

# ==========================================
# 2. INTERFACE OPERACIONAL ORIGINAL
# ==========================================
st.markdown("<h1 style='text-align: center; color: #38BDF8; letter-spacing: 12px;'>🛡️ NEXUS SUPREMO v1032</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00FF41; font-size: 0.8rem;'>ARQUITETURA DE ENGENHARIA SÊNIOR - MISSÃO CRÍTICA</p>", unsafe_allow_html=True)

# PAINEL SUPERIOR DE TELEMETRIA
col_a, col_b, col_c, col_d = st.columns(4)
with col_a:
    st.metric("CPU CARGA", f"{psutil.cpu_percent()}%")
with col_b:
    st.metric("MEMÓRIA", f"{psutil.virtual_memory().percent}%")
with col_c:
    net_io = psutil.net_io_counters()
    st.metric("TRÁFEGO REDE", f"{(net_io.bytes_sent + net_io.bytes_recv) / 1024 / 1024:.1f} MB")
with col_d:
    st.metric("STATUS SOH", "v2.2 ACTIVE")

st.divider()

# MAPA E TERMINAL DE COMANDO
col_map, col_terminal = st.columns([1.5, 1])

with col_map:
    map_fig = go.Figure(go.Scattergeo(
        lat=[-2.3, 25.9, -15.7, 40.71, 35.68], 
        lon=[-44.4, -97.1, -47.8, -74.00, 139.69],
        text=["Alcântara", "Starbase", "Brasília HQ", "Global NY", "Tokyo Node"],
        mode='markers+text', 
        marker=dict(size=12, color='#38BDF8', symbol='diamond', line=dict(width=2, color='#00FF41'))
    ))
    map_fig.update_layout(
        geo=dict(bgcolor='#000000', showland=True, landcolor='#050505', countrycolor='#1E293B', 
                 projection_type='orthographic', showocean=False),
        margin=dict(l=0,r=0,t=0,b=0), height=350, paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(map_fig, use_container_width=True)

with col_terminal:
    st.write("### ⌨️ INGESTÃO DE COMANDO")
    if cmd := st.chat_input("Executar Auditoria Xeon..."):
        res = f"SISTEMA XEON: Auditoria em '{cmd}' finalizada. Vetor de integridade: 1.0."
        st.session_state.last_res = res
        speak(res)
    
    if 'last_res' in st.session_state:
        st.info(f"**LOG:** {st.session_state.last_res}")

# GRADE DE OPERAÇÕES EXPANDIDA
st.write("### 🚀 MÓDULOS DE MISSÃO")
btns = [
    ("🚀 SPACEX", "SPACEX"), ("⚖️ LAW", "LAW"), ("🧠 NEURALINK", "NEURALINK"), 
    ("🧬 BIOGENETICS", "BIOGENETICS"), ("📈 IPO GOLD", "IPO"), ("🏗️ ENG SÊNIOR", "ENGINEERING"),
    ("🛡️ DEFESA CYBER", "CYBER"), ("📊 VALUATION", "IPO"), ("🌐 SOBERANIA", "SOH")
]

cols = st.columns(3)
for i, (label, key) in enumerate(btns):
    with cols[i % 3]:
        if st.button(label, use_container_width=True):
            res = f"MÓDULO {key}: Ativado. Sincronia 100%."
            st.session_state.last_res = res
            speak(res)

# EXPORTAÇÃO E AUDITORIA PDF
if 'last_res' in st.session_state:
    st.divider()
    buf = BytesIO()
    p = canvas.Canvas(buf, pagesize=A4)
    p.setFillColorRGB(0, 0, 0); p.rect(0, 0, 600, 900, fill=1)
    p.setFillColorRGB(0, 1, 0.25)
    p.setFont("Courier-Bold", 18); p.drawString(50, 800, "DOSSIÊ DE AUDITORIA CRÍTICA - NEXUS v1032")
    p.save(); buf.seek(0)
    st.download_button("📂 BAIXAR RELATÓRIO SOBERANO (PDF)", buf, "Nexus_Audit_Report.pdf", use_container_width=True)

# PULSO DE SINCRONIA NEURAL
st.divider()
t = np.linspace(0, 10, 250)
y = np.sin(t + time.time())
fig_wave = go.Figure(go.Scatter(x=t, y=y, line=dict(color='#00FF41', width=1), fill='tozeroy', fillcolor='rgba(0, 255, 65, 0.1)'))
fig_wave.update_layout(
    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
    height=120, margin=dict(l=0,r=0,t=0,b=0), 
    xaxis=dict(visible=False), yaxis=dict(visible=False, range=[-2, 2])
)
st.plotly_chart(fig_wave, use_container_width=True)
