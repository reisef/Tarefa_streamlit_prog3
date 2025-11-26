import streamlit as st
from tratamento import carregar_dados

df = carregar_dados()

st.title("🧹 Dataset Tratado")

st.subheader("Colunas traduzidas")
st.write(list(df.columns))

st.subheader("Primeiras linhas")
st.dataframe(df.head())