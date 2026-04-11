import streamlit as st
import numpy as np
import plotly.graph_objects as go
import yfinance as yf
import feedparser
import psutil
import time, hashlib, collections, sqlite3, os, re
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from scipy.fft import fft, ifft
from cryptography.fernet import Fernet
from Bio.Seq import Seq

# --- 1. SEGURANÇA E PERSISTÊNCIA DE CHAVE ---
def get_encryption_suite():
    KEY_FILE = "xeon_kernel.key"
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f: secret_key = f.read()
    else:
        secret_key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f: f.write(secret_key)
    return Fernet(secret_key)

cipher = get_encryption_suite()

# --- 2. ENGENHARIA DE DADOS: SINGLETON POOL ---
class XeonDB:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = sqlite3.connect('xeon_sovereign.db', timeout=60, check_same_thread=False)
            cls._instance.execute('''CREATE TABLE IF NOT EXISTS intel_vault 
                                    (timestamp TEXT, node TEXT, cpu REAL, payload TEXT)''')
            cls._instance.commit()
        return cls._instance

db = XeonDB()

def save_log(node, cpu, payload):
    try:
        db.execute("INSERT INTO intel_vault VALUES (?,?,?,?)", 
                  (time.strftime('%Y-%m-%d %H:%M:%S'), node, cpu, payload))
        db.commit()
    except: pass

# --- 3. MOTORES DE REALIDADE (BILINGUAL) ---
def fetch_osint(query):
    try:
        url = f"https://google.com{query}+2026&hl=en-US&gl=US&ceid=US:en"
        feed = feedparser.parse(url)
        return feed.entries[0].title.upper() if feed.entries else "SCAN: STABLE / ESTÁVEL"
    except: return "CONNECTION OFFLINE / CONEXÃO OFFLINE"

@st.cache_data(ttl=3600)
def bio_dna_process(sequence):
    try:
        clean_dna = re.sub(r'[^ATCG]', '', sequence.upper())
        if len(clean_dna) < 3: return "INVALID SEQ / SEQ INVÁLIDA"
        dna = Seq(clean_dna)
        return f"DNA_COMP: {dna.complement()} | PROTEIN: {dna.translate()[:12]}..."
    except: return "BIO_ENGINE_ERROR"

# --- 4. GERAÇÃO DE PDF SOBERANO ---
def generate_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFillColorRGB(0, 0, 0); p.rect(0, 0, 600, 900, fill=1)
    p.setFillColorRGB(0, 1, 0.8); p.setFont("Courier-Bold", 14)
    p.drawString(50, 820, "SCIENTIFIC SOBERANIA REPORT - v27.0")
    p.setFont("Courier", 7)
    y = 790
    logs = db.execute("SELECT * FROM intel_vault ORDER BY timestamp DESC LIMIT 60").fetchall()
    for l in logs:
        p.drawString(50, y, f"> [{l[0]}] NODE: {l[1]} | CPU: {l[2]}% | {l[3][:80]}")
        y -= 13
    p.showPage(); p.save(); buffer.seek(0)
    return buffer

