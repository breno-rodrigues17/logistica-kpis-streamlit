# 📦 Análise de KPIs Logísticos com Streamlit

Este projeto é uma aplicação interativa desenvolvida com Python e Streamlit para analisar dados logísticos de entregas. Ele permite importar um arquivo `.csv` com os dados, calcular indicadores importantes (KPIs) e visualizar gráficos com destaques para regiões com alto ou baixo desempenho.

---

## ✅ Funcionalidades

- Upload de arquivo CSV com dados de entregas
- Cálculo automático dos KPIs:
  - Total de entregas
  - Percentual de entregas com atraso
  - Tempo médio de entrega
  - Custo total
- Gráfico de entregas por região com **códigos de cores**:
  - 🟩 Verde: Regiões com ≤ 20% de atraso
  - 🟥 Vermelho: Regiões com > 20% de atraso
- Exibição da tabela de dados original

---

## 🛠 Tecnologias utilizadas

- Python 
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

---

## 🗂 Estrutura esperada do CSV

Seu arquivo `.csv` deve conter as seguintes colunas:

| Coluna         | Descrição                                |
|----------------|------------------------------------------|
| `id_entrega`   | Identificador único da entrega           |
| `dias_atraso`  | Quantidade de dias de atraso da entrega  |
| `tempo_entrega`| Tempo total da entrega em dias           |
| `custo`        | Custo da entrega                         |
| `regiao`       | Nome da região onde a entrega foi feita  |

---

## ▶️ Como executar o projeto

1. **Instale as bibliotecas necessárias** (caso ainda não tenha):
   ```bash
   pip install streamlit pandas matplotlib
