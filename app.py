#app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análise de Entregas", layout="wide")

st.title("📦 Análise de KPIs Logísticos")

# Upload do CSV
arquivo = st.file_uploader("Envie o arquivo de entregas (.csv)", type="csv")

if arquivo:
    df = pd.read_csv(arquivo)

    # Indicadores
    total_entregas = len(df)
    percentual_atraso = (df['dias_atraso'] > 0).mean() * 100
    tempo_medio = df['tempo_entrega'].mean()
    custo_total = df['custo'].sum()

    # KPIs
    st.subheader("📊 Indicadores Principais")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de entregas", total_entregas)
    col2.metric("Com atraso", f"{percentual_atraso:.2f}%")
    col3.metric("Tempo médio", f"{tempo_medio:.2f} dias")
    col4.metric("Custo total", f"R$ {custo_total:,.2f}")

    # Gráfico por região
    st.subheader("📍 Entregas por Região")
    entregas_por_regiao = df.groupby('regiao')['id_entrega'].count().sort_values(ascending=False)

    fig, ax = plt.subplots()
    entregas_por_regiao.plot(kind='bar', ax=ax, color='#4F81BD')
    ax.set_ylabel("Quantidade de Entregas")
    ax.set_xlabel("Região")
    st.pyplot(fig)

    # Mostrar dados brutos
    st.subheader("📁 Dados da Tabela")
    st.dataframe(df)
else:
    st.info("Faça o upload de um arquivo CSV para iniciar a análise.")
