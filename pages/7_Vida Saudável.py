import streamlit as st
import plotly.express as px
from tratamento import carregar_dados

df = carregar_dados()

st.title("🩺 Expectativa de Vida Saudável vs Felicidade")

anos = sorted(df["Ano"].unique())
ano_selecionado = st.sidebar.selectbox("Selecione o ano", anos)
df_filtrado = df[df["Ano"] == ano_selecionado]

# Filtro por país
paises = sorted(df_filtrado["País"].unique())
pais_selecionado = st.sidebar.selectbox("Selecione o país", ["Todos"] + paises)

if pais_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["País"] == pais_selecionado]


fig = px.scatter(
    df_filtrado,
    x="Expectativa de Vida Saudável",
    y="Índice de Felicidade",
    color="País",
    hover_name="País",
    title=f"Expectativa de Vida Saudável vs Felicidade ({ano_selecionado})"
)
st.plotly_chart(fig, use_container_width=True)