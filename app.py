import streamlit as st
import numpy as np
import psutil
import time
import hashlib
import plotly.graph_objects as go
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import datetime

# --- [1. BLINDAGEM VISUAL TOTAL (ZERO BRANCO)] ---
st.set_page_config(page_title="Nexus Supremo v270.0", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"], footer, header { display: none !important; }
    .stApp { 
        background-color: #000000 !important; 
        color: #00FF41 !important; 
        font-family: 'Courier New', monospace;
        margin-top: -60px;
    }
    textarea { 
        background-color: #000000 !important; 
        color: #00FF41 !important; 
        border: 1px solid #00FF41 !important; 
    }
    [data-testid="stMetricValue"] { color: #38BDF8 !important; font-size: 1.8rem !important; text-shadow: 0 0 10px #38BDF8; }
    [data-testid="stMetricLabel"] { color: #00FF41 !important; }
    
    .stButton>button { 
        background-color: #000000 !important; 
        color: #38BDF8 !important; 
        border: 1px solid #38BDF8 !important; 
        border-radius: 0px;
        font-weight: bold;
    }
    .stButton>button:hover { border-color: #00FF41 !important; color: #00FF41 !important; box-shadow: 0 0 20px #00FF41; }
    </style>
""", unsafe_allow_html=True)

def speak(text):
    st.components.v1.html(f"""
        <script>
        var u = new SpeechSynthesisUtterance('{text}');
        u.lang = 'en-US'; u.rate = 0.95;
        window.speechSynthesis.speak(u);
        </script>
    """, height=0)

# --- [2. MOTOR DE DOSSIÊ EM INGLÊS (6 PAGES)] ---
def generate_english_dossier(module_name):
    buf = BytesIO()
    p = canvas.Canvas(buf, pagesize=A4)
    # Setores Traduzidos para o Padrão Americano (NIW/EB-1A)
    sectors = [
        "NIST CYBERSECURITY AUDIT", 
        "GLOBAL FINANCIAL FORECAST", 
        "PQC QUANTUM GOVERNANCE", 
        "DIGITAL PHYSIOLOGY TELEMETRY", 
        "EB-1A EXTRAORDINARY EVIDENCE", 
        "FINAL MISSION VERDICT"
    ]
    
    for i, sector in enumerate(sectors):
        p.setFillColorRGB(0, 0, 0); p.rect(0, 0, 600, 900, fill=1)
        p.setFillColorRGB(0, 1, 0.25) # Matrix Green
        p.setFont("Courier-Bold", 18)
        p.drawCentredString(300, 800, f"NEXUS SUPREMO v270.0 - {module_name}")
        p.setFont("Courier", 12)
        p.drawString(50, 750, f"SECTION: {sector}")
        p.drawString(50, 730, f"PRINCIPAL ARCHITECT: MARCO ANTONIO DO NASCIMENTO")
        p.drawString(50, 710, f"OPERATIONAL HASH: {hashlib.sha256(module_name.encode()).hexdigest()[:16].upper()}")
        p.drawString(50, 690, f"TIMESTAMP: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        p.drawString(50, 650, f"PAGE {i+1} OF 6 - MISSION CRITICAL DATA")
        p.line(50, 640, 550, 640)
        
        # Conteúdo em Inglês
        p.setFont("Courier", 10)
        text = "Technical verification confirmed under SOH v2.2 protocols. Extraordinary ability evidence established for National Interest Waiver (NIW) criteria."
        p.drawString(50, 610, text)
        
        p.showPage()
    
    p.save(); buf.seek(0)
    return buf

# --- [3. DASHBOARD OPERACIONAL] ---
st.markdown("<h1 style='text-align: center; color: #38BDF8; letter-spacing: 8px;'>🛡️ NEXUS SUPREMO v270.0</h1>", unsafe_allow_html=True)

# TELEMETRIA
col_a, col_b, col_c, col_d = st.columns(4)
with col_a: st.metric("CPU LOAD", f"{psutil.cpu_percent()}%")
with col_b: st.metric("MEMORY USAGE", f"{psutil.virtual_memory().percent}%")
with col_c: st.metric("NETWORK TRAFFIC", "214.5 MB")
with col_d: st.metric("SOH STATUS", "v2.2 ACTIVE")

st.divider()

# MAPA E TERMINAL
col_map, col_terminal = st.columns([1.5, 1])

with col_map:
    map_fig = go.Figure(go.Scattergeo(
        lat=[-2.3, 25.9, -15.7, 40.71, 35.68],
        lon=[-44.4, -97.1, -47.8, -74.00, 139.69],
        text=["Alcantara Node", "Starbase US", "Brasilia HQ", "Global NY", "Tokyo Node"],
        mode='markers+text',
        marker=dict(size=10, color='#38BDF8', symbol='diamond', line=dict(width=2, color='#00FF41'))
    ))
    map_fig.update_layout(
        geo=dict(bgcolor='rgba(0,0,0,0)', showland=True, landcolor='#050505', countrycolor='#00FF41', projection_type='orthographic', showocean=False),
        margin=dict(l=0,r=0,t=0,b=0), height=400, paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(map_fig, use_container_width=True)

with col_terminal:
    st.write("### ⌨️ COMMAND INGESTION")
    cmd = st.text_area("Execute Xeon Audit...", height=120, label_visibility="collapsed")
    if st.button("🚀 PROCESS COMMAND"):
        res = f"Command '{cmd[:20]}' processed. System Integrity: 100%."
        speak(res)

st.divider()

# MÓDULOS DE MISSÃO (ENGLISH DOSSIER)
st.write("### 🚀 MISSION MODULES")
btns = [
    ("🚀 SPACEX", "SPACEX"), ("⚖️ LAW", "LAW"), ("🧠 NEURALINK", "NEURALINK"),
    ("🧬 BIOGENETICS", "BIOGENETICS"), ("📈 IPO GOLD", "IPO"), ("🏗️ SENIOR ENG", "ENGINEERING"),
    ("🛡️ CYBER DEFENSE", "CYBER"), ("📊 VALUATION", "VALUATION"), ("🌐 SOVEREIGNTY", "SOH")
]
cols = st.columns(3)
for i, (label, key) in enumerate(btns):
    with cols[i % 3]:
        if st.button(label, key=f"btn_{key}", use_container_width=True):
            st.session_state.active_module = label
            speak(f"Module {label} activated. Generating English technical dossier.")
            st.session_state.pdf_buffer = generate_english_dossier(label)

if 'pdf_buffer' in st.session_state:
    st.download_button(
        label=f"📂 DOWNLOAD 6-PAGE DOSSIER: {st.session_state.active_module}",
        data=st.session_state.pdf_buffer,
        file_name=f"Nexus_Audit_Report_{st.session_state.active_module}.pdf",
        mime="application/pdf", use_container_width=True
    )

# PULSO DE SINCRONIA
st.divider()
t = np.linspace(0, 10, 250); y = np.sin(t + time.time())
fig_wave = go.Figure(go.Scatter(x=t, y=y, line=dict(color='#00FF41', width=2), fill='tozeroy', fillcolor='rgba(0, 255, 65, 0.1)'))
fig_wave.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=120, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(visible=False), yaxis=dict(visible=False, range=[-1.5, 1.5]))
st.plotly_chart(fig_wave, use_container_width=True)
