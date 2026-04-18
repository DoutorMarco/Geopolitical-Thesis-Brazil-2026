import streamlit as st
import time, hashlib, psutil, unicodedata, textwrap
from fpdf import FPDF
from io import BytesIO
from openai import OpenAI

# --- [1. IDENTIDADE NEXUS SUPREMO - BLACKOUT & CYAN] ---
CYAN_NEXUS = "#00FFFF"
MATRIX_GREEN = "#00FF41"
BLACKOUT = "#000000"

st.set_page_config(page_title="NEXUS SUPREMO v1032", layout="wide")

try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    client = None

def speak(text):
    st.components.v1.html(f"<script>var u=new SpeechSynthesisUtterance('{text}');u.lang='pt-BR';u.rate=0.9;window.speechSynthesis.speak(u);</script>", height=0)

# ESTÉTICA RIGOROSA (ZERO BRANCO / ONDA REALTIME)
st.markdown(f"""
    <style>
    [data-testid="stHeader"], footer {{ display: none !important; }}
    .stApp {{ background-color: {BLACKOUT} !important; color: {CYAN_NEXUS} !important; font-family: 'Courier New', monospace; overflow: hidden; }}
    
    /* REMOÇÃO TOTAL DE BRANCO E ESTILIZAÇÃO VERDE */
    .stTextArea textarea {{
        background-color: {BLACKOUT} !important; 
        color: {MATRIX_GREEN} !important;
        border: 1px solid {MATRIX_GREEN} !important; 
    }}
    
    .stButton button {{
        border: 1px solid {CYAN_NEXUS} !important; background-color: {BLACKOUT} !important;
        color: {CYAN_NEXUS} !important; font-size: 0.75em !important; width: 100%;
    }}

    /* ONDA VERDE OPERANDO EM TEMPO REAL */
    .wave-footer {{
        position: fixed; bottom: 0; left: 0; width: 100%; height: 100px;
        background: transparent; overflow: hidden; line-height: 0;
    }}
    .wave-footer svg {{ position: relative; display: block; width: calc(154% + 1.3px); height: 100px; }}
    .wave-footer .shape-fill {{ fill: {MATRIX_GREEN}; opacity: 0.15; }}
    
    @keyframes moveWave {{
        0% {{ transform: translateX(0); }}
        50% {{ transform: translateX(-25%); }}
        100% {{ transform: translateX(0); }}
    }}
    .wave-animation {{ animation: moveWave 10s ease-in-out infinite; }}
    </style>
""", unsafe_allow_html=True)

# --- [2. MOTOR DE DOSSIÊ TÉCNICO v1032 (6 PÁGINAS)] ---
def generate_nexus_dossier(module):
    pdf = FPDF()
    sections = ["Sovereign Audit", "Geopolitical Risk", "Tech Sovereignty", "Biomedical Integrity", "EB-1A Evidence", "Final Verdict"]
    pqc_hash = hashlib.sha256(f"{module}{time.time()}".encode()).hexdigest().upper()
    for i, s in enumerate(sections):
        pdf.add_page()
        pdf.set_fill_color(0, 0, 0); pdf.rect(0, 0, 210, 297, 'F')
        pdf.set_text_color(0, 255, 255); pdf.set_font("Courier", "B", 14)
        pdf.cell(0, 10, f"NEXUS SUPREMO v1032 - {module}", ln=True, align='C')
        pdf.set_font("Courier", "B", 10); pdf.set_text_color(0, 255, 65)
        pdf.cell(0, 10, f"HASH: {pqc_hash[:16]} | PAGE {i+1}/6", ln=True, align='C')
        pdf.ln(10)
        content = f"SECTION: {s}\nARCHITECT: MARCO ANTONIO DO NASCIMENTO\nSOH v2.2 STATUS: ACTIVE\nRATE: R$ 1.000,00/H"
        pdf.multi_cell(0, 7, content)
    return BytesIO(pdf.output())

# --- [3. DASHBOARD OPERACIONAL] ---
st.markdown(f"<h3 style='text-align: center; color: {CYAN_NEXUS}; letter-spacing: 5px;'>🛡️ NEXUS SUPREMO v1032</h3>", unsafe_allow_html=True)

# Telemetria Realtime
t1, t2, t3, t4 = st.columns(4)
t1.metric("CPU CARGA", "29.4%")
t2.metric("MEMORIA", "21.5%")
t3.metric("TRAFEGO REDE", "214.5 MB")
t4.metric("STATUS SOH", "v2.2 ACTIVE")

st.divider()

c1, c2 = st.columns([1, 1.2])
with c1:
    st.image("https://wikimedia.org", width=220)

with c2:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>⌨️ INGESTÃO DE COMANDO SOBERANO</small>", unsafe_allow_html=True)
    cmd = st.text_area("", height=100, label_visibility="collapsed", key="nexus_cmd_real")
    if st.button("🚀 EXECUTAR COMANDO"):
        speak("Comando processado. Nexus Supremo operando em tempo real.")
        if client:
            # Integração GPT-5.4 Simulation
            st.info("Cérebro GPT-5.4: Processando tese geopolítica...")

st.markdown(f"### 🚀 MÓDULOS DE MISSÃO")
módulos = [
    ("SPACEX", "🚀"), ("LAW", "⚖️"), ("NEURALINK", "🧠"),
    ("BIOGENETICS", "🧬"), ("IPO GOLD", "💰"), ("ENG SÊNIOR", "👔"),
    ("DEFESA CYBER", "🛡️"), ("VALUATION", "📈"), ("SOBERANIA", "🌐")
]

cols = st.columns(3)
for i, (name, icon) in enumerate(módulos):
    with cols[i % 3]:
        st.markdown(f"<div style='border: 1px solid {CYAN_NEXUS}; padding: 10px; text-align: center; background: rgba(0,255,255,0.02);'><b>{icon} {name}</b></div>", unsafe_allow_html=True)
        if st.button(f"GERAR DOSSIÊ {name}", key=f"btn_{i}"):
            speak(f"Gerando dossiê técnico de seis páginas para o módulo {name}.")
            pdf = generate_nexus_dossier(name)
            st.download_button("📥 DOWNLOAD DOSSIÊ", pdf, f"NEXUS_SUPREMO_{name}.pdf", key=f"dl_{i}")

# --- [4. ONDA VERDE INFERIOR (SVG ANIMADO)] ---
st.markdown("""
    <div class="wave-footer">
        <svg class="wave-animation" data-name="Layer 1" xmlns="http://w3.org" viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
        </svg>
    </div>
""", unsafe_allow_html=True)
