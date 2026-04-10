import streamlit as st
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
import time, random, hashlib
from reportlab.pdfgen import canvas
from io import BytesIO

# --- CONFIGURAÇÃO DE NÍVEL MILITAR ---
st.set_page_config(page_title="XEON COMMAND SOBERANO", layout="wide")

# Inicialização de Estados
if 'last_intel' not in st.session_state:
    st.session_state.last_intel = "SISTEMA AGUARDANDO INJEÇÃO DE DADOS..."

# --- MOTOR DE GERAÇÃO DE PDF (FUNCIONAL) ---
def gerar_pdf_soberano(conteudo):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Courier-Bold", 16)
    p.drawString(100, 800, "XEON COMMAND - RELATÓRIO DE SOBERANIA")
    p.setFont("Courier", 12)
    p.drawString(100, 770, f"DATA: {time.ctime()}")
    p.drawString(100, 750, "-"*50)
    p.drawString(100, 730, "INTELIGÊNCIA PROCESSADA:")
    
    # Quebra de linha simples para o conteúdo
    textobject = p.beginText(100, 710)
    for line in conteudo.split('\n'):
        textobject.textLine(line[:80])
    p.drawText(textobject)
    
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

# --- CSS FIEL À IMAGEM (CORES EXATAS) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FFCC; font-family: 'Courier New', monospace; }
    
    /* Input de Dados */
    .stTextInput>div>div>input { background-color: #000000; color: #00FFCC; border: 1px solid #00FFCC; }
    
    /* GRID DE BOTÕES - CORES DA IMAGEM */
    /* Coluna 1: Amarelo */
    div[data-testid="column"]:nth-child(1) button { background-color: #FFC107 !important; color: #000 !important; border-radius: 0; font-weight: bold; width: 100%; border: none; margin-bottom: 5px;}
    /* Coluna 2: Verde Água / Teal */
    div[data-testid="column"]:nth-child(2) button { background-color: #008B8B !important; color: #FFF !important; border-radius: 0; font-weight: bold; width: 100%; border: none; margin-bottom: 5px;}
    /* Coluna 3: Branco */
    div[data-testid="column"]:nth-child(3) button { background-color: #FFFFFF !important; color: #000 !important; border-radius: 0; font-weight: bold; width: 100%; border: none; margin-bottom: 5px;}
    /* Coluna 4: Ciano em cima, Laranja/Vermelho embaixo */
    div[data-testid="column"]:nth-child(4) button:first-child { background-color: #00FFFF !important; color: #000 !important; border-radius: 0; font-weight: bold; width: 100%; border: none; }
    div[data-testid="column"]:nth-child(4) button:last-child { background-color: #FF4500 !important; color: #FFF !important; border-radius: 0; font-weight: bold; width: 100%; border: none; }

    .log-box { border: 2px solid #00FFCC; padding: 15px; background: #000000; min-height: 180px; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.write(f"📡 CONEXÃO REAL: TERMINAIS MUNDIAIS {' '*40} MÉDICA MESTRA: XEON® COMMAND {' '*40} {time.strftime('%H:%M:%S')}")
user_input = st.text_input("INJETAR DADOS / PESQUISA PROFUNDA:", placeholder="Ex: Status Neuralink 2026")
st.markdown("<div style='text-align: center; border: 1px solid #00FFCC; padding: 5px; margin: 10px 0;'>IDENTIFICADOR DA MISSÃO (TERMINAL/BANCO/GUERRA/BIO)</div>", unsafe_allow_html=True)

# --- GRID OPERACIONAL ---
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.write("🏗️ ENGENHARIA")
    if st.button("FORJAR CHIP GRAFENO"):
        st.session_state.last_intel = "NANO-LITOGRAFIA: SINTETIZANDO ESTRUTURA DE GRAFENO PARA IA."
    if st.button("SENTIR DOR IA (ANTI-ALUC)"):
        st.session_state.last_intel = "SISTEMA ÉTICO: CALIBRANDO SENSORES DE DOR PARA PREVENÇÃO DE ERROS."

with c2:
    st.write("🌍 GEOPOLÍTICA")
    if st.button("US/CH/RU/EU DEPT"):
        st.session_state.last_intel = "VARREDURA DEFESA: MOVIMENTAÇÃO ESTRATÉGICA DETECTADA NO SETOR NORTE."
    if st.button("VARREDURA ORIENTE MÉDIO"):
        st.session_state.last_intel = "SINAL DE SATÉLITE: TENSÕES GEOPOLÍTICAS EM MONITORAMENTO REAL."

with c3:
    st.write("💰 FINANCEIRO")
    target = st.selectbox("", ["BTC-USD", "GC=F", "ETH-USD"], label_visibility="collapsed")
    if st.button("B.C. & BOLSAS REAIS"):
        px = yf.Ticker(target).fast_info.last_price
        st.session_state.last_intel = f"FLUXO FINANCEIRO: {target} COTADO EM ${px:.2f}."
    if st.button("CORRETORAS & BANCOS"):
        st.session_state.last_intel = "SISTEMA BANCÁRIO: CONEXÃO SWIFT ESTABILIZADA."

with c4:
    st.write("🧬 BIO-EVOLUÇÃO")
    if st.button("BIO/CURA/LONGEVIDADE"):
        st.session_state.last_intel = "BIO-TECH: PESQUISA DE LONGEVIDADE MRNA EM FASE DE VALIDAÇÃO."
    
    # GERAÇÃO DE PDF REAL
    pdf_file = gerar_pdf_soberano(st.session_state.last_intel)
    st.download_button("📄 PDF DE SOBERANIA", data=pdf_file, file_name="XEON_REPORT.pdf", mime="application/pdf")

# --- RESPOSTA E LOG ---
if user_input:
    st.session_state.last_intel = f"INJEÇÃO PROCESSADA: {user_input.upper()} - ANALISANDO..."

st.divider()
log_html = f"""
<div class="log-box">
    <span style="color: #00FFCC;">[REGISTRO SOBERANO IMORTALIZADO]</span><br>
    🛡️ HARDWARE: Xeon Sentinel Neuromórfico | CARGA: {random.uniform(0.1, 0.9):.3f}<br>
    🎯 RESULTADO: {st.session_state.last_intel}<br>
    >> STATUS: CONEXÃO CRIPTOGRÁFICA EM {time.strftime('%d/%m/%Y, %H:%M:%S')}
</div>
"""
st.markdown(log_html, unsafe_allow_html=True)

# --- GRÁFICO DE ESPECTRO (FIEL) ---
signal = np.random.uniform(0.1, 1, 60)
fig = go.Figure(go.Bar(y=signal, marker_color='#00FFCC'))
fig.update_layout(
    template="plotly_dark", height=150, margin=dict(l=0,r=0,b=0,t=0),
    paper_bgcolor='black', plot_bgcolor='black',
    xaxis=dict(visible=False), yaxis=dict(visible=False)
)
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

time.sleep(5)
if not user_input:
    st.rerun()
