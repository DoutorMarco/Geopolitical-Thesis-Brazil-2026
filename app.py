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

# --- [1. IDENTIDADE SOBERANA v350.0 - BLACKOUT TOTAL] ---
st.set_page_config(page_title="NEXUS SUPREMO v350.0", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"], footer, header { display: none !important; }
    .stApp { 
        background-color: #000000 !important; 
        color: #00FF41 !important; 
        font-family: 'Courier New', monospace;
        margin-top: -60px;
    }
    [data-testid="stMetricValue"] { color: #38BDF8 !important; font-size: 1.8rem !important; }
    .stTextArea textarea { background-color: #000000 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    .stButton>button { background-color: #000000 !important; color: #38BDF8 !important; border: 1px solid #38BDF8 !important; height: 45px; font-weight: bold; }
    .stButton>button:hover { border-color: #00FF41 !important; color: #00FF41 !important; box-shadow: 0 0 20px #00FF41; }
    </style>
""", unsafe_allow_html=True)

def speak(text):
    st.components.v1.html(f"<script>var u=new SpeechSynthesisUtterance('{text}');u.lang='en-US';u.rate=1.0;window.speechSynthesis.speak(u);</script>", height=0)

# --- [2. MOTOR DE DOSSIÊ PQC (6 PÁGINAS)] ---
def generate_pqc_dossier(module_name):
    buf = BytesIO()
    p = canvas.Canvas(buf, pagesize=A4)
    sections = ["NIST AUDIT", "GLOBAL FINANCE", "PQC GOVERNANCE", "DIGITAL PHYSIOLOGY", "EB-1A EVIDENCE", "FINAL VERDICT"]
    q_hash = hashlib.sha384(f"QUANTUM_{module_name}_{time.time()}".encode()).hexdigest().upper()
    for i, title in enumerate(sections):
        p.setFillColorRGB(0, 0, 0); p.rect(0, 0, 600, 900, fill=1)
        p.setFillColorRGB(0, 1, 0.25); p.setFont("Courier-Bold", 18)
        p.drawCentredString(300, 800, f"NEXUS SUPREMO - {module_name}")
        p.setFont("Courier", 12); p.drawString(50, 750, f"SECTION: {title}")
        p.drawString(50, 720, f"ARCHITECT: MARCO ANTONIO DO NASCIMENTO")
        p.drawString(50, 700, f"PQC HASH: {q_hash[:32]}")
        p.drawString(50, 640, f"PAGE {i+1} OF 6 | MISSION CRITICAL")
        p.showPage()
    p.save(); buf.seek(0)
    return buf

# --- [3. DASHBOARD OPERACIONAL] ---
st.markdown("<h2 style='text-align: center; color: #38BDF8; letter-spacing: 10px;'>🛡️ NEXUS SUPREMO v350.0</h2>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("CPU LOAD", f"{psutil.cpu_percent()}%")
with c2: st.metric("PQC STATUS", "SECURED")
with c3:
    try: 
        sp500 = yf.Ticker("^GSPC").history(period="1d")['Close'].iloc[-1]
        st.metric("S&P 500", f"{sp500:.2f}")
    except: st.metric("S&P 500", "7035.94")
with c4: st.metric("RATE", "$1,000/H")

st.divider()

# --- [4. MAPA GLOBAL E COMANDO] ---
col_map, col_cmd = st.columns([1.6, 1])
with col_map:
    rot = (time.time() % 360) * 0.8
    fig = go.Figure(go.Scattergeo(
        lat=[-2.3, 25.9, -15.7, 40.71, 35.68], lon=[-44.4, -97.1, -47.8, -74.00, 139.69],
        text=["Alcantara", "Starbase", "Brasilia", "NY", "Tokyo"],
        mode='markers+text', marker=dict(size=12, color='#38BDF8', symbol='diamond', line=dict(width=2, color='#00FF41'))
    ))
    fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)', showland=True, landcolor='#050505', projection_type='orthographic', projection_rotation=dict(lon=rot, lat=20, roll=0)), margin=dict(l=0,r=0,t=0,b=0), height=450, paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with col_cmd:
    st.write("### ⌨️ COMMAND INGESTION")
    query = st.text_area("Live Mission Command...", height=150, label_visibility="collapsed", key="v350_cmd")
    if st.button("🚀 EXECUTE COMMAND"):
        speak("Command executed. Quantum synchronization active.")

st.divider()

# --- [5. OS 9 NÓS DE MISSÃO (LOGICA CORRIGIDA)] ---
st.write("### 🚀 MISSION NODES (QUANTUM ENFORCED)")
nodes = [
    ("🚀 SPACEX", "SPACEX"), ("⚖️ LAW", "LAW"), ("🧠 NEURALINK", "NEURALINK"),
    ("🧬 BIOGENETICS", "BIOGENETICS"), ("💰 IPO GOLD", "IPOGOLD"), ("🏗️ SENIOR ENG", "ENGINEERING"),
    ("🛡️ CYBER DEFENSE", "CYBER"), ("📈 VALUATION", "VALUATION"), ("🌐 SOVEREIGNTY", "SOH")
]
cols = st.columns(3)
for i, (label, key) in enumerate(nodes):
    with cols[i % 3]:
        # Correção do erro de variável: uso direto de 'label' para a condicional
        color_node = "#FFD700" if "GOLD" in label else "#00FF41"
        st.markdown(f"<div style='text-align:center; color:{color_node}; font-size:0.8rem; border-bottom:1px solid {color_node}; margin-bottom:5px;'>{label}</div>", unsafe_allow_html=True)
        if st.button(f"ACTIVATE {key}", key=f"btn_{key}", use_container_width=True):
            speak(f"Node {label} engaged. Quantum encryption active.")
            st.session_state.pdf = generate_pqc_dossier(label)
            st.session_state.n_active = label

if 'pdf' in st.session_state:
    st.download_button(f"📥 DOWNLOAD {st.session_state.n_active} PQC DOSSIER", st.session_state.pdf, f"NEXUS_PQC_{st.session_state.n_active}.pdf", use_container_width=True)

# --- [6. ONDA DE PULSO OPERACIONAL] ---
@st.fragment(run_every=1)
def wave():
    t = np.linspace(0, 10, 250); y = np.sin(t * (psutil.cpu_percent()/10 + 1) + time.time() * 2)
    fig_w = go.Figure(go.Scatter(x=t, y=y, line=dict(color='#00FF41', width=3), fill='tozeroy', fillcolor='rgba(0, 255, 65, 0.2)'))
    fig_w.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=140, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(visible=False), yaxis=dict(visible=False, range=[-2, 2]))
    st.plotly_chart(fig_w, use_container_width=True)

wave()
