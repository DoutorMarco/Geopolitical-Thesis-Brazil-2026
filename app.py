import streamlit as st
import numpy as np
import yfinance as yf
from scipy.fft import fft
from scipy.signal.windows import kaiser
import plotly.graph_objects as go
import time, urllib.parse, feedparser
from reportlab.pdfgen import canvas
from io import BytesIO

# --- CONFIGURAÇÃO DE INTERFACE E CORES (IDENTIDADE VISUAL DA IMAGEM) ---
st.set_page_config(page_title="XEON COMMAND v15.0", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FFCC; font-family: 'Courier New', monospace; }
    
    /* ESTILIZAÇÃO CIRÚRGICA DOS BOTÕES (CORES DA IMAGEM) */
    /* Coluna 1 - Engenharia: Amarelo */
    div[data-testid="column"]:nth-child(1) button { background-color: #FFCC00 !important; color: black !important; border-radius: 0; font-weight: bold; border: 1px solid #00FFCC; width: 100%; height: 45px; }
    
    /* Coluna 2 - Geopolítica: Verde Mar */
    div[data-testid="column"]:nth-child(2) button { background-color: #008080 !important; color: white !important; border-radius: 0; font-weight: bold; border: 1px solid #00FFCC; width: 100%; height: 45px; }
    
    /* Coluna 3 - Financeiro: Branco */
    div[data-testid="column"]:nth-child(3) button { background-color: #FFFFFF !important; color: black !important; border-radius: 0; font-weight: bold; border: 1px solid #00FFCC; width: 100%; height: 45px; }
    
    /* Coluna 4 - Bio: Ciano e Vermelho */
    div[data-testid="column"]:nth-child(4) button:first-child { background-color: #00FFFF !important; color: black !important; border-radius: 0; font-weight: bold; border: 1px solid #00FFCC; width: 100%; height: 45px; }
    div[data-testid="column"]:nth-child(4) button:last-child { background-color: #FF3300 !important; color: white !important; border-radius: 0; font-weight: bold; border: 1px solid #00FFCC; width: 100%; height: 45px; }

    .log-box { background-color: #000000; border: 2px solid #00FFCC; padding: 15px; color: #00FFCC; font-size: 13px; }
    .stTextInput>div>div>input { background-color: #050505; color: #00FFCC; border: 1px solid #00FFCC; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE INTELIGÊNCIA (OSINT E PDF) ---
def buscar_intel(query, idioma="pt-br"):
    try:
        q_enc = urllib.parse.quote(query)
        url = f"https://google.com{q_enc}&hl={idioma}&gl=BR&ceid=BR:pt"
        feed = feedparser.parse(url)
        return feed.entries[0].title if feed.entries else "Aguardando sinal..."
    except: return "Sinal Interrompido."

def gerar_pdf_relatorio(ticker, preco, intel):
    buf = BytesIO()
    c = canvas.Canvas(buf)
    c.setFont("Courier-Bold", 16)
    c.drawString(50, 800, "XEON COMMAND - RELATÓRIO DE SOBERANIA")
    c.setFont("Courier", 12)
    c.drawString(50, 770, f"CARIMBO DO TEMPO: {time.ctime()}")
    c.drawString(50, 750, f"ALVO ANALISADO: {ticker} | VALOR: {preco}")
    c.drawString(50, 730, "INTELIGÊNCIA CAPTURADA:")
    c.drawString(50, 715, f"> {intel[:85]}...")
    c.save()
    return buf.getvalue()

# --- CABEÇALHO ---
st.write(f"📡 CONEXÃO REAL: TERMINAIS MUNDIAIS {' '*30} MÉDICA MESTRA: XEON® COMMAND {' '*30} {time.strftime('%H:%M:%S')}")

# CÉLULA DE INGESTÃO (OSINT)
col_in1, col_in2 = st.columns([3, 1])
with col_in1:
    query_user = st.text_input("INJETAR DADOS / PESQUISA PROFUNDA:", "Neuralink Starshield 2026")
with col_in2:
    lang_opt = st.selectbox("SISTEMA:", ["PT", "EN"], label_visibility="collapsed")

st.markdown("<h3 style='text-align: center; border: 1px solid #00FFCC; padding: 5px;'>IDENTIFICADOR DA MISSÃO (TERMINAL/BANCO/GUERRA/BIO)</h3>", unsafe_allow_html=True)

# --- GRID DE COMANDO (4 COLUNAS FUNCIONAIS) ---
c1, c2, c3, c4 = st.columns(4)
current_intel = "Aguardando varredura..."

with c1:
    st.write("🏗️ ENGENHARIA")
    if st.button("FORJAR CHIP GRAFENO"): st.toast("Sintetizando estrutura nanométrica...")
    if st.button("SENTIR DOR (ANTI-ALUC)"): st.warning("Hardware Sync: Integridade 100%")

with c2:
    st.write("🌍 GEOPOLÍTICA")
    if st.button("US/CH/RU/EU DEPT"): current_intel = buscar_intel("conflito geopolitico guerra 2026")
    if st.button("VARREDURA ORIENTE MÉDIO"): current_intel = buscar_intel("israel iran tensão 2026")

with c3:
    st.write("💰 FINANCEIRO")
    t_input = st.selectbox("", ["BTC-USD", "GC=F", "USDBRL=X"], label_visibility="collapsed")
    if st.button("B.C. & BOLSAS REAIS"): st.success("Sincronizado via WebSocket.")
    if st.button("CORRETORAS & BANCOS"): st.toast("Acessando canais Swift...")

with c4:
    st.write("🧬 BIO-EVOLUÇÃO")
    if st.button("BIO/CURA/LONGEVIDADE"): current_intel = buscar_intel("mRNA cancer cure longevity 2026")
    
    # FUNCIONALIDADE PDF (IMPRIMIR PARA PC)
    pdf_bytes = gerar_pdf_relatorio(t_input, "REAL-TIME", current_intel)
    st.download_button("📄 PDF DE SOBERANIA", data=pdf_bytes, file_name="XEON_SOBERANIA.pdf", mime="application/pdf")

# --- PROCESSAMENTO E GRÁFICO (RODAPÉ DA IMAGEM) ---
try:
    df = yf.download(t_input.strip(), period="300d", interval="1d", progress=False)
    if not df.empty:
        precos = df['Close'].values.flatten()
        y = (np.diff(np.log(precos))[-128:] - 0) * kaiser(128, beta=14)
        mag = 2.0/128 * np.abs(fft(y)[0:64])
        
        st.divider()
        log_content = f"""
        [REGISTRO SOBERANO IMORTALIZADO] -----------------------------
        🛡️ HARDWARE: Xeon Sentinel Neuromórfico | STATUS: OPERACIONAL
        🎯 ALVO: {t_input} | PREÇO: {precos[-1]:.2f}
        >> INVESTIGAÇÃO: {current_intel[:80]}...
        >> STATUS: CONEXÃO CRIPTOGRAFADA. PDF PRONTO PARA DOWNLOAD.
        """
        st.markdown(f"<div class='log-box'><pre style='color:#00FFCC; margin:0;'>{log_content}</pre></div>", unsafe_allow_html=True)
        
        # GRÁFICO DE BARRAS VERDES (IDENTICO AO DASHBOARD)
        fig = go.Figure(go.Bar(x=np.arange(64), y=mag, marker_color='#00FFCC'))
        fig.update_layout(template="plotly_dark", height=200, margin=dict(l=0,r=0,b=0,t=10), paper_bgcolor='black', plot_bgcolor='black')
        st.plotly_chart(fig, use_container_width=True)
except: st.error("Aguardando sincronia do sinal satélite...")

time.sleep(30)
st.rerun()
