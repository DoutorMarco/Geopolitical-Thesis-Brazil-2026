import streamlit as st
import numpy as np
import yfinance as yf
from scipy.fft import fft
from scipy.signal.windows import kaiser
import plotly.graph_objects as go
import time, urllib.parse, feedparser
from reportlab.pdfgen import canvas
from io import BytesIO

# --- CONFIGURAÇÃO DE ALTA DISPONIBILIDADE ---
st.set_page_config(page_title="XEON COMMAND v16.0", layout="wide")

# CSS PARA IDENTIDADE VISUAL ABSOLUTA (CORES DA MISSÃO)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FFCC; font-family: 'Courier New', monospace; }
    
    /* BOTÕES OPERACIONAIS - FIDELIDADE À IMAGEM */
    div[data-testid="column"]:nth-child(1) button { background-color: #FFCC00 !important; color: black !important; border-radius: 0; font-weight: bold; width: 100%; border: 1px solid #00FFCC; }
    div[data-testid="column"]:nth-child(2) button { background-color: #008080 !important; color: white !important; border-radius: 0; font-weight: bold; width: 100%; border: 1px solid #00FFCC; }
    div[data-testid="column"]:nth-child(3) button { background-color: #FFFFFF !important; color: black !important; border-radius: 0; font-weight: bold; width: 100%; border: 1px solid #00FFCC; }
    div[data-testid="column"]:nth-child(4) button:first-child { background-color: #00FFFF !important; color: black !important; border-radius: 0; font-weight: bold; border: 1px solid #00FFCC; }
    div[data-testid="column"]:nth-child(4) button:last-child { background-color: #FF3300 !important; color: white !important; border-radius: 0; font-weight: bold; border: 1px solid #00FFCC; }

    .log-box { background-color: #000000; border: 2px solid #00FFCC; padding: 15px; color: #00FFCC; font-size: 13px; min-height: 100px; }
    .stTextInput>div>div>input { background-color: #050505; color: #00FFCC; border: 1px solid #00FFCC; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTORES DE INTELIGÊNCIA ---
def buscar_osint(termo):
    try:
        q = urllib.parse.quote(termo)
        url = f"https://google.com{q}&hl=pt-br&gl=BR&ceid=BR:pt"
        feed = feedparser.parse(url)
        return feed.entries[0].title if feed.entries else "Aguardando sinal satélite..."
    except: return "Sinal Geopolítico Interrompido."

def gerar_pdf_soberano(ticker, preco, intel):
    buf = BytesIO()
    c = canvas.Canvas(buf)
    c.setFont("Courier-Bold", 16)
    c.drawString(50, 800, "XEON® COMMAND - RELATÓRIO DE SOBERANIA")
    c.setFont("Courier", 11)
    c.drawString(50, 770, f"DATA: {time.ctime()} | TICKER: {ticker} | VALOR: {preco}")
    c.drawString(50, 740, "INVESTIGAÇÃO DE CAMPO:")
    c.drawString(50, 725, f"> {intel[:90]}...")
    c.save()
    return buf.getvalue()

# --- INTERFACE DE COMANDO ---
st.write(f"📡 CONEXÃO REAL: TERMINAIS MUNDIAIS {' '*30} MÉDICA MESTRA: XEON® COMMAND {' '*30} {time.strftime('%H:%M:%S')}")

# CÉLULA DE INTERAÇÃO (OSINT)
col_in1, col_in2 = st.columns([3, 1])
with col_in1:
    user_query = st.text_input("INJETAR DADOS / PESQUISA PROFUNDA (BIO/GUERRA/AERO):", "Neuralink Starshield 2026")
with col_int2 := col_in2:
    idioma = st.selectbox("SISTEMA:", ["PT", "EN"], label_visibility="collapsed")

st.markdown("<h3 style='text-align: center; border: 1px solid #00FFCC; padding: 5px;'>IDENTIFICADOR DA MISSÃO (TERMINAL/BANCO/GUERRA/BIO)</h3>", unsafe_allow_html=True)

# --- GRID 4 COLUNAS (BOTÕES ATIVOS) ---
c1, c2, c3, c4 = st.columns(4)
current_intel = "Aguardando varredura..."

with c1:
    st.write("🏗️ ENGENHARIA")
    if st.button("FORJAR CHIP GRAFENO"): st.toast("Sintetizando estrutura...")
    if st.button("SENTIR DOR (HARDWARE)"): st.warning("Pulso de Hardware Sincronizado.")

with c2:
    st.write("🌍 GEOPOLÍTICA")
    if st.button("US/CH/RU/EU DEPT"): current_intel = buscar_osint("war geopolitics 2026")
    if st.button("VARREDURA SETOR 7"): current_intel = buscar_osint("middle east tension")

with c3:
    st.write("💰 FINANCEIRO")
    t_in = st.selectbox("", ["BTC-USD", "GC=F", "USDBRL=X", "^GSPC"], label_visibility="collapsed")
    if st.button("B.C. & BOLSAS REAIS"): st.success("Terminais Bancários Online.")
    if st.button("CORRETORAS & BANCOS"): st.info("Sincronia Swift Ativa.")

with c4:
    st.write("🧬 BIO-EVOLUÇÃO")
    if st.button("BIO/CURA/LONGEVIDADE"): current_intel = buscar_osint("mRNA cure cancer 2026")
    
    # PDF FUNCIONAL (IMPRIMIR)
    pdf_bytes = gerar_pdf_soberano(t_in, "REAL-TIME", current_intel if current_intel else user_query)
    st.download_button("📄 PDF DE SOBERANIA", data=pdf_bytes, file_name="XEON_REPORT.pdf", mime="application/pdf")

# --- MOTOR DE VIDA: GRÁFICO ESPECTRAL EM TEMPO REAL ---
st.divider()
try:
    df = yf.download(t_in.strip(), period="1mo", interval="1h", progress=False)
    if not df.empty:
        # Transformando dados estáticos em Espectro Dinâmico
        prices = df['Close'].values.flatten()
        returns = np.diff(np.log(prices))
        n = 64
        window = kaiser(n, beta=14)
        y = (returns[-n:] - np.mean(returns[-n:])) * window
        mag = 2.0/n * np.abs(fft(y)[0:n])
        
        # LOG DE REGISTRO (FIEL À IMAGEM)
        log_content = f"""
        [REGISTRO SOBERANO IMORTALIZADO] -----------------------------
        🛡️ HARDWARE: Xeon Sentinel Neuromórfico | STATUS: OPERACIONAL
        🎯 ALVO: {t_in} | PREÇO: {prices[-1]:.2f} | VOLATILIDADE: {np.std(returns):.6f}
        >> INVESTIGAÇÃO: {current_intel[:85]}...
        >> STATUS: CONEXÃO CRIPTOGRAFADA. GRÁFICO ESPECTRAL ATIVO.
        """
        st.markdown(f"<div class='log-box'><pre style='color:#00FFCC; margin:0;'>{log_content}</pre></div>", unsafe_allow_html=True)
        
        # O GRÁFICO "COM VIDA" (Barras de Alta Precisão)
        fig = go.Figure(go.Bar(x=np.arange(n), y=mag, marker_color='#00FFCC'))
        fig.update_layout(template="plotly_dark", height=250, margin=dict(l=0,r=0,b=0,t=10), 
                          paper_bgcolor='black', plot_bgcolor='black',
                          xaxis=dict(showgrid=False, zeroline=False), yaxis=dict(showgrid=True, gridcolor='#111'))
        st.plotly_chart(fig, use_container_width=True)
except: st.error("Aguardando sincronia do sinal satélite...")

# SENTINELA (RE-ANÁLISE AUTOMÁTICA)
time.sleep(30)
st.rerun()
