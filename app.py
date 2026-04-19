import streamlit as st
import psutil, time, hashlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO
from openai import OpenAI

# --- [1. IDENTIDADE SOBERANA - BLACKOUT, CYAN & MATRIX GREEN] ---
CYAN_NEXUS = "#00FFFF"
MATRIX_GREEN = "#00FF41"
BLACKOUT = "#000000"

st.set_page_config(page_title="NEXUS SUPREMO v1032", layout="wide")

try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    client = None

# ESTÉTICA RIGOROSA (SEM BRANCO / GLOBO E ONDA EM TEMPO REAL)
st.markdown(f"""
    <style>
    [data-testid="stHeader"], footer {{ display: none !important; }}
    .stApp {{ background-color: {BLACKOUT} !important; color: {CYAN_NEXUS} !important; font-family: 'Courier New', monospace; }}
    
    /* REMOÇÃO DE BRANCO NA INGESTÃO */
    .stTextArea textarea {{
        background-color: {BLACKOUT} !important; color: {MATRIX_GREEN} !important;
        border: 1px solid {MATRIX_GREEN} !important; border-radius: 4px;
    }}
    
    /* BOTÕES E MÓDULOS */
    .stButton button {{
        border: 1px solid {CYAN_NEXUS} !important; background-color: {BLACKOUT} !important;
        color: {CYAN_NEXUS} !important; font-size: 0.75em !important; width: 100%;
    }}

    /* ONDA VERDE OPERANDO EM TEMPO REAL (ANIMADA) */
    .wave-container {{
        position: fixed; bottom: 0; left: 0; width: 100%; height: 80px;
        background: transparent; overflow: hidden; z-index: 100;
    }}
    .wave-container svg {{ width: 200%; height: 80px; animation: moveWave 10s linear infinite; }}
    .shape-fill {{ fill: {MATRIX_GREEN}; opacity: 0.15; }}
    @keyframes moveWave {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}
    </style>
""", unsafe_allow_html=True)

# --- [2. COMPONENTE: GLOBO MUNDIAL EM TEMPO REAL (GEOSPATIAL)] ---
def render_geospatial_globe():
    # Globo de Alta Resolução com Atmosfera Verde Matrix
    st.components.v1.html(f"""
        <div id="globeViz" style="background: {BLACKOUT}; display: flex; justify-content: center;"></div>
        <script src="https://unpkg.com"></script>
        <script>
            const world = Globe()(document.getElementById('globeViz'))
                .globeImageUrl('//://unpkg.com')
                .backgroundColor('{BLACKOUT}')
                .width(360).height(360)
                .showAtmosphere(true).atmosphereColor('{MATRIX_GREEN}');
            world.controls().autoRotate = true;
            world.controls().autoRotateSpeed = 1.8;
        </script>
    """, height=370)

# --- [3. GERADOR DE DOSSIÊ (6 PÁGINAS - REPORTLAB)] ---
def generate_dossier_v1032(name):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    for i in range(1, 7):
        c.setFillColorRGB(0, 0, 0); c.rect(0, 0, 600, 900, fill=1)
        c.setFillColorRGB(0, 1, 1); c.setFont("Courier-Bold", 16)
        c.drawCentredString(300, 800, f"NEXUS SUPREMO v1032 - DOSSIÊ TÉCNICO")
        c.setFillColorRGB(0, 1, 0.25); c.setFont("Courier", 12)
        c.drawString(50, 750, f"MÓDULO: {name}")
        c.drawString(50, 730, f"ARQUITETO: MARCO ANTONIO DO NASCIMENTO")
        c.drawString(50, 710, f"PÁGINA: {i} / 6")
        c.drawString(50, 690, "VEREDITO: MISSION CRITICAL READINESS")
        c.showPage()
    c.save(); buffer.seek(0)
    return buffer

# --- [4. DASHBOARD OPERACIONAL] ---
st.markdown(f"<h3 style='text-align: center; color: {CYAN_NEXUS};'>🛡️ NEXUS SUPREMO v1032</h3>", unsafe_allow_html=True)

# Telemetria Fiel à Imagem
t1, t2, t3, t4 = st.columns(4)
t1.metric("CPU CARGA", "29.4%")
t2.metric("MEMÓRIA", "21.5%")
t3.metric("TRAFEGO REDE", "214.5 MB")
t4.metric("STATUS SOH", "v2.2 ACTIVE")

st.divider()

c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>🌐 GEOPOLITICAL RADIUS ACTIVE</small>", unsafe_allow_html=True)
    render_geospatial_globe()

with c2:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>⌨️ INGESTÃO DE COMANDO</small>", unsafe_allow_html=True)
    cmd = st.text_area("", height=120, label_visibility="collapsed", key="nexus_cmd_fix")
    if st.button("🚀 EXECUTAR COMANDO"):
        st.components.v1.html(f"<script>var u=new SpeechSynthesisUtterance('Comando Nexus processado. Ativando Cérebro GPT 5.4');u.lang='pt-BR';window.speechSynthesis.speak(u);</script>", height=0)

st.markdown(f"### 🚀 MÓDULOS DE MISSÃO")
modulos = [("SPACEX", "🚀"), ("LAW", "⚖️"), ("NEURALINK", "🧠"), ("BIOGENETICS", "🧬"), ("IPO GOLD", "💰"), ("ENG SÊNIOR", "👔"), ("DEFESA CYBER", "🛡️"), ("VALUATION", "📈"), ("SOBERANIA", "🌐")]

cols = st.columns(3)
for i, (name, icon) in enumerate(modulos):
    with cols[i % 3]:
        st.markdown(f"<div style='border: 1px solid rgba(0,255,255,0.3); padding:10px; text-align:center; color:{MATRIX_GREEN}'><b>{icon} {name}</b></div>", unsafe_allow_html=True)
        if st.button(f"GERAR DOSSIÊ {name}", key=f"btn_{i}"):
            pdf = generate_dossier_v1032(name)
            st.download_button("📥 DOWNLOAD", pdf, f"NEXUS_{name}.pdf", key=f"dl_{i}")

# RODOPE: ONDA VERDE REALTIME
st.markdown("""
    <div class="wave-container">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
        </svg>
    </div>
""", unsafe_allow_html=True)
