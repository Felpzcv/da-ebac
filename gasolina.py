import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv("gasolina.csv")
gasolina_df.rename(columns={'dia': 'Dias', 'venda' : 'Preços'}, inplace=True)


grafico_linha = sns.lineplot(data=gasolina_df, x="Dias", y="Preços", marker='X', markerfacecolor='red', markeredgecolor='red')
grafico_linha.set_title("Preço da gasolina ao longo de 10 dias em São Paulo")
plt.savefig("gasolina.png")
plt.show()