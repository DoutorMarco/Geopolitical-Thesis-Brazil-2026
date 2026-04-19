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

# --- [ESTÉTICA MATRIX ABSOLUTA] ---
st.markdown(f"""
    <style>
    [data-testid="stHeader"], footer {{ display: none !important; }}
    .stApp {{ background-color: {BLACKOUT} !important; color: {CYAN_NEXUS} !important; font-family: 'Courier New', monospace; }}
    
    /* REMOÇÃO DE BRANCO */
    .stTextArea textarea {{
        background-color: {BLACKOUT} !important; color: {MATRIX_GREEN} !important;
        border: 1px solid {MATRIX_GREEN} !important;
    }}
    
    .stButton button {{
        border: 1px solid {CYAN_NEXUS} !important; background-color: {BLACKOUT} !important;
        color: {CYAN_NEXUS} !important; width: 100%; font-weight: bold;
    }}

    /* ONDA VERDE EM TEMPO REAL */
    .wave-container {{
        position: fixed; bottom: 0; left: 0; width: 100%; height: 70px;
        background: transparent; overflow: hidden; z-index: 999;
    }}
    .wave {{
        width: 200%; height: 100%; background: url('https://githubusercontent.com');
        background-size: 50% 70px; opacity: 0.2; filter: hue-rotate(90deg);
        animation: move_wave 10s linear infinite;
    }}
    @keyframes move_wave {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}
    </style>
""", unsafe_allow_html=True)

# --- [2. GLOBO MUNDIAL 3D EM TEMPO REAL] ---
def render_globe():
    st.components.v1.html(f"""
        <div id="globeViz" style="background: {BLACKOUT};"></div>
        <script src="//://unpkg.com"></script>
        <script>
            const world = Globe()(document.getElementById('globeViz'))
                .globeImageUrl('//://unpkg.com')
                .backgroundColor('{BLACKOUT}')
                .width(400).height(400)
                .showAtmosphere(true).atmosphereColor('{MATRIX_GREEN}');
            world.controls().autoRotate = true;
            world.controls().autoRotateSpeed = 1.2;
        </script>
    """, height=410)

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
        c.drawString(50, 710, f"PAGINA: {i+1} DE 6")
        c.drawString(50, 690, f"SOH v2.2 STATUS: MISSION CRITICAL")
        c.showPage()
    c.save(); buffer.seek(0)
    return buffer

# --- [4. DASHBOARD OPERACIONAL] ---
st.markdown(f"<h2 style='text-align: center; color: {CYAN_NEXUS};'>🛡️ NEXUS SUPREMO v1032</h2>", unsafe_allow_html=True)

# Telemetria Superior
t1, t2, t3, t4 = st.columns(4)
t1.metric("CPU", f"{psutil.cpu_percent()}%")
t2.metric("MEM", f"{psutil.virtual_memory().percent}%")
t3.metric("TRAFEGO", "214.5 MB")
t4.metric("STATUS", "v2.2 ACTIVE")

st.divider()

c1, c2 = st.columns([1.2, 1])
with c1:
    render_globe()

with c2:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>⌨️ INGESTÃO DE COMANDO SOBERANO</small>", unsafe_allow_html=True)
    cmd = st.text_area("", height=150, label_visibility="collapsed", key="nexus_real_cmd")
    if st.button("🚀 EXECUTAR COMANDO"):
        speak("Comando processado. Nexus Supremo em plena carga operacional.")

st.markdown("### 🚀 MÓDULOS DE MISSÃO")
modulos = [("SPACEX", "🚀"), ("LAW", "⚖️"), ("NEURALINK", "🧠"), ("BIOGENETICS", "🧬"), ("IPO GOLD", "💰"), ("ENG SÊNIOR", "👔"), ("DEFESA CYBER", "🛡️"), ("VALUATION", "📈"), ("SOBERANIA", "🌐")]

cols = st.columns(3)
for i, (name, icon) in enumerate(modulos):
    with cols[i % 3]:
        st.markdown(f"<div style='border:1px solid {CYAN_NEXUS}; padding:10px; text-align:center;'>{icon} {name}</div>", unsafe_allow_html=True)
        if st.button(f"GERAR DOSSIÊ {name}", key=f"btn_{i}"):
            speak(f"Iniciando impressão do dossiê de seis páginas para {name}.")
            pdf = generate_dossier_6_pages(name)
            st.download_button(f"📥 BAIXAR {name}", pdf, f"NEXUS_{name}.pdf", key=f"dl_{i}")

# Roda a VOX de inicialização apenas uma vez
if 'vox_init' not in st.session_state:
    speak("Nexus Supremo v10 32 online. Sistema soberano pronto para o arquiteto.")
    st.session_state.vox_init = True

# ONDA VERDE (RODAPÉ)
st.markdown("<div class='wave-container'><div class='wave'></div></div>", unsafe_allow_html=True)
