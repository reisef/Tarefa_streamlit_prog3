import streamlit as st
import plotly.express as px
from tratamento import carregar_dados

df = carregar_dados()

# Frases explicativas
st.markdown("### ✨ Algumas observações sobre os dados:")
st.write("➡️ Criei essa dashboard para mostrar como diferentes países se comportam em relação à felicidade.")
st.write("➡️ Você deve filtrar primeiro o ano, depois o país para ter uma visão mais detalhada.")
st.write("➡️ Os gráficos ajudam a comparar os indicadores de forma visual e intuitiva, passando o mouse, eles interagem mostrando mais detalhes.")