# --- 5. INTERFACE CYBER-VERDE/PRETO (PRODUÇÃO) ---
st.set_page_config(page_title="XEON COMMAND v27.0", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FFCC; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #000; color: #00FFCC; border: 1px solid #00FFCC; border-radius: 0; }
    .stButton>button { background-color: #000 !important; color: #00FFCC !important; border: 1px solid #00FFCC !important; width: 100%; border-radius: 0; font-size: 10px; font-weight: bold; }
    .stButton>button:hover { background-color: #00FFCC !important; color: #000 !important; box-shadow: 0 0 15px #00FFCC; }
    .terminal { border: 1px solid #00FFCC; padding: 12px; background: #000; height: 180px; font-size: 11px; overflow-y: auto; color: #00FFCC; border-style: double; }
    .res-box { border: 2px solid #00FFCC; padding: 15px; text-align: center; font-weight: bold; margin: 10px 0; background: #010101; color: #00FFCC; text-shadow: 0 0 5px #00FFCC; }
    </style>
    """, unsafe_allow_html=True)

if 'hw_trace' not in st.session_state:
    st.session_state.hw_trace = collections.deque([0.0 for _ in range(60)], maxlen=100)
if 'intel_log' not in st.session_state:
    st.session_state.intel_log = collections.deque(["[SYSTEM ON] KERNEL v27.0 - FINAL SOBERANO"], maxlen=12)
if 'last_out' not in st.session_state:
    st.session_state.last_out = "AWAITING DATA INJECTION / AGUARDANDO INGESTÃO"

def run_kernel(node, u_in=""):
    t_start = time.perf_counter()
    # Integridade Física (FFT Stress Check)
    sig = np.random.normal(0, 1, 512)
    if not np.allclose(sig, ifft(fft(sig)).real, atol=1e-12): return

    cpu = psutil.cpu_percent()
    res = "PROTOCOL COMPLETE / CONCLUÍDO"
    
    if node == "BIO_GEN": res = bio_dna_process(u_in)
    elif node == "GEO_SCAN": res = fetch_osint(u_in or "geopolitics")
    elif "FIN" in node:
        try: res = f"BTC-USD: ${yf.Ticker('BTC-USD').fast_info.last_price:.2f}"
        except: res = "FIN_DATA_TIMEOUT"

    st.session_state.last_out = res
    st.session_state.hw_trace.append(cpu)
    st.session_state.intel_log.append(f"[{time.strftime('%H:%M:%S')}] [{node}] {res[:55]} | CPU: {cpu}%")
    save_log(node, cpu, res[:100])

# --- 6. LAYOUT OPERACIONAL FINAL ---
st.write(f"📡 XEON NODE v27.0 | SOBERANIA REAL | {time.strftime('%H:%M:%S')}")
u_query = st.text_input("", placeholder="INSERT DATA / PESQUISAR / INJETAR (DNA, GEO, FIN)...", label_visibility="collapsed")
if st.button("EXECUTE SCIENTIFIC PROTOCOL / EXECUTAR PROTOCOLO CIENTÍFICO"):
    if u_query: run_kernel("DATA_INJECT", u_query)

st.markdown(f'<div class="res-box">{st.session_state.last_out}</div>', unsafe_allow_html=True)

# Grid 4 Colunas Fiel à Imagem
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.write("🏗️ ENGINEERING")
    if st.button("LITHO GRAFENO"): run_kernel("ENG_GRAF")
    if st.button("CORE INTEGRITY"): run_kernel("ENG_CORE")
with c2:
    st.write("🌍 GEOPOLITICS")
    if st.button("SCAN GLOBAL (REAL)"): run_kernel("GEO_SCAN", u_query)
    if st.button("DEFESA SPACE-X"): run_kernel("GEO_SPX")
with c3:
    st.write("💰 FINANCIAL")
    if st.button("MARKET MONITOR"): run_kernel("FIN_MKT")
    if st.button("SWIFT SINC"): run_kernel("FIN_SWIFT")
with c4:
    st.write("🧬 BIO-EVOLUTION")
    if st.button("DNA RESEARCH"): run_kernel("BIO_GEN", u_query)
    st.download_button("📄 PDF REPORT (EN/PT)", data=generate_pdf(), file_name="XEON_FINAL.pdf")

# Gráfico de Telemetria de Hardware
st.markdown('<div class="terminal">' + "<br>".join(list(st.session_state.intel_log)) + '</div>', unsafe_allow_html=True)
fig = go.Figure(go.Bar(y=list(st.session_state.hw_trace), marker_color='#00FFCC'))
fig.update_layout(template="plotly_dark", height=150, margin=dict(l=0,r=0,b=0,t=0), paper_bgcolor='black', plot_bgcolor='black', xaxis=dict(visible=False), yaxis=dict(title="CPU %", range=[0, 100]))
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

st.write(f"📊 **HARDWARE:** CPU: {psutil.cpu_percent()}% | RAM: {psutil.virtual_memory().percent}% | **STATUS:** ✅ REAL SOBERANO")

time.sleep(5)
if not u_query: st.rerun()
