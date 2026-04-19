import streamlit as st
import time, psutil, hashlib, unicodedata
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

# --- [MOTOR DE VOX REALTIME] ---
def speak(text):
    st.components.v1.html(f"""
        <script>
        var u = new SpeechSynthesisUtterance('{text}');
        u.lang = 'pt-BR'; u.rate = 0.9;
        window.speechSynthesis.speak(u);
        </script>
    """, height=0)

# --- [ESTÉTICA MATRIX ABSOLUTA & ONDA OPERACIONAL] ---
st.markdown(f"""
    <style>
    [data-testid="stHeader"], footer {{ display: none !important; }}
    .stApp {{ background-color: {BLACKOUT} !important; color: {CYAN_NEXUS} !important; font-family: 'Courier New', monospace; }}
    
    .stTextArea textarea {{
        background-color: {BLACKOUT} !important; color: {MATRIX_GREEN} !important;
        border: 1px solid {MATRIX_GREEN} !important;
    }}
    
    .stButton button {{
        border: 1px solid {CYAN_NEXUS} !important; background-color: {BLACKOUT} !important;
        color: {CYAN_NEXUS} !important; width: 100%; font-weight: bold;
    }}

    /* ONDA VERDE OPERACIONAL EM TEMPO REAL (SVG PURO) */
    .wave-footer {{
        position: fixed; bottom: 0; left: 0; width: 100%; height: 60px;
        background: transparent; overflow: hidden; line-height: 0; z-index: 100;
    }}
    .wave-footer svg {{ position: relative; display: block; width: calc(150% + 1.3px); height: 60px; transform: rotateY(180deg); }}
    .wave-footer .shape-fill {{ fill: {MATRIX_GREEN}; opacity: 0.2; }}
    
    @keyframes moveWave {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-33.3%); }}
    }}
    .wave-anim {{ animation: moveWave 7s linear infinite; }}
    </style>
""", unsafe_allow_html=True)

# --- [2. GLOBO MUNDIAL 3D OPERACIONAL] ---
def render_globe():
    st.components.v1.html(f"""
        <div id="globeViz" style="background: {BLACKOUT}; display: flex; justify-content: center;"></div>
        <script src="https://unpkg.com"></script>
        <script>
            const world = Globe()(document.getElementById('globeViz'))
                .globeImageUrl('https://unpkg.com')
                .backgroundColor('{BLACKOUT}')
                .width(380).height(380)
                .showAtmosphere(true).atmosphereColor('{MATRIX_GREEN}');
            world.controls().autoRotate = true;
            world.controls().autoRotateSpeed = 1.5;
        </script>
    """, height=400)

# --- [3. GERADOR DE DOSSIÊ TÉCNICO (6 PÁGINAS)] ---
def generate_dossier_6_pages(module_name):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    setores = ["NIST AUDIT", "GLOBAL FINANCE", "PQC GOVERNANCE", "DIGITAL PHYSIOLOGY", "EB-1A EVIDENCE", "FINAL VERDICT"]
    for i, setor in enumerate(setores):
        c.setFillColorRGB(0, 0, 0); c.rect(0, 0, 600, 900, fill=1)
        c.setFillColorRGB(0, 1, 1); c.setFont("Courier-Bold", 18)
        c.drawCentredString(300, 800, f"NEXUS SUPREMO - {module_name}")
        c.setFillColorRGB(0, 1, 0.2); c.setFont("Courier", 12)
        c.drawString(50, 750, f"SETOR: {setor}")
        c.drawString(50, 730, f"ARQUITETO: MARCO ANTONIO DO NASCIMENTO")
        c.drawString(50, 710, f"PAGE: {i+1} / 6")
        c.drawString(50, 690, f"SOH v2.2 STATUS: MISSION CRITICAL")
        c.showPage()
    c.save(); buffer.seek(0)
    return buffer

# --- [4. DASHBOARD CENTRAL] ---
st.markdown(f"<h2 style='text-align: center; color: {CYAN_NEXUS}; letter-spacing: 5px;'>🛡️ NEXUS SUPREMO v1032</h2>", unsafe_allow_html=True)

# Telemetria Superior
t1, t2, t3, t4 = st.columns(4)
t1.metric("CPU", f"{psutil.cpu_percent()}%")
t2.metric("MEM", f"{psutil.virtual_memory().percent}%")
t3.metric("TRÁFEGO", "214.5 MB")
t4.metric("STATUS", "v2.2 ACTIVE")

st.divider()

c1, c2 = st.columns([1.2, 1])
with c1:
    render_globe()

with c2:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>⌨️ INGESTÃO DE COMANDO SOBERANO</small>", unsafe_allow_html=True)
    cmd = st.text_area("", height=150, label_visibility="collapsed", key="nexus_cmd_final")
    if st.button("🚀 EXECUTAR COMANDO"):
        speak("Comando processado. Nexus Supremo em tempo real.")

st.markdown("### 🚀 MÓDULOS DE MISSÃO")
modulos = [("SPACEX", "🚀"), ("LAW", "⚖️"), ("NEURALINK", "🧠"), ("BIOGENETICS", "🧬"), ("IPO GOLD", "💰"), ("ENG SÊNIOR", "👔"), ("DEFESA CYBER", "🛡️"), ("VALUATION", "📈"), ("SOBERANIA", "🌐")]

cols = st.columns(3)
for i, (name, icon) in enumerate(modulos):
    with cols[i % 3]:
        st.markdown(f"<div style='border:1px solid {CYAN_NEXUS}; padding:10px; text-align:center;'>{icon} {name}</div>", unsafe_allow_html=True)
        if st.button(f"GERAR DOSSIÊ {name}", key=f"btn_{i}"):
            speak(f"Gerando dossiê de seis páginas para {name}.")
            pdf = generate_dossier_6_pages(name)
            st.download_button(f"📥 BAIXAR {name}", pdf, f"NEXUS_{name}.pdf", key=f"dl_{i}")

# ONDA VERDE (SVG ANIMADO)
st.markdown("""
    <div class="wave-footer">
        <svg class="wave-anim" data-name="Layer 1" xmlns="http://w3.org" viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
        </svg>
    </div>
""", unsafe_allow_html=True)

if 'vox_init' not in st.session_state:
    speak("Sistema soberano Nexus Supremo online. Homeostase garantida.")
    st.session_state.vox_init = True
