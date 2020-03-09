import pandas as pd

url_data="http://www.portaltransparencia.gov.br/download-de-dados/servidores/202001_Servidores"
filtro_unb="Fundao Universidade de Braslia"
filtro_cargo="PROFESSOR DO MAGISTERIO SUPERIOR"

print("Carregando servidores")
iter_csv = pd.read_csv("./202001_Cadastro.csv", iterator=True, sep=';', header=0, encoding='latin-1')

servidores_unb = pd.concat([chunk[chunk['ORG_EXERCICIO'] == filtro_unb] for chunk in iter_csv])
print(type(servidores_unb))
#profs_unb = pd.concat([chunk[chunk['DESCRICAO_CARGO'] == filtro_cargo] for chunk in servidores_unb])

print("Carregados")
