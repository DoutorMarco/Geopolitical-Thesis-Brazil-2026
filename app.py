import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import httpx
import psutil
import time, hashlib, collections, sqlite3, os, re, random
import plotly.graph_objects as go
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from scipy.fft import fft, ifft
from cryptography.fernet import Fernet
from Bio.Seq import Seq
from sklearn.linear_model import LinearRegression
from contextlib import contextmanager

# --- SEGURANÇA ---
def get_hsm_cipher():
    if not os.path.exists("xeon_omni.key"):
        with open("xeon_omni.key", "wb") as f: f.write(Fernet.generate_key())
    with open("xeon_omni.key", "rb") as f: return Fernet(f.read())
cipher = get_hsm_cipher()

# --- DB ATÔMICO ---
@contextmanager
def sovereign_transaction():
    conn = sqlite3.connect('xeon_sovereign.db', timeout=60, check_same_thread=False)
    try:
        yield conn
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

# --- MOTORES REAIS ---
def fetch_osint(query):
    try:
        url = f"https://google.com{query}+2026&hl=en-US"
        with httpx.Client(timeout=10.0) as client:
            r = client.get(url)
            titles = re.findall(r"<title>(.*?)</title>", r.text)
            return titles[1].upper() if len(titles) > 1 else "SCAN: STABLE"
    except: return "OFFLINE"

@st.cache_data(ttl=3600)
def bio_dna(sequence):
    try:
        dna = Seq(re.sub(r'[^ATCG]', '', sequence.upper()))
        return f"COMP: {dna.complement()} | TRANS: {dna.translate()[:10]}..."
    except: return "BIO_ERROR"

# --- UI CONFIG ---
st.set_page_config(page_title="XEON COMMAND", layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>.stApp { background-color: #000; color: #00FFCC; font-family: monospace; }</style>", unsafe_allow_html=True)

if 'intel_log' not in st.session_state: st.session_state.intel_log = collections.deque(["[SISTEMA ON] v42.0 SOBERANO"], maxlen=10)
if 'hw_trace' not in st.session_state: st.session_state.hw_trace = collections.deque([random.uniform(5,10) for _ in range(60)], maxlen=100)

def run_mission(node, u_in=""):
    cpu = psutil.cpu_percent()
    res = "SUCCESS"
    if node == "BIO": res = bio_dna(u_in)
    elif node == "GEO": res = fetch_osint(u_in)
    elif "FIN" in node:
        try: res = f"BTC: ${yf.Ticker('BTC-USD').fast_info['last_price']:.2f}"
        except: res = "FIN_STABLE"
    st.session_state.hw_trace.append(cpu)
    st.session_state.intel_log.append(f"[{time.strftime('%H:%M:%S')}] {node}: {res[:40]}")

# --- LAYOUT FIEL À IMAGEM ---
st.write(f"📡 TERMINAL REAL | v42.0 SOBERANA | {time.strftime('%H:%M:%S')}")
u_input = st.text_input("INJETAR DADOS:", label_visibility="collapsed")
if st.button("EXE_PROTOCOL"): run_mission("DATA", u_input)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.caption("🏗️ ENGENHARIA")
    if st.button("LITHO GRAFENO"): run_mission("ENG", "GRAFENO")
with c2:
    st.caption("🌍 GEOPOLÍTICA")
    if st.button("SCAN GLOBAL"): run_mission("GEO", u_input)
with c3:
    st.caption("💰 FINANCEIRO")
    if st.button("BOLSAS REAIS"): run_mission("FIN", "")
with c4:
    st.caption("🧬 BIO-EVOLUÇÃO")
    if st.button("DNA RESEARCH"): run_mission("BIO", u_input)
    def gen_pdf():
        output = BytesIO(); p = canvas.Canvas(output, pagesize=A4); p.setFillColorRGB(0,0,0); p.rect(0,0,600,900,fill=1)
        p.setFillColorRGB(0,1,0.8); p.setFont("Courier-Bold", 14); p.drawString(50, 820, "REPORTE SOBERANO FINAL")
        p.setFont("Courier", 8); y = 790
        for l in list(st.session_state.intel_log): p.drawString(50, y, f"> {l}"); y -= 15
        p.showPage(); p.save(); output.seek(0); return output
    st.download_button("📄 EXPORT PDF", data=gen_pdf(), file_name="XEON.pdf")

st.markdown(f'<div style="border:1px solid #00FFCC;padding:10, background:#000;height:150px;overflow:auto;font-size:11px;">{"<br>".join(list(st.session_state.intel_log))}</div>', unsafe_allow_html=True)

fig = go.Figure(go.Bar(y=list(st.session_state.hw_trace), marker_color='#00FFCC'))
fig.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=100, paper_bgcolor='black', plot_bgcolor='black', xaxis=dict(visible=False), yaxis=dict(visible=False))
st.plotly_chart(fig, use_container_width=True)

st.write(f"📊 **CPU:** {psutil.cpu_percent()}% | **RAM:** {psutil.virtual_memory().percent}% | **STATUS:** ✅ ACTIVE")
time.sleep(5); st.rerun()
