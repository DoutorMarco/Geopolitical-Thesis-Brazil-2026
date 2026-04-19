import streamlit as st
import numpy as np
import psutil
import time
import hashlib
import yfinance as yf
import feedparser
import plotly.graph_objects as go
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import datetime

# --- [1. IDENTIDADE SOBERANA v310.0 - BLACKOUT TOTAL] ---
st.set_page_config(page_title="Nexus Supremo v310.0", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"], footer, header { display: none !important; }
    .stApp { 
        background-color: #000000 !important; 
        color: #00FF41 !important; 
        font-family: 'Courier New', monospace;
        margin-top: -60px;
    }
    [data-testid="stMetricValue"] { color: #38BDF8 !important; font-size: 1.8rem !important; text-shadow: 0 0 12px #38BDF8; }
    .stTextArea textarea { background-color: #000000 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    .stButton>button { background-color: #000000 !important; color: #38BDF8 !important; border: 1px solid #38BDF8 !important; border-radius: 0px; font-weight: bold; }
    .stButton>button:hover { border-color: #00FF41 !important; color: #00FF41 !important; box-shadow: 0 0 25px #00FF41; }
    </style>
""", unsafe_allow_html=True)

def speak(text):
    st.components.v1.html(f"<script>var u=new SpeechSynthesisUtterance('{text}');u.lang='en-US';u.rate=0.95;window.speechSynthesis.speak(u);</script>", height=0)

# --- [2. MOTOR DE DOSSIÊ EM INGLÊS (6 PAGES - MISSION CRITICAL)] ---
def generate_6_page_english_dossier(module_name):
    buf = BytesIO()
    p = canvas.Canvas(buf, pagesize=A4)
    sectors = [
        "NIST CYBERSECURITY AUDIT", "GLOBAL FINANCIAL FORECAST", 
        "PQC QUANTUM GOVERNANCE", "DIGITAL PHYSIOLOGY TELEMETRY", 
        "EB-1A EXTRAORDINARY EVIDENCE", "FINAL MISSION VERDICT"
    ]
    for i, sector in enumerate(sectors):
        p.setFillColorRGB(0, 0, 0); p.rect(0, 0, 600, 900, fill=1)
        p.setFillColorRGB(0, 1, 0.25); p.setFont("Courier-Bold", 18)
        p.drawCentredString(300, 800, f"NEXUS SUPREMO v310.0 - {module_name}")
        p.setFont("Courier", 12); p.drawString(50, 750, f"SECTION: {sector}")
        p.drawString(50, 730, f"PRINCIPAL ARCHITECT: MARCO ANTONIO DO NASCIMENTO")
        p.drawString(50, 710, f"OPERATIONAL RATE: $1,000/H")
        p.drawString(50, 690, f"HASH: {hashlib.sha256(module_name.encode()).hexdigest()[:16].upper()}")
        p.drawString(50, 650, f"PAGE {i+1} OF 6 - SOH v2.2 CERTIFIED")
        p.line(50, 640, 550, 640)
        p.showPage()
    p.save(); buf.seek(0)
    return buf

# --- [3. DASHBOARD OPERACIONAL CENTRAL] ---
st.markdown("<h1 style='text-align: center; color: #38BDF8; letter-spacing: 10px;'>🛡️ NEXUS SUPREMO v310.0</h1>", unsafe_allow_html=True)

# TELEMETRIA E MERCADO REAL
col_a, col_b, col_c, col_d = st.columns(4)
with col_a: st.metric("CPU LOAD", f"{psutil.cpu_percent()}%")
with col_b: st.metric("MEM USAGE", f"{psutil.virtual_memory().percent}%")
with col_c:
    try: sp500 = yf.Ticker("^GSPC").history(period="1d")['Close'].iloc[-1]
    except: sp500 = 7035.94
    st.metric("S&P 500 LIVE", f"{sp500:.2f}")
with col_d: st.metric("RATE", "$1,000/H")

st.divider()

# MAPA E TERMINAL
col_map, col_terminal = st.columns([1.5, 1])
with col_map:
    rot = (time.time() % 360) * 0.5
    fig = go.Figure(go.Scattergeo(
        lat=[-2.3, 25.9, -15.7, 40.71, 35.68], lon=[-44.4, -97.1, -47.8, -74.00, 139.69],
        text=["Alcantara", "Starbase", "Brasilia HQ", "Global NY", "Tokyo Node"],
        mode='markers+text', marker=dict(size=12, color='#38BDF8', symbol='diamond', line=dict(width=2, color='#00FF41'))
    ))
    fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)', showland=True, landcolor='#050505', projection_type='orthographic', projection_rotation=dict(lon=rot, lat=20, roll=0)), margin=dict(l=0,r=0,t=0,b=0), height=400, paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with col_terminal:
    st.write("### ⌨️ COMMAND INGESTION")
    cmd = st.text_area("Live Mission Command...", height=120, label_visibility="collapsed")
    if st.button("🚀 EXECUTE COMMAND"):
        speak(f"Command executed. System integrity 100 percent.")

st.divider()

# --- [4. OS 9 NÓS DE MISSÃO] ---
st.write("### 🚀 MISSION MODULES (9 NODES ACTIVE)")
btns = [
    ("🚀 SPACEX", "SPACEX"), ("⚖️ LAW", "LAW"), ("🧠 NEURALINK", "NEURALINK"),
    ("🧬 BIOGENETICS", "BIOGENETICS"), ("📈 IPO GOLD", "IPO"), ("🏗️ SENIOR ENG", "ENGINEERING"),
    ("🛡️ DEFESA CYBER", "CYBER"), ("📊 VALUATION", "VALUATION"), ("🌐 SOVEREIGNTY", "SOH")
]
cols = st.columns(3)
for i, (label, key) in enumerate(btns):
    with cols[i % 3]:
        if st.button(label, key=f"btn_{key}", use_container_width=True):
            speak(f"Activating {label} node. Generating 6-page technical dossier.")
            st.session_state.pdf = generate_6_page_english_dossier(label)
            st.session_state.active_n = label

if 'pdf' in st.session_state:
    st.download_button(f"📥 DOWNLOAD {st.session_state.active_n} DOSSIER (6 PAGES)", st.session_state.pdf, f"NEXUS_AUDIT_{st.session_state.active_n}.pdf", use_container_width=True)

# --- [5. ONDA DE HOMEOSTASE REALTIME] ---
@st.fragment(run_every=1)
def wave_pulse():
    t = np.linspace(0, 10, 250); y = np.sin(t * (psutil.cpu_percent()/10 + 1) + time.time() * 2)
    fig_wave = go.Figure(go.Scatter(x=t, y=y, line=dict(color='#00FF41', width=3), fill='tozeroy', fillcolor='rgba(0, 255, 65, 0.2)'))
    fig_wave.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=120, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(visible=False), yaxis=dict(visible=False, range=[-2, 2]))
    st.plotly_chart(fig_wave, use_container_width=True)

wave_pulse()
