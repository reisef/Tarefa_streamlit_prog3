import streamlit as st
import matplotlib.pyplot as plt
from tratamento import carregar_dados

df = carregar_dados()

st.title("💰 PIB vs Felicidade")

# Filtro por ano
anos = sorted(df["Ano"].unique())
ano_selecionado = st.sidebar.selectbox("Selecione o ano", anos)
df_filtrado = df[df["Ano"] == ano_selecionado]

# Filtro por país
paises = sorted(df_filtrado["País"].unique())
pais_selecionado = st.sidebar.selectbox("Selecione o país", ["Todos"] + paises)

if pais_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["País"] == pais_selecionado]

# Criando o gráfico com Matplotlib (reduzido em ~30%)
fig, ax = plt.subplots(figsize=(5.6, 4.2))
scatter = ax.scatter(
    df_filtrado["PIB per capita (log)"],
    df_filtrado["Índice de Felicidade"],
    c="blue",
    alpha=0.7
)

# Adicionando rótulos
ax.set_xlabel("PIB per capita (log)")
ax.set_ylabel("Índice de Felicidade")
ax.set_title(f"PIB per capita vs Felicidade ({ano_selecionado})")

# Exibir no Streamlit
st.pyplot(fig)