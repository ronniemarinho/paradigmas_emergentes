import streamlit as st
import pandas as pd
import plotly.express as px

# configurando o layout da página
st.set_page_config(layout="wide")
# lendo o arquivo venda
df = pd.read_csv("vendas.csv", sep=";", decimal=",")

# convertendo a coluna data para o forma correto
df["Data"] = pd.to_datetime(df["Data"])
df = df.sort_values("Data") #ordena o Dataframa df com base na coluna "Data" de forma ascendente

df["Mês"] = df["Data"].apply(lambda x:str(x.year) + "-" + str(x.month))

#criando uma coluna nova que contem o ano e o mes
#Cria uma widget de seleção na barra lateral
month = st.sidebar.selectbox("Mês", df["Mês"].unique())
df_filtered = df[df["Mês"] == month] # aqui cria um novo dataframe chamado df_diltered que contém apenas
#as linhas do dataframe original df on o valor da coluna mes é igual ao mes selecionado



#adicionando filtro por genero
#cria um widget de seleção multipla, que permite que o usuario seleione multiplos valores p/ po filtro
generos = st.sidebar.multiselect("Gênero", df["Gênero"].unique(), default=df["Gênero"].unique())

if generos: #verifica se a listageneros não esta vazia
    #filtra o dataframe df_filtered p/ incluir apenas as linhas onde o valor da coluna genero esta presente na lista genero
    # isin() p/ verificar se cada valor da coluna Gênero esta presenta na lista generos
    df_filtered=df_filtered[df_filtered["Gênero"].isin(generos)]

st.sidebar.image("img.png", use_column_width=True)

st.title("Dashboard Fatec Adamantina")
st.write("Prof. Dr. Ronnie Shida Marinho")

st.markdown("## Resumo")
total_faturamento = df_filtered["Total"].sum()
total_vendas = df_filtered.shape[0]
avaliação_media = df_filtered["Rating"].mean()
total_produtos = df_filtered["Quantidade"].sum()

col1, col2, col3, col4 = st.columns(4)
#adicionar os cartões de dashboard em cada coluna
with col1:
    st.metric(label="Total Faturamento", value=f"R${total_faturamento:.2f}")
with col2:
    st.metric(label="Total Vendas", value=total_vendas)
with col3:
    st.metric(label="Total Produtos Vendidos", value=total_produtos)
with col4:
    st.metric(label="Avaliação Média", value=f"{avaliação_media:.2f}")

# dividir a tela em colunas para os gráficos
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# criar o gráfico de faturamento por dia
fig_date = px.bar(df_filtered, x="Data", y="Total", color="Cidade", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtered, x="Data", y="Linha de produto", color="Cidade", title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

# calcular o faturamento total por cidade
#criando umum novo dataframe chamado citY-total que contém a somatória do faturamento total agrupado
#por cidade
city_total = df_filtered.groupby("Cidade")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="Cidade", y="Total", title="Faturamento por cidade")
col3.plotly_chart(fig_city, use_container_width=True)

#criando o gráfico de pizza para exibir o faturamento por tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Pagamento", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

# calcular a avaliação média por cidade
city_total = df_filtered.groupby("Cidade")[["Rating"]].mean().reset_index()

fig_rating = px.bar(df_filtered, y="Rating", x="Cidade", title="Avaliação Média")
col5.plotly_chart(fig_rating, use_container_width=True)

vendas_por_produto_e_mes = df_filtered.groupby(["Mês","Linha de produto"])[["Quantidade"]].sum().reset_index()
fig_vendas_por_produto_e_mes= px.bar(vendas_por_produto_e_mes, x="Linha de produto", y="Quantidade", color="Mês",
                                     title="Total de vendas por Mês e por linha de produto", facet_row="Mês",
                                     height=600, width=1200)

#exibir o gráfico
st.plotly_chart(fig_vendas_por_produto_e_mes, use_container_width=True)