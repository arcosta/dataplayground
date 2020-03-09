import pandas as pd

url_data="http://www.portaltransparencia.gov.br/download-de-dados/servidores/202001_Servidores"
filtro_unb="Fundação Universidade de Brasília"
filtro_cargo="PROFESSOR DO MAGISTERIO SUPERIOR"

print("Carregando servidores")
iter_csv = pd.read_csv("./202001_Cadastro.csv", sep=';', header=0, encoding='latin-1')

servidores_unb = iter_csv[iter_csv['ORG_EXERCICIO'].str.contains(filtro_unb)]

profs_unb = servidores_unb[servidores_unb['DESCRICAO_CARGO'].str.contains(filtro_cargo)]


print("Carregados {} professore de {} servidores".format(len(profs_unb), len(servidores_unb)))
