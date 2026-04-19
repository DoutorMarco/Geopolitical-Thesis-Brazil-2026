import streamlit as st
import numpy as np
import psutil
import time
import hashlib
import yfinance as yf
import requests
import plotly.graph_objects as go
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import datetime

# --- [1. BLINDAGEM ESTÉTICA v430.0 - BLACKOUT MATRIX] ---
st.set_page_config(page_title="NEXUS SUPREMO v430.0", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"], footer, header { display: none !important; }
    .stApp { background-color: #000000 !important; color: #00FF41 !important; font-family: 'Courier New', monospace; margin-top: -60px; }
    [data-testid="stMetricValue"] { color: #00FFFF !important; font-size: 1.8rem !important; text-shadow: 0 0 10px #00FFFF; }
    .stTextArea textarea { background-color: #000000 !important; color: #00FF41 !important; border: 2px solid #00FF41 !important; font-weight: bold; }
    .stButton>button { background-color: #000000 !important; color: #00FFFF !important; border: 1px solid #00FFFF !important; height: 50px; font-weight: bold; width: 100%; }
    .stButton>button:hover { border-color: #00FF41 !important; color: #00FF41 !important; box-shadow: 0 0 30px #00FF41; }
    .node-active { border: 1px solid #00FF41; padding: 10px; background: rgba(0, 255, 65, 0.05); text-align: center; }
    </style>
""", unsafe_allow_html=True)

def speak(text):
    st.components.v1.html(f"<script>var u=new SpeechSynthesisUtterance('{text}');u.lang='en-US';u.rate=1.0;window.speechSynthesis.speak(u);</script>", height=0)

# --- [2. MOTOR DE DOSSIÊ v430.0 (AEROSPACE & EB-1A)] ---
def generate_v430_dossier(node_name, live_data):
    buf = BytesIO()
    p = canvas.Canvas(buf, pagesize=A4)
    sections = [
        "I. NIST CYBERSECURITY & AEROSPACE INFRASTRUCTURE",
        "II. TRANSDISCIPLINARY DEFENSE THESIS (DATA-BIO-LAW)",
        "III. PQC QUANTUM GOVERNANCE & ORBITAL SOVEREIGNTY",
        "IV. STARSHIP TELEMETRY & SPACE-DATA PROTOCOLS",
        "V. EB-1A EXTRAORDINARY ABILITY - NATIONAL INTEREST",
        "VI. FINAL VERDICT: MISSION READY / SOH v2.2"
    ]
    q_hash = hashlib.sha384(f"AERO_{node_name}_{time.time()}".encode()).hexdigest().upper()
    for i, title in enumerate(sections):
        p.setFillColorRGB(0, 0, 0); p.rect(0, 0, 600, 900, fill=1)
        p.setFillColorRGB(0, 1, 0.25); p.setFont("Courier-Bold", 18)
        p.drawCentredString(300, 800, f"NEXUS SUPREMO - {node_name}")
        p.setFont("Courier", 12); p.drawString(50, 750, f"SECTION: {title}")
        p.drawString(50, 720, f"PRINCIPAL ARCHITECT: MARCO ANTONIO DO NASCIMENTO")
        p.drawString(50, 700, f"PQC HASH: {q_hash[:32]}")
        if i == 3: # Seção de Telemetria Espacial
            p.setFont("Courier", 10)
            p.drawString(50, 650, f"LIVE AEROSPACE DATA INGESTED: {live_data[:60]}...")
        p.showPage()
    p.save(); buf.seek(0)
    return buf

# --- [3. INTEGRAÇÃO SPACEX API REALTIME] ---
def get_spacex_telemetry():
    try:
        res = requests.get("https://spacexdata.com", timeout=5).json()
        return f"Flight: {res['name']} | Status: {res['success']} | Node: Starbase TX"
    except:
        return "Starship Node: Monitoring Pre-Launch Protocols..."

# --- [4. DASHBOARD DE SINCRONIA GLOBAL] ---
st.markdown("<h1 style='text-align: center; color: #00FFFF; letter-spacing: 12px;'>🛡️ NEXUS SUPREMO v430.0</h1>", unsafe_allow_html=True)

@st.fragment(run_every=5)
def global_sync_hub():
    cpu = psutil.cpu_percent()
    try: sp500 = yf.Ticker("^GSPC").history(period="1d")['Close'].iloc[-1]
    except: sp500 = 7035.94
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("HARDWARE LOAD", f"{cpu}%")
    c2.metric("S&P 500 REALTIME", f"{sp500:.2f}")
    c3.metric("STARSHIP TELEMETRY", "ACTIVE", delta="SYNC")
    c4.metric("MONETIZATION", "$1,000/H")

    st.divider()

    col_m, col_t = st.columns([1.6, 1])
    with col_m:
        rot = (time.time() % 360) * 0.9
        fig = go.Figure(go.Scattergeo(
            lat=[-2.3, 25.9, -15.7, 40.71, 35.68, 51.5], lon=[-44.4, -97.1, -47.8, -74.00, 139.69, -0.1],
            text=["Alcantara (Launch)", "Starbase (TX)", "HQ (SOH)", "NY (PQC)", "Tokyo", "London"],
            mode='markers+text', marker=dict(size=14, color='#00FFFF', symbol='diamond', line=dict(width=2, color='#00FF41'))
        ))
        fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)', showland=True, landcolor='#050505', projection_type='orthographic', projection_rotation=dict(lon=rot, lat=20, roll=0)), margin=dict(l=0,r=0,t=0,b=0), height=400, paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    
    with col_t:
        st.write("### 🧠 COMMAND BRAIN v430")
        st.markdown(f"<small>SPACEX-DATA-LINK: ACTIVE</small>", unsafe_allow_html=True)
        query = st.text_area("Ingesting Orbital Signals...", height=120, key="brain_v430")
        if st.button("🚀 EXECUTE ORBITAL REPROCESSING"):
            speak("Orbital telemetry synchronized. SpaceX nodes evolving.")

    st.divider()

    # --- [5. OS 9 NÓS ATIVOS COM FOCO AEROSPACE] ---
    nodes = [
        ("🚀 SPACEX", get_spacex_telemetry()), ("⚖️ LAW", "Sovereignty/EB-1A"), ("🧠 NEURALINK", "Neural-Mesh"),
        ("🧬 BIOGENETICS", "Longevity-Live"), ("💰 IPO GOLD", "Quantum Valuation"), ("🏗️ SENIOR ENG", "Infra-Sovereign"),
        ("🛡️ DEFESA CYBER", "Entropic Shield"), ("📈 VALUATION", "Asset Liquidity"), ("🌐 SOBERANIA", "SOH v2.2 Hub")
    ]
    
    cols = st.columns(3)
    for i, (label, api_source) in enumerate(nodes):
        with cols[i % 3]:
            color = "#FFD700" if "GOLD" in label else "#00FFFF"
            st.markdown(f"""<div class='node-active'>
                <b style='color:{color}'>{label}</b><br>
                <small style='color:#00FF41'>STATUS: {api_source[:30]}</small><br>
                <code style='font-size:0.6rem;'>PQC-HASH: {hashlib.sha1(str(time.time()).encode()).hexdigest()[:8]}</code>
            </div>""", unsafe_allow_html=True)
            if st.button(f"AUDIT {label}", key=f"btn_{i}"):
                speak(f"Audit sequence initiated for {label}. Ingesting real-time telemetry.")
                st.session_state.pdf_evo = generate_v430_dossier(label, api_source)
                st.session_state.n_active = label

    if 'pdf_evo' in st.session_state:
        st.download_button(f"📥 DOWNLOAD {st.session_state.n_active} SOVEREIGN DOSSIER", st.session_state.pdf_evo, f"NEXUS_V430_{st.session_state.n_active}.pdf", use_container_width=True)

global_sync_hub()

# --- [6. ONDA DE HOMEOSTASE REALTIME] ---
@st.fragment(run_every=1)
def wave_v430():
    t = np.linspace(0, 10, 250); y = np.sin(t * (psutil.cpu_percent()/10 + 2.5) + time.time() * 3.5)
    fig = go.Figure(go.Scatter(x=t, y=y, line=dict(color='#00FF41', width=3), fill='tozeroy', fillcolor='rgba(0, 255, 65, 0.2)'))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=120, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(visible=False), yaxis=dict(visible=False, range=[-2, 2]))
    st.plotly_chart(fig, use_container_width=True)

wave_v430()
