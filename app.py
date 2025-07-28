import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análise de Entregas", layout="wide")

st.title("📦 Análise de KPIs Logísticos")

arquivo = st.file_uploader("Envie o arquivo de entregas (.csv)", type="csv")

if arquivo:
    df = pd.read_csv(arquivo)

    # Indicadores gerais
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

    # Cálculo entregas por região
    entregas_por_regiao = df.groupby('regiao')['id_entrega'].count().sort_values(ascending=False)

    # Cálculo percentual de atraso por região
    atraso_por_regiao = df.groupby('regiao').apply(lambda x: (x['dias_atraso'] > 0).mean() * 100)

    # Definindo cores: verde para atraso <= 20%, vermelho para atraso > 20%
    colors = ['green' if atraso_por_regiao[reg] <= 20 else 'red' for reg in entregas_por_regiao.index]

    # Gráfico menor e colorido
    st.subheader("📍 Entregas por Região (cores indicam % de atraso)")

    fig, ax = plt.subplots(figsize=(7, 4))
    entregas_por_regiao.plot(kind='bar', ax=ax, color=colors)
    ax.set_ylabel("Quantidade de Entregas")
    ax.set_xlabel("Região")
    ax.set_title("Entregas por Região com indicação de atraso")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Legenda manual (como matplotlib não gera legenda automática para cores custom)
    import matplotlib.patches as mpatches
    verde_patch = mpatches.Patch(color='green', label='Atraso ≤ 20%')
    vermelho_patch = mpatches.Patch(color='red', label='Atraso > 20%')
    ax.legend(handles=[verde_patch, vermelho_patch])

    st.pyplot(fig)

    # Mostrar tabela
    st.subheader("📁 Dados da Tabela")
    st.dataframe(df)

else:
    st.info("Faça o upload de um arquivo CSV para iniciar a análise.")
