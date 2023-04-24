import pandas as pd
import matplotlib.pyplot as plt

gasolina = pd.read_csv('./gasolina.csv')

plt.plot(gasolina["dia"], gasolina["venda"])
plt.xlabel('dia')
plt.ylabel('venda')
plt.savefig('gasolina.png', format='png')
plt.show()
