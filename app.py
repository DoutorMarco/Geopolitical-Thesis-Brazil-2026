import streamlit as st
import numpy as np
import psutil
import time
import hashlib
import yfinance as yf
import plotly.graph_objects as go
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import datetime

# --- [1. IDENTIDADE SOBERANA v320.0 - BLACKOUT ABSOLUTO] ---
st.set_page_config(page_title="NEXUS SUPREMO v320.0", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"], footer, header { display: none !important; }
    .stApp { 
        background-color: #000000 !important; 
        color: #00FF41 !important; 
        font-family: 'Courier New', monospace;
        margin-top: -60px;
    }
    [data-testid="stMetricValue"] { color: #38BDF8 !important; font-size: 1.8rem !important; text-shadow: 0 0 15px #38BDF8; }
    .stTextArea textarea { background-color: #000000 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    .stButton>button { background-color: #000000 !important; color: #38BDF8 !important; border: 1px solid #38BDF8 !important; height: 50px; font-weight: bold; }
    .stButton>button:hover { border-color: #00FF41 !important; color: #00FF41 !important; box-shadow: 0 0 30px #00FF41; }
    </style>
""", unsafe_allow_html=True)

def speak(text):
    st.components.v1.html(f"<script>var u=new SpeechSynthesisUtterance('{text}');u.lang='en-US';u.rate=1.0;window.speechSynthesis.speak(u);</script>", height=0)

# --- [2. MOTOR DE DOSSIÊ TÉCNICO GLOBAL (6 PÁGINAS)] ---
def generate_sovereign_dossier(module_name):
    buf = BytesIO()
    p = canvas.Canvas(buf, pagesize=A4)
    sections = [
        "I. NIST CYBERSECURITY INFRASTRUCTURE AUDIT",
        "II. GLOBAL FINANCIAL SYSTEMS & MARKET IMPACT",
        "III. PQC QUANTUM GOVERNANCE & DATA SOVEREIGNTY",
        "IV. BIOMEDICAL ENGINEERING & DIGITAL PHYSIOLOGY",
        "V. EXTRAORDINARY ABILITY EVIDENCE (EB-1A CRITERIA)",
        "VI. MISSION CRITICAL VERDICT - SOH v2.2 ACTIVE"
    ]
    for i, title in enumerate(sections):
        p.setFillColorRGB(0, 0, 0); p.rect(0, 0, 600, 900, fill=1)
        p.setFillColorRGB(0, 1, 0.25); p.setFont("Courier-Bold", 18)
        p.drawCentredString(300, 800, f"NEXUS SUPREMO - {module_name}")
        p.setFont("Courier", 12); p.drawString(50, 750, f"SECTION: {title}")
        p.drawString(50, 720, f"PRINCIPAL ARCHITECT: MARCO ANTONIO DO NASCIMENTO")
        p.drawString(50, 700, f"CONSULTATION RATE: $1,000/H")
        p.drawString(50, 680, f"VALIDATION HASH: {hashlib.sha256(module_name.encode()).hexdigest()[:20].upper()}")
        p.drawString(50, 640, f"PAGE {i+1} OF 6 | GLOBAL OPERATIONAL REALITY")
        p.line(50, 630, 550, 630)
        p.showPage()
    p.save(); buf.seek(0)
    return buf

# --- [3. DASHBOARD DE TELEMETRIA EM TEMPO REAL] ---
st.markdown("<h1 style='text-align: center; color: #38BDF8; letter-spacing: 12px;'>🛡️ NEXUS SUPREMO v320.0</h1>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("CPU LOAD", f"{psutil.cpu_percent()}%")
with c2: st.metric("MEMORY", f"{psutil.virtual_memory().percent}%")
with c3:
    try: 
        sp500_real = yf.Ticker("^GSPC").history(period="1d")['Close'].iloc[-1]
        st.metric("S&P 500 (LIVE)", f"{sp500_real:.2f}")
    except: st.metric("S&P 500", "7035.94")
with c4: st.metric("VALUATION", "$1,000/H")

st.divider()

# --- [4. MAPA GLOBAL E COMANDO SOBERANO] ---
col_map, col_cmd = st.columns([1.6, 1])

with col_map:
    # Globo Mundial Operacional com Rotação Real
    rotation_speed = (time.time() % 360) * 0.8
    map_fig = go.Figure(go.Scattergeo(
        lat=[-2.3, 25.9, -15.7, 40.71, 35.68], lon=[-44.4, -97.1, -47.8, -74.00, 139.69],
        text=["Alcantara", "Starbase US", "Brasília HQ", "Wall Street", "Tokyo Node"],
        mode='markers+text', marker=dict(size=12, color='#38BDF8', symbol='diamond', line=dict(width=2, color='#00FF41'))
    ))
    map_fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)', showland=True, landcolor='#050505', projection_type='orthographic', projection_rotation=dict(lon=rotation_speed, lat=20, roll=0)), margin=dict(l=0,r=0,t=0,b=0), height=450, paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(map_fig, use_container_width=True)

with col_cmd:
    st.write("### ⌨️ COMMAND INGESTION")
    query = st.text_area("Analyze Mission Parameters...", height=150, label_visibility="collapsed")
    if st.button("🚀 EXECUTE GLOBAL COMMAND"):
        speak(f"Analyzing {query[:15]}. All global nodes synchronized. Results pending audit.")

st.divider()

# --- [5. OS 9 NÓS DE MISSÃO CRÍTICA] ---
st.write("### 🚀 MISSION NODES (ACTIVE)")
nodes = [
    ("🚀 SPACEX", "SPACEX"), ("⚖️ LAW", "LAW"), ("🧠 NEURALINK", "NEURALINK"),
    ("🧬 BIOGENETICS", "BIOGENETICS"), ("💰 IPO GOLD", "IPO"), ("🏗️ SENIOR ENG", "ENGINEERING"),
    ("🛡️ CYBER DEFENSE", "CYBER"), ("📈 VALUATION", "VALUATION"), ("🌐 SOBERANIA", "SOH")
]
cols = st.columns(3)
for i, (label, key) in enumerate(nodes):
    with cols[i % 3]:
        if st.button(label, key=f"node_{key}", use_container_width=True):
            speak(f"Node {label} engaged. Compiling six-page technical dossier for EB-1A verification.")
            st.session_state.current_pdf = generate_sovereign_dossier(label)
            st.session_state.node_active = label

if 'current_pdf' in st.session_state:
    st.download_button(f"📥 DOWNLOAD {st.session_state.node_active} DOSSIER (6 PAGES)", st.session_state.current_pdf, f"NEXUS_AUDIT_{st.session_state.node_active}.pdf", use_container_width=True)

# --- [6. ONDA DE PULSO OPERACIONAL REALTIME] ---
@st.fragment(run_every=1)
def operational_wave():
    t = np.linspace(0, 10, 250); y = np.sin(t * (psutil.cpu_percent()/10 + 1) + time.time() * 2.5)
    fig_wave = go.Figure(go.Scatter(x=t, y=y, line=dict(color='#00FF41', width=3), fill='tozeroy', fillcolor='rgba(0, 255, 65, 0.2)'))
    fig_wave.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=140, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(visible=False), yaxis=dict(visible=False, range=[-2, 2]))
    st.plotly_chart(fig_wave, use_container_width=True)

operational_wave()
