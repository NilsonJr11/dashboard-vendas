import pandas as pd
import matplotlib.pyplot as plt

# Lê os dados
df = pd.read_csv("vendas.csv")

# Agrupa por mês
total_por_mes = df.groupby("mes")["valor"].sum()

# Gera o gráfico
plt.figure(figsize=(8,5))
plt.bar(total_por_mes.index, total_por_mes.values, color='skyblue')
plt.title("Vendas por Mês")
plt.xlabel("Mês")
plt.ylabel("Valor (R$)")
plt.tight_layout()
plt.show()




