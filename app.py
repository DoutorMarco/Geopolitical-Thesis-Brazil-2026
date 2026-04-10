import streamlit as st
import pandas as pd
import plotly.express as px
import feedparser

# --- CONFIGURAÇÃO DE INTERFACE (THEME: ONYX & NEON) ---
st.set_page_config(page_title="XEON COMMAND", layout="wide")

# CSS para forçar o visual Preto com Verde Neon
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF00; }
    h1, h2, h3, p { color: #00FF00 !important; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #000000; color: #00FF00; border: 1px solid #00FF00; }
    .stTextInput>div>div>input { background-color: #111111; color: #00FF00; border: 1px solid #00FF00; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ XEON® COMMAND - NÚCLEO SOBERANO")
st.write("STATUS: OPERAÇÃO EM REGIME DE DEFESA NACIONAL")

# --- MÓDULO: MAPA DE CALOR GEOPOLÍTICO REAL ---
st.header("🌍 MAPA DE CALOR: FOCOS DE TENSÃO GLOBAL")

# Dados de exemplo de focos de conflito/tensão (Pode ser automatizado via API)
focos_tensao = {
    'Local': ['Oriente Médio', 'Leste Europeu', 'Mar do Sul da China', 'Fronteira Brasil/Venezuela'],
    'Lat': [32.0, 48.0, 15.0, 4.0],
    'Lon': [35.0, 31.0, 115.0, -60.0],
    'Intensidade': [95, 98, 80, 40]
}
df_mapa = pd.DataFrame(focos_tensao)

fig_mapa = px.density_mapbox(df_mapa, lat='Lat', lon='Lon', z='Intensidade', radius=30,
                             center=dict(lat=20, lon=0), zoom=1,
                             mapbox_style="carto-darkmatter", title="ZONAS DE CONFLITO ATIVAS")
fig_mapa.update_layout(margin={"r":0,"t":40,"l":0,"b":0}, paper_bgcolor='black', font_color='#00FF00')
st.plotly_chart(fig_mapa, use_container_width=True)

# --- INVESTIGAÇÃO INTERATIVA ---
query_investigacao = st.text_input("🔬 INVESTIGAÇÃO PROFUNDA (BIO/GUERRA/AERO):", "Neuralink Starshield 2026")
if st.button("EXECUTAR PROTOCOLO DE BUSCA"):
    url = f"https://google.com{query_investigacao.replace(' ', '+')}&hl=pt-BR&gl=BR"
    feed = feedparser.parse(url)
    for n in feed.entries[:5]:
        st.write(f"» [LINK] {n.title}")
