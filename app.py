import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/Pedidos.csv")
df = pd.DataFrame(data)

def main():
    st.title("Dashboard de Vendas :shopping_trolley:")
    
    aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
    with aba1:
        display_dataframe(df)
    with aba2:
        display_charts(df)
    with aba3:
        display_metrics(df)

def display_dataframe(data):
    st.header("Visualização do DataFrame")
    st.sidebar.header("Filtros")
    selected_region = st.sidebar.multiselect(
        "Selecione as regiões",
        data['Regiao'].unique(),
        data['Regiao'].unique()
    )
    filtered_data = data[data['Regiao'].isin(selected_region)]
    st.write(filtered_data)

def display_charts(data):
    st.header("Visualização de Gráficos")
    
    st.subheader("Desempenho por Região")
    plt.figure(figsize=(10, 6))
    sns.countplot(x="Regiao", data=data)
    st.pyplot(plt.gcf())
    
    st.subheader("Itens mais Vendidos")
    plt.figure(figsize=(10, 6))
    sns.countplot(x="Item", data=data)
    st.pyplot(plt.gcf())
    
    st.subheader("Preço Médio por Item")
    avg_price = data.groupby("Item")["PrecoUnidade"].mean().sort_values(ascending=False)
    st.bar_chart(avg_price)

def display_metrics(data):
    st.subheader("Métricas")
    total_sales = data["Unidades"].sum()
    average_price = data["PrecoUnidade"].mean()
    most_productive = data["Vendedor"].value_counts().idxmax()
    
    coluna1, coluna2, coluna3 = st.columns(3)
    with coluna1:
        st.metric("Vendedor mais produtivo", most_productive)
    with coluna2:
        st.metric("Vendas Totais", total_sales)
    with coluna3:
        st.metric("Preço Médio", f"R$ {round(average_price, 2)}")

if __name__ == "__main__":
    main()
