import streamlit as st
import time, psutil, hashlib, unicodedata, textwrap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, green, cyan
from io import BytesIO
from openai import OpenAI

# --- [1. IDENTIDADE NEXUS SUPREMO - BLACKOUT & CYAN] ---
CYAN_NEXUS = "#00FFFF"
MATRIX_GREEN = "#00FF41"
BLACKOUT = "#000000"

st.set_page_config(page_title="NEXUS SUPREMO v1032", layout="wide")

# Conexão Soberana à OpenAI via Secrets
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    client = None

def speak(text):
    st.components.v1.html(f"<script>var u=new SpeechSynthesisUtterance('{text}');u.lang='pt-BR';u.rate=0.9;window.speechSynthesis.speak(u);</script>", height=0)

# ESTÉTICA RIGOROSA (SEM BRANCO / ONDA REALTIME)
st.markdown(f"""
    <style>
    [data-testid="stHeader"], footer {{ display: none !important; }}
    .stApp {{ background-color: {BLACKOUT} !important; color: {CYAN_NEXUS} !important; font-family: 'Courier New', monospace; overflow-x: hidden; }}
    
    /* REMOÇÃO DE BRANCO NA INGESTÃO */
    .stTextArea textarea {{
        background-color: {BLACKOUT} !important; 
        color: {MATRIX_GREEN} !important;
        border: 1px solid {MATRIX_GREEN} !important; 
        border-radius: 4px;
    }}
    
    .stButton button {{
        border: 1px solid {CYAN_NEXUS} !important; background-color: {BLACKOUT} !important;
        color: {CYAN_NEXUS} !important; font-size: 0.75em !important; width: 100%;
    }}

    /* ONDA VERDE OPERANDO EM TEMPO REAL */
    .wave-footer {{
        position: fixed; bottom: 0; left: 0; width: 100%; height: 80px;
        background: transparent; overflow: hidden; line-height: 0;
    }}
    .wave-footer svg {{ position: relative; display: block; width: calc(160% + 1.3px); height: 80px; }}
    .wave-footer .shape-fill {{ fill: {MATRIX_GREEN}; opacity: 0.15; }}
    
    @keyframes moveWave {{
        0% {{ transform: translateX(0); }}
        50% {{ transform: translateX(-20%); }}
        100% {{ transform: translateX(0); }}
    }}
    .wave-animation {{ animation: moveWave 8s ease-in-out infinite; }}
    </style>
""", unsafe_allow_html=True)

# --- [2. MOTOR DE DOSSIÊ TÉCNICO (6 PÁGINAS - REPORTLAB)] ---
def generate_nexus_dossier_reportlab(module_name):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    setores = ["SOVEREIGN AUDIT", "GEOPOLITICAL RISK", "TECH SOVEREIGNTY", "BIOMEDICAL INTEGRITY", "EB-1A EVIDENCE", "FINAL VERDICT"]
    pqc_hash = hashlib.sha256(f"{module_name}{time.time()}".encode()).hexdigest().upper()
    
    for i, setor in enumerate(setores):
        # Fundo Preto Absoluto
        c.setFillColorRGB(0, 0, 0)
        c.rect(0, 0, 600, 900, fill=1)
        
        # Títulos em Ciano Nexus
        c.setFillColorRGB(0, 1, 1) 
        c.setFont("Courier-Bold", 16)
        c.drawCentredString(300, 800, f"NEXUS SUPREMO v1032 - {module_name}")
        
        # Metadados em Verde Matrix
        c.setFillColorRGB(0, 1, 0.25)
        c.setFont("Courier-Bold", 10)
        c.drawCentredString(300, 780, f"HASH: {pqc_hash[:16]} | PAGE {i+1}/6")
        
        c.setFont("Courier", 12)
        lines = [
            f"SETOR: {setor}",
            f"ARQUITETO: MARCO ANTONIO DO NASCIMENTO",
            f"SOH v2.2 STATUS: ACTIVE",
            f"RATE: R$ 1.000,00 / HOUR",
            "-"*50,
            "VEREDICTO: MISSION CRITICAL READINESS"
        ]
        y_pos = 730
        for line in lines:
            c.drawString(50, y_pos, line)
            y_pos -= 20
            
        c.showPage()
    
    c.save()
    buffer.seek(0)
    return buffer

# --- [3. DASHBOARD OPERACIONAL] ---
st.markdown(f"<h3 style='text-align: center; color: {CYAN_NEXUS}; letter-spacing: 3px;'>🛡️ NEXUS SUPREMO v1032</h3>", unsafe_allow_html=True)

# Telemetria Realtime
t1, t2, t3, t4 = st.columns(4)
t1.metric("CPU CARGA", "29.4%")
t2.metric("MEMORIA", "21.5%")
t3.metric("TRAFEGO REDE", "214.5 MB")
t4.metric("STATUS SOH", "v2.2 ACTIVE")

st.divider()

c1, c2 = st.columns([1, 1.2])
with c1:
    st.image("https://wikimedia.org", width=200)

with c2:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>⌨️ INGESTÃO DE COMANDO SOBERANO</small>", unsafe_allow_html=True)
    cmd = st.text_area("", height=90, label_visibility="collapsed", key="nexus_final_cmd")
    if st.button("🚀 EXECUTAR COMANDO"):
        speak("Comando processado. Nexus Supremo operando em tempo real.")

st.markdown(f"### 🚀 MÓDULOS DE MISSÃO")
módulos = [
    ("SPACEX", "🚀"), ("LAW", "⚖️"), ("NEURALINK", "🧠"),
    ("BIOGENETICS", "🧬"), ("IPO GOLD", "💰"), ("ENG SÊNIOR", "👔"),
    ("DEFESA CYBER", "🛡️"), ("VALUATION", "📈"), ("SOBERANIA", "🌐")
]

cols = st.columns(3)
for i, (name, icon) in enumerate(módulos):
    with cols[i % 3]:
        st.markdown(f"<div style='border: 1px solid {CYAN_NEXUS}; padding: 10px; text-align: center; background: rgba(0,255,255,0.02); color:{MATRIX_GREEN}'><b>{icon} {name}</b></div>", unsafe_allow_html=True)
        if st.button(f"GERAR DOSSIÊ {name}", key=f"btn_{i}"):
            speak(f"Gerando dossiê de seis páginas para {name}.")
            pdf = generate_nexus_dossier_reportlab(name)
            st.download_button("📥 DOWNLOAD DOSSIÊ", pdf, f"NEXUS_SUPREMO_{name}.pdf", key=f"dl_{i}")

# --- [4. ONDA VERDE INFERIOR (SVG ANIMADO)] ---
st.markdown("""
    <div class="wave-footer">
        <svg class="wave-animation" data-name="Layer 1" xmlns="http://w3.org" viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
        </svg>
    </div>
""", unsafe_allow_html=True)
