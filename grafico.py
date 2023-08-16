import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_gasolina = pd.read_csv("gasolina.csv")
df_gasolina.rename(columns={'dia': 'Dias', 'venda': 'Preços'}, inplace=True)


graf_linha = sns.lineplot(data=df_gasolina, x="Dias", y="Preços", marker='o', markerfacecolor='blue', markeredgecolor='blue')
graf_linha.lines[0].set_color("red")
graf_linha.set_title("Preço da gasolina ao decorrer de 10 dias")
plt.savefig("gasolina.png")
plt.show()