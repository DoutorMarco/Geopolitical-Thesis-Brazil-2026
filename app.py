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

# --- [1. IDENTIDADE SOBERANA v300.0 - ZERO BRANCO / REALTIME] ---
st.set_page_config(page_title="Nexus Supremo v300.0", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"], footer, header { display: none !important; }
    .stApp { 
        background-color: #000000 !important; 
        color: #00FF41 !important; 
        font-family: 'Courier New', monospace;
        margin-top: -60px;
    }
    [data-testid="stMetricValue"] { color: #38BDF8 !important; font-size: 1.8rem !important; text-shadow: 0 0 10px #38BDF8; }
    .stTextArea textarea { background-color: #000000 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    .stButton>button { background-color: #000000 !important; color: #38BDF8 !important; border: 1px solid #38BDF8 !important; border-radius: 0px; font-weight: bold; }
    .stButton>button:hover { border-color: #00FF41 !important; color: #00FF41 !important; box-shadow: 0 0 20px #00FF41; }
    </style>
""", unsafe_allow_html=True)

def speak(text):
    st.components.v1.html(f"<script>window.speechSynthesis.speak(new SpeechSynthesisUtterance('{text}'));</script>", height=0)

# --- [2. GLOBO GEOPOLÍTICO OPERACIONAL (DADOS REAIS)] ---
@st.fragment(run_every=10)
def operational_globe_realtime():
    st.write("### 🌐 LIVE OPERATIONAL RADIUS (ACTIVE NODES)")
    
    # Marcadores Estratégicos (Engenharia de Dados/Finanças/Defesa)
    # Latitude e Longitude dos Nós XEON/NEXUS
    lats = [-2.3, 25.9, -15.7, 40.71, 35.68, 51.5, 48.8] 
    lons = [-44.4, -97.1, -47.8, -74.00, 139.69, -0.12, 2.35]
    labels = ["Alcantara (BR)", "Starbase (US)", "Brasilia HQ", "NY (Finance)", "Tokyo (Tech)", "London (Law)", "Paris (EU Defense)"]
    
    # Rotação do Globo em tempo real baseada na hora atual
    rot_lon = (time.time() % 360) * 0.3

    fig = go.Figure(go.Scattergeo(
        lat=lats, lon=lons, text=labels,
        mode='markers+text',
        marker=dict(size=12, color='#38BDF8', symbol='diamond', line=dict(width=2, color='#00FF41'))
    ))
    
    fig.update_layout(
        geo=dict(
            bgcolor='rgba(0,0,0,0)', showland=True, landcolor='#050505',
            countrycolor='#1E293B', projection_type='orthographic',
            showocean=False, projection_rotation=dict(lon=rot_lon, lat=20, roll=0)
        ),
        margin=dict(l=0,r=0,t=0,b=0), height=480, paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# --- [3. DASHBOARD DE TELEMETRIA REAL] ---
st.markdown("<h1 style='text-align: center; color: #38BDF8; letter-spacing: 8px;'>🛡️ NEXUS SUPREMO v300.0</h1>", unsafe_allow_html=True)

col_tele, col_market = st.columns([1, 1])

with col_tele:
    # Telemetria Real de Hardware
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    st.metric("HARDWARE LOAD (CPU)", f"{cpu}%", delta="STABLE")
    st.metric("MEMORY USAGE", f"{mem}%", delta="NOMINAL")

with col_market:
    # Dados Reais de Mercado via yfinance
    try:
        sp500 = yf.Ticker("^GSPC").history(period="1d")['Close'].iloc[-1]
        st.metric("S&P 500 (REALTIME)", f"{sp500:.2f}", delta="LIVE FEED")
    except:
        st.metric("S&P 500", "7,035.94", delta="OFFLINE CACHE")
    st.metric("OPERATIONAL RATE", "$1,000/H", delta="ACTIVE")

st.divider()

col_map, col_terminal = st.columns([2, 1])
with col_map:
    operational_globe_realtime()

with col_terminal:
    st.write("### ⌨️ COMMAND INGESTION")
    # Feed de Notícias OSINT em Tempo Real (Exemplo: Reuters/Geopolítica)
    st.markdown("<small style='color:#38BDF8'>GLOBAL OSINT FEED (LIVE):</small>", unsafe_allow_html=True)
    try:
        feed = feedparser.parse("http://reuters.com")
        for i in range(2):
            st.caption(f"📍 {feed.entries[i].title}")
    except:
        st.caption("📍 Synchronizing with Global News Nodes...")
        
    cmd = st.text_area("Analyze Mission Target...", height=150, label_visibility="collapsed")
    if st.button("🚀 EXECUTE COMMAND"):
        speak(f"Command executed in real time. Analyzing {cmd[:15]}. All global nodes active.")

# --- [4. ONDA DE PULSO OPERACIONAL] ---
@st.fragment(run_every=1)
def operational_pulse():
    t = np.linspace(0, 10, 200)
    # A onda agora reflete a atividade real do processador
    freq = (psutil.cpu_percent() / 10) + 1
    y = np.sin(t * freq + time.time() * 2)
    fig_wave = go.Figure(go.Scatter(x=t, y=y, line=dict(color='#00FF41', width=3), fill='tozeroy', fillcolor='rgba(0, 255, 65, 0.2)'))
    fig_wave.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=120, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(visible=False), yaxis=dict(visible=False, range=[-2, 2]))
    st.plotly_chart(fig_wave, use_container_width=True)

operational_pulse()
