import streamlit as st
import plotly.express as px
from tratamento import carregar_dados

df = carregar_dados()

st.title("📊 Visão Geral")

# Filtro por ano
anos = sorted(df["Ano"].unique())
ano_selecionado = st.sidebar.selectbox("Selecione o ano", anos)
df_filtrado = df[df["Ano"] == ano_selecionado]

# Filtro por país
paises = sorted(df_filtrado["País"].unique())
pais_selecionado = st.sidebar.selectbox("Selecione o país", ["Todos"] + paises)

if pais_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["País"] == pais_selecionado]

# Métricas em colunas
col1, col2, col3 = st.columns(3)
col1.metric("Número de países", len(df_filtrado["País"].unique()))
col2.metric("Maior Índice de Felicidade", round(df_filtrado["Índice de Felicidade"].max(), 2))
col3.metric("Menor Índice de Felicidade", round(df_filtrado["Índice de Felicidade"].min(), 2))

# Gráfico de barras (Top 10 países mais felizes)
top10 = df_filtrado.sort_values("Índice de Felicidade", ascending=False).head(10)
fig = px.bar(top10, x="País", y="Índice de Felicidade", title="Top 10 países mais felizes")
st.plotly_chart(fig, use_container_width=True)