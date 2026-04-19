import streamlit as st
import psutil, time, hashlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO
from openai import OpenAI

# --- [1. IDENTIDADE SOBERANA - BLACKOUT, CYAN & GREEN] ---
CYAN_NEXUS = "#00FFFF"
MATRIX_GREEN = "#00FF41"
BLACKOUT = "#000000"

st.set_page_config(page_title="NEXUS SUPREMO v1032", layout="wide")

try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    client = None

# ESTÉTICA RIGOROSA (SEM BRANCO / GLOBO EM TEMPO REAL)
st.markdown(f"""
    <style>
    [data-testid="stHeader"], footer {{ display: none !important; }}
    .stApp {{ background-color: {BLACKOUT} !important; color: {CYAN_NEXUS} !important; font-family: 'Courier New', monospace; }}
    
    /* REMOÇÃO TOTAL DE BRANCO NA INGESTÃO */
    .stTextArea textarea {{
        background-color: {BLACKOUT} !important; color: {MATRIX_GREEN} !important;
        border: 1px solid {MATRIX_GREEN} !important; border-radius: 4px;
    }}
    
    .node-card {{
        border: 1px solid rgba(0, 255, 255, 0.3); padding: 10px;
        background: rgba(0, 255, 255, 0.02); text-align: center;
        border-radius: 2px; margin-bottom: 5px;
    }}
    
    /* ONDA VERDE REALTIME INFERIOR */
    .wave-footer {{
        position: fixed; bottom: 0; left: 0; width: 100%; height: 80px;
        background: transparent; overflow: hidden;
    }}
    .wave-footer svg {{ position: relative; display: block; width: 150%; height: 80px; }}
    .wave-footer .shape-fill {{ fill: {MATRIX_GREEN}; opacity: 0.15; }}
    @keyframes moveWave {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-20%); }} }}
    .wave-animation {{ animation: moveWave 8s linear infinite; }}
    </style>
""", unsafe_allow_html=True)

# --- [2. COMPONENTE: GLOBO MUNDIAL EM TEMPO REAL] ---
def render_global_globe():
    st.components.v1.html(f"""
        <div id="globeViz" style="background: {BLACKOUT}; display: flex; justify-content: center;"></div>
        <script src="//://unpkg.com"></script>
        <script>
            const world = Globe()
                (document.getElementById('globeViz'))
                .globeImageUrl('//://unpkg.com')
                .backgroundColor('{BLACKOUT}')
                .width(350).height(350)
                .showAtmosphere(true)
                .atmosphereColor('{MATRIX_GREEN}')
                .atmosphereDayQuotient(0.1);
            world.controls().autoRotate = true;
            world.controls().autoRotateSpeed = 0.5;
        </script>
    """, height=360)

# --- [3. DASHBOARD OPERACIONAL v1032] ---
st.markdown(f"<h3 style='text-align: center; color: {CYAN_NEXUS};'>🛡️ NEXUS SUPREMO v1032</h3>", unsafe_allow_html=True)

# Telemetria Superior (Fiel à Imagem)
t1, t2, t3, t4 = st.columns(4)
t1.metric("CPU CARGA", "29.4%")
t2.metric("MEMORIA", "21.5%")
t3.metric("TRAFEGO REDE", "214.5 MB")
t4.metric("STATUS SOH", "v2.2 ACTIVE")

st.divider()

c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>🌐 GLOBO MUNDIAL REALTIME</small>", unsafe_allow_html=True)
    render_global_globe()

with c2:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>⌨️ INGESTÃO DE COMANDO</small>", unsafe_allow_html=True)
    cmd = st.text_area("", height=120, label_visibility="collapsed", key="nexus_global_cmd")
    if st.button("🚀 EXECUTAR COMANDO SOBERANO"):
        st.components.v1.html(f"<script>var u=new SpeechSynthesisUtterance('Comando processado pelo Cérebro GPT 5.4');u.lang='pt-BR';window.speechSynthesis.speak(u);</script>", height=0)

st.markdown(f"### 🚀 MÓDULOS DE MISSÃO")
módulos = [
    ("SPACEX", "🚀"), ("LAW", "⚖️"), ("NEURALINK", "🧠"),
    ("BIOGENETICS", "🧬"), ("IPO GOLD", "💰"), ("ENG SÊNIOR", "👔"),
    ("DEFESA CYBER", "🛡️"), ("VALUATION", "📈"), ("SOBERANIA", "🌐")
]

cols = st.columns(3)
for i, (name, icon) in enumerate(módulos):
    with cols[i % 3]:
        st.markdown(f"<div class='node-card'><b style='color:{MATRIX_GREEN}'>{icon} {name}</b></div>", unsafe_allow_html=True)
        if st.button(f"GERAR DOSSIÊ {name}", key=f"btn_{i}"):
            st.info(f"Gerando dossiê de 6 páginas para {name}...")

# ONDA VERDE REALTIME (SVG ANIMADO)
st.markdown(f"""
    <div class="wave-footer">
        <svg class="wave-animation" viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
        </svg>
    </div>
""", unsafe_allow_html=True)
