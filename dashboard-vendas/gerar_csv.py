import pandas as pd

dados = {
    "mes": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"],
    "valor": [1200, 1500, 1700, 1300, 1600]
}

df = pd.DataFrame(dados)
df.to_csv("vendas.csv", index=False)
print("✅ Arquivo vendas.csv gerado com sucesso!")
