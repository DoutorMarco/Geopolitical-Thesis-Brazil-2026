import streamlit as st
import psutil, time, hashlib, unicodedata
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO
from openai import OpenAI

# --- [1. IDENTIDADE SOBERANA - BLACKOUT TOTAL] ---
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

# --- [ESTÉTICA MATRIX BLINDADA - REMOÇÃO DE BRANCO] ---
st.markdown(f"""
    <style>
    [data-testid="stHeader"], footer, header {{ display: none !important; }}
    .stApp {{ background-color: {BLACKOUT} !important; color: {CYAN_NEXUS} !important; font-family: 'Courier New', monospace; }}
    
    /* Ingestão de Comando - Zero Branco */
    .stTextArea textarea {{
        background-color: {BLACKOUT} !important; color: {MATRIX_GREEN} !important;
        border: 2px solid {MATRIX_GREEN} !important;
    }}
    
    .stButton button, .stDownloadButton button {{
        border: 1px solid {CYAN_NEXUS} !important; background-color: {BLACKOUT} !important;
        color: {CYAN_NEXUS} !important; font-weight: bold !important; width: 100%;
    }}

    /* ONDA VERDE OPERANDO EM TEMPO REAL */
    .wave-container {{
        position: fixed; bottom: 0; left: 0; width: 100%; height: 70px;
        background: transparent; overflow: hidden; z-index: 1000;
    }}
    .wave-container svg {{ width: 200%; height: 70px; animation: moveWave 8s linear infinite; opacity: 0.3; }}
    .shape-fill {{ fill: {MATRIX_GREEN}; }}
    @keyframes moveWave {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}
    </style>
""", unsafe_allow_html=True)

# --- [2. GLOBO MUNDIAL 3D EM TEMPO REAL] ---
def render_sovereign_globe():
    st.components.v1.html(f"""
        <div id="globeViz" style="background: {BLACKOUT}; display: flex; justify-content: center;"></div>
        <script src="https://unpkg.com"></script>
        <script>
            const world = Globe()(document.getElementById('globeViz'))
                .globeImageUrl('https://unpkg.com')
                .backgroundColor('{BLACKOUT}')
                .width(360).height(360)
                .showAtmosphere(true).atmosphereColor('{MATRIX_GREEN}');
            world.controls().autoRotate = true;
            world.controls().autoRotateSpeed = 2.0;
        </script>
    """, height=370)

# --- [3. GERADOR DE DOSSIÊ TÉCNICO (6 PÁGINAS)] ---
def generate_nexus_dossier(name):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    setores = ["SOVEREIGN AUDIT", "GEOPOLITICAL RISK", "TECH SOVEREIGNTY", "BIOMEDICAL INTEGRITY", "EB-1A EVIDENCE", "FINAL VERDICT"]
    for i, setor in enumerate(setores):
        c.setFillColorRGB(0, 0, 0); c.rect(0, 0, 600, 900, fill=1)
        c.setFillColorRGB(0, 1, 1); c.setFont("Courier-Bold", 16)
        c.drawCentredString(300, 800, f"NEXUS SUPREMO v1032 - {name}")
        c.setFillColorRGB(0, 1, 0.25); c.setFont("Courier", 12)
        c.drawString(50, 750, f"SETOR: {setor}")
        c.drawString(50, 730, f"ARQUITETO: MARCO ANTONIO DO NASCIMENTO")
        c.drawString(50, 710, f"PÁGINA: {i+1} / 6")
        c.showPage()
    c.save(); buffer.seek(0)
    return buffer

# --- [4. DASHBOARD OPERACIONAL] ---
st.markdown(f"<h2 style='text-align: center; color: {CYAN_NEXUS};'>🛡️ NEXUS SUPREMO v1032</h2>", unsafe_allow_html=True)

# Telemetria Superior Fixa
t1, t2, t3, t4 = st.columns(4)
t1.metric("CPU CARGA", "29.4%")
t2.metric("MEMÓRIA", "21.5%")
t3.metric("TRAFEGO REDE", "214.5 MB")
t4.metric("STATUS SOH", "v2.2 ACTIVE")

st.divider()

col_left, col_right = st.columns([1, 1.2])
with col_left:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>🌐 GEOPOLITICAL RADIUS ACTIVE</small>", unsafe_allow_html=True)
    render_sovereign_globe()

with col_right:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>⌨️ INGESTÃO DE COMANDO</small>", unsafe_allow_html=True)
    cmd = st.text_area("", height=150, label_visibility="collapsed", key="nexus_final_fix")
    if st.button("🚀 EXECUTAR COMANDO SOBERANO"):
        speak("Comando Nexus Supremo processado. Cérebro GPT 5.4 ativo.")

st.markdown(f"### 🚀 MÓDULOS DE MISSÃO")
modulos = [("SPACEX", "🚀"), ("LAW", "⚖️"), ("NEURALINK", "🧠"), ("BIOGENETICS", "🧬"), ("IPO GOLD", "💰"), ("ENG SÊNIOR", "👔"), ("DEFESA CYBER", "🛡️"), ("VALUATION", "📈"), ("SOBERANIA", "🌐")]

cols = st.columns(3)
for i, (name, icon) in enumerate(modulos):
    with cols[i % 3]:
        st.markdown(f"<div style='border: 1px solid rgba(0,255,255,0.3); padding:10px; text-align:center; color:{MATRIX_GREEN}'><b>{icon} {name}</b></div>", unsafe_allow_html=True)
        if st.button(f"GERAR DOSSIÊ {name}", key=f"btn_{i}"):
            speak(f"Gerando dossiê de seis páginas para {name}.")
            pdf = generate_nexus_dossier(name)
            st.download_button("📥 DOWNLOAD", pdf, f"NEXUS_{name}.pdf", key=f"dl_{i}")

# RODA-PÉ: ONDA VERDE REALTIME
st.markdown("""
    <div class="wave-container">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
        </svg>
    </div>
""", unsafe_allow_html=True)

if 'vox_init' not in st.session_state:
    speak("Nexus Supremo v10 32 online. Mapa global e onda verde operacionais.")
    st.session_state.vox_init = True
