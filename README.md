# Dashboard de Vendas :shopping_trolley:

Este repositório contém um **Dashboard Interativo de Vendas** criado com [Streamlit](https://streamlit.io/). Ele permite visualizar e explorar um conjunto de dados fictício sobre vendas, fornecendo métricas, gráficos e a capacidade de filtrar dados por região.

Você pode acessar a aplicação diretamente por este link: [Dashboard de Vendas](https://dashboardapp-avbohmkbfybfyixilpbhfn.streamlit.app/).

---

## 📋 Funcionalidades

1. **Dataset**:
   - Visualização do DataFrame com um filtro interativo para selecionar regiões específicas.

2. **Receita**:
   - Gráficos interativos para:
     - Desempenho por região.
     - Itens mais vendidos.
     - Preço médio por item.

3. **Vendedores**:
   - Métricas como:
     - Total de vendas realizadas.
     - Preço médio dos produtos vendidos.
     - Vendedor mais produtivo.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework:** Streamlit
- **Visualizações:** Matplotlib, Seaborn
- **Bibliotecas para dados:** Pandas

---

## 📂 Estrutura do Projeto

```plaintext
.
├── app.py           # Código principal do dashboard
├── data
│   └── Pedidos.csv  # Arquivo de dados
├── .gitignore       # Configuração para ignorar arquivos sensíveis
└── README.md        # Documentação do projeto
