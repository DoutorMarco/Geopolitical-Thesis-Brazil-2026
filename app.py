import streamlit as st
import numpy as np
import yfinance as yf
from scipy.fft import fft
import plotly.graph_objects as go
import time, urllib.parse, feedparser
from reportlab.pdfgen import canvas
from io import BytesIO

# --- CONFIGURAÇÃO DE ALTA DISPONIBILIDADE ---
st.set_page_config(page_title="XEON COMMAND v17.0", layout="wide")

# CSS PARA FIDELIDADE ABSOLUTA À IMAGEM ORIGINAL
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FFCC; font-family: 'Courier New', monospace; }
    
    /* GRID DE BOTÕES COM CORES IDENTICAS */
    div[data-testid="column"]:nth-child(1) button { background-color: #FFCC00 !important; color: black !important; border-radius: 0; font-weight: bold; width: 100%; border: 1px solid #00FFCC; }
    div[data-testid="column"]:nth-child(2) button { background-color: #008080 !important; color: white !important; border-radius: 0; font-weight: bold; width: 100%; border: 1px solid #00FFCC; }
    div[data-testid="column"]:nth-child(3) button { background-color: #FFFFFF !important; color: black !important; border-radius: 0; font-weight: bold; width: 100%; border: 1px solid #00FFCC; }
    div[data-testid="column"]:nth-child(4) button:first-child { background-color: #00FFFF !important; color: black !important; border-radius: 0; font-weight: bold; border: 1px solid #00FFCC; }
    div[data-testid="column"]:nth-child(4) button:last-child { background-color: #FF3300 !important; color: white !important; border-radius: 0; font-weight: bold; border: 1px solid #00FFCC; }

    .log-box { background-color: #000000; border: 2px solid #00FFCC; padding: 15px; color: #00FFCC; font-size: 13px; min-height: 120px; margin-top: 10px; }
    .stTextInput>div>div>input { background-color: #050505; color: #00FFCC; border: 1px solid #00FFCC; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTORES DE MISSÃO ---
def buscar_intel(termo):
    try:
        q = urllib.parse.quote(termo)
        url = f"https://google.com{q}&hl=pt-br&gl=BR"
        feed = feedparser.parse(url)
        return feed.entries[0].title if feed.entries else "Aguardando sinal..."
    except: return "Sinal Geopolítico Instável."

def gerar_pdf_final(ticker, valor, intel):
    buf = BytesIO()
    c = canvas.Canvas(buf)
    c.setFont("Courier-Bold", 16)
    c.drawString(50, 800, "XEON COMMAND - RELATÓRIO SOBERANO")
    c.setFont("Courier", 11)
    c.drawString(50, 770, f"DATA: {time.ctime()} | ATIVO: {ticker} | PREÇO: {valor}")
    c.drawString(50, 740, "RESULTADO DA VARREDURA:")
    c.drawString(50, 725, f"> {intel[:90]}...")
    c.save()
    return buf.getvalue()

# --- CABEÇALHO TÁTICO ---
st.write(f"📡 CONEXÃO REAL: TERMINAIS MUNDIAIS {' '*30} MÉDICA MESTRA: XEON® COMMAND {' '*30} {time.strftime('%H:%M:%S')}")

col_in1, col_in2 = st.columns([3, 1])
with col_in1:
    user_query = st.text_input("INJETAR DADOS / PESQUISA PROFUNDA:", "Neuralink Starshield 2026")
with col_in2:
    lang = st.selectbox("SISTEMA:", ["PT", "EN"], label_visibility="collapsed")

st.markdown("<h3 style='text-align: center; border: 1px solid #00FFCC; padding: 5px;'>IDENTIFICADOR DA MISSÃO (TERMINAL/BANCO/GUERRA/BIO)</h3>", unsafe_allow_html=True)

# --- GRID OPERACIONAL (4 COLUNAS FIÉIS) ---
c1, c2, c3, c4 = st.columns(4)
res_intel = "Aguardando varredura..."

with c1:
    st.write("🏗️ ENGENHARIA")
    if st.button("FORJAR CHIP GRAFENO"): st.toast("Sintetizando estrutura...")
    if st.button("SENTIR DOR (HARDWARE)"): st.warning("Pulso de Hardware Sincronizado.")

with c2:
    st.write("🌍 GEOPOLÍTICA")
    if st.button("US/CH/RU/EU DEPT"): res_intel = buscar_intel("global war geopolitics")
    if st.button("VARREDURA SETOR 7"): res_intel = buscar_intel("middle east tension")

with c3:
    st.write("💰 FINANCEIRO")
    t_in = st.selectbox("", ["BTC-USD", "GC=F", "USDBRL=X"], label_visibility="collapsed")
    if st.button("B.C. & BOLSAS REAIS"): st.success("Terminais Bancários Online.")
    if st.button("CORRETORAS & BANCOS"): st.info("Sincronia Swift Ativa.")

with c4:
    st.write("🧬 BIO-EVOLUÇÃO")
    if st.button("BIO/CURA/LONGEVIDADE"): res_intel = buscar_intel("mRNA cure breakthrough")
    
    # PDF FUNCIONAL E REAL
    pdf_data = gerar_pdf_final(t_in, "REAL-TIME", res_intel if res_intel != "Aguardando varredura..." else user_query)
    st.download_button("📄 PDF DE SOBERANIA", data=pdf_data, file_name="XEON_REPORT.pdf", mime="application/pdf")

# --- O GRÁFICO VIVO: ESPECTRO DE VOLATILIDADE DINÂMICO ---
st.divider()
try:
    df = yf.download(t_in.strip(), period="1mo", interval="1h", progress=False)
    if not df.empty:
        # Matemática de Pulso Espectral
        prices = df['Close'].values.flatten()
        returns = np.diff(np.log(prices))
        n_bars = 64
        # Criando vida: Magnitude real da volatilidade combinada com pulso estocástico
        mag = (np.abs(fft(returns[-n_bars:]))[:n_bars//2]) * 10
        mag = np.concatenate([mag, mag[::-1]]) # Espelhamento para visual simétrico
        
        # LOG DE REGISTRO IMORTALIZADO (IDÊNTICO À IMAGEM)
        log_content = f"""
        [REGISTRO SOBERANO IMORTALIZADO] -----------------------------
        🛡️ HARDWARE: Xeon Sentinel Neuromórfico | STATUS: OPERACIONAL
        🎯 ALVO: {t_in} | PREÇO: {prices[-1]:.2f} | PULSO: Sincronizado
        >> INVESTIGAÇÃO: {res_intel[:85]}...
        >> STATUS: CONEXÃO CRIPTOGRÁFICA EM {time.strftime('%d/%m/%Y, %H:%M:%S')}
        """
        st.markdown(f"<div class='log-box'><pre style='color:#00FFCC; margin:0;'>{log_content}</pre></div>", unsafe_allow_html=True)
        
        # O ESPECTRO QUE PULSA (GRÁFICO DE BARRAS VERDES)
        fig = go.Figure(go.Bar(x=np.arange(len(mag)), y=mag, marker_color='#00FFCC'))
        fig.update_layout(template="plotly_dark", height=200, margin=dict(l=0,r=0,b=0,t=10), 
                          paper_bgcolor='black', plot_bgcolor='black',
                          xaxis=dict(showgrid=False, visible=False), yaxis=dict(visible=False))
        st.plotly_chart(fig, use_container_width=True)
except: 
    st.error("Aguardando sincronia do sinal satélite...")

# SENTINELA (RE-ANÁLISE PARA CRIAR MOVIMENTO)
time.sleep(15)
st.rerun()
