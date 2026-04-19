import streamlit as st
import psutil, time, hashlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO
from openai import OpenAI

# --- [1. IDENTIDADE SOBERANA - BLACKOUT TOTAL & CYAN/MATRIX] ---
CYAN_NEXUS = "#00FFFF"
MATRIX_GREEN = "#00FF41"
BLACKOUT = "#000000"

st.set_page_config(page_title="NEXUS SUPREMO v1032", layout="wide")

try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    client = None

# BLINDAGEM ESTÉTICA: REMOÇÃO DE BRANCO E FIXAÇÃO DE CORES
st.markdown(f"""
    <style>
    /* Supressão Total de Elementos Streamlit (Branco Superior) */
    [data-testid="stHeader"], footer, header {{ display: none !important; }}
    .stApp {{ 
        background-color: {BLACKOUT} !important; 
        color: {CYAN_NEXUS} !important; 
        font-family: 'Courier New', monospace;
    }}
    
    /* Ingestão de Comando - Fundo Preto / Borda Verde Matrix */
    .stTextArea textarea {{
        background-color: {BLACKOUT} !important; 
        color: {MATRIX_GREEN} !important;
        border: 2px solid {MATRIX_GREEN} !important;
        border-radius: 4px !important;
    }}
    
    /* Botões e Módulos */
    .stButton button, .stDownloadButton button {{
        border: 1px solid {CYAN_NEXUS} !important; 
        background-color: {BLACKOUT} !important;
        color: {CYAN_NEXUS} !important; 
        font-weight: bold !important;
        text-transform: uppercase;
    }}

    /* Onda de Homeostase Estável no Rodapé */
    .wave-box {{
        position: fixed; bottom: 0; left: 0; width: 100%; height: 60px;
        background: {BLACKOUT}; overflow: hidden; z-index: 1000;
    }}
    .wave-box svg {{ width: 200%; height: 60px; animation: moveWave 12s linear infinite; opacity: 0.2; }}
    .shape-fill {{ fill: {MATRIX_GREEN}; }}
    @keyframes moveWave {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}
    </style>
""", unsafe_allow_html=True)

# --- [2. COMPONENTE: GLOBO MUNDIAL REALTIME (NATIVO)] ---
def render_sovereign_globe():
    # Injeção de script de alta performance para o Mapa Global
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

# --- [3. GERADOR DE DOSSIÊ (6 PÁGINAS - CONSOLIDADO)] ---
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
st.markdown(f"<h2 style='text-align: center; color: {CYAN_NEXUS}; letter-spacing: 2px;'>🛡️ NEXUS SUPREMO v1032</h2>", unsafe_allow_html=True)

# Telemetria Superior Fixa
t1, t2, t3, t4 = st.columns(4)
t1.metric("CPU CARGA", "29.4%")
t2.metric("MEMÓRIA", "21.5%")
t3.metric("TRÁFEGO REDE", "214.5 MB")
t4.metric("STATUS SOH", "v2.2 ACTIVE")

st.divider()

col_globe, col_cmd = st.columns([1, 1.2])
with col_globe:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>🌐 GEOPOLITICAL RADIUS ACTIVE</small>", unsafe_allow_html=True)
    render_sovereign_globe()

with col_cmd:
    st.markdown(f"<small style='color:{MATRIX_GREEN}'>⌨️ INGESTÃO DE COMANDO</small>", unsafe_allow_html=True)
    cmd = st.text_area("", height=150, label_visibility="collapsed", key="nexus_cmd_definitivo")
    if st.button("🚀 EXECUTAR COMANDO SOBERANO"):
        st.components.v1.html(f"<script>var u=new SpeechSynthesisUtterance('Comando Nexus Processado.');u.lang='pt-BR';window.speechSynthesis.speak(u);</script>", height=0)

st.markdown(f"### 🚀 MÓDULOS DE MISSÃO")
modulos = [
    ("SPACEX", "🚀"), ("LAW", "⚖️"), ("NEURALINK", "🧠"),
    ("BIOGENETICS", "🧬"), ("IPO GOLD", "💰"), ("ENG SÊNIOR", "👔"),
    ("DEFESA CYBER", "🛡️"), ("VALUATION", "📈"), ("SOBERANIA", "🌐")
]

cols = st.columns(3)
for i, (name, icon) in enumerate(modulos):
    with cols[i % 3]:
        st.markdown(f"<div style='border: 1px solid rgba(0,255,255,0.3); padding:10px; text-align:center; color:{MATRIX_GREEN}'><b>{icon} {name}</b></div>", unsafe_allow_html=True)
        if st.button(f"GERAR DOSSIÊ {name}", key=f"btn_{i}"):
            pdf = generate_dossier_v1032(name)
            st.download_button("📥 DOWNLOAD", pdf, f"NEXUS_{name}.pdf", key=f"dl_{i}")

# RODA-PÉ: ONDA VERDE REALTIME (SVG BLINDADO)
st.markdown("""
    <div class="wave-box">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
        </svg>
    </div>
""", unsafe_allow_html=True)
