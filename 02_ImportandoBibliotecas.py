import pandas as pd
import IPython as ip

dados = pd.read_csv("MGLU3.SA.csv")
assert isinstance(dados.shape, object)
dados.shape
dados['Open'].plot();
dados = pd.read_csv("MGLU3.SA.csv")

print(ip.core)
print(dados)

