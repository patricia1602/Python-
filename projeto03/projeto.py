import pandas as pd
import plotly.express as px

dados = pd.read_excel("vendas.xlsx")

dados["loja"].value_counts()

dados.tail()

dados.shape

dados.info()

# faturamneto por loja
dados.groupby("loja")["preco"].sum().to_frame

# faturamento 
dados_agrupados = dados.groupby(["estado", "cidade", "loja", "forma_pagamento"])["preco"].sum().to_frame()

dados_agrupados.to_excel("Faturamento.xlsx")

lista_colunas = ["loja", "cidade", "estado", "tamanho", "local_consumo"]

for coluna in lista_colunas:
    grafico = px.histogram(dados, x=coluna,
                    y="preco",
                    text_auto=True,
                    title="Faturamento",
                    color="forma_pagamento")
    grafico.show()
    grafico.write_html(f"Faturamento-{coluna}.html")

    listas_nomes = ["Vinícius, Patrícia, Pietro"]

#listas_nomes
for nome in listas_nomes:
    print(nome)