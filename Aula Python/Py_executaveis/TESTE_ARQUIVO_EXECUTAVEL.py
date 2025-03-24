# %% [markdown]
# ### https://pandas.pydata.org/docs/reference/api/pandas.concat.html

# %%
import pandas as pd
import os

vendas2021 = pd.read_excel(r"C:\Users\TERRA\JAVA\dio-java-basico\udemy1\Origem\arquivos_excel\Consolidar\Vendas2021.xlsx")
vendas2022 = pd.read_excel(r"C:\Users\TERRA\JAVA\dio-java-basico\udemy1\Origem\arquivos_excel\Consolidar\Vendas2022.xlsx")
vendas2023 = pd.read_excel(r"C:\Users\TERRA\JAVA\dio-java-basico\udemy1\Origem\arquivos_excel\Consolidar\Vendas2023.xlsx")

# %%
vendas2021.head(5)

# %%
vendas2022.head(5)

# %%
vendas2023.head(5)

# %%
#Consolidado=pd.concat([vendas2021,vendas2022,vendas2023]) # com indice
Consolidado=pd.concat([vendas2021,vendas2022,vendas2023],ignore_index=True) # Sem indice
#Consolidado=pd.concat([vendas2021,vendas2022,vendas2023],keys=["2021","2022","2023"]) # identificando tabelas 


# %%
Consolidado.head(30)

# %% [markdown]
# ##### Verificar se arquivo ja existe e adicionar no final 
# 
# 

# %%
# Caminho da pasta onde será salvo o arquivo Excel
pasta_destino = r'C:\Users\TERRA\JAVA\dio-java-basico\udemy1\Origem\arquivos_excel\Consolidar\Concat\\'

# Nome do arquivo Excel (variável)
nome_arquivo = 'VendasConcat.xlsx'

# Lista para armazenar os dados dos arquivos
dados = []

# Caminho completo do arquivo Excel
Caminho_Completo = pasta_destino + nome_arquivo 

if os.path.exists(Caminho_Completo):
    # Carregar o arquivo Excel consolidado existente em um DataFrame
    df_existente = pd.read_excel(Caminho_Completo)
    # Adicionar os dados existentes ao DataFrame consolidado
    dados.append(df_existente)



# Salvar o DataFrame consolidado como arquivo Excel
Consolidado.to_excel(Caminho_Completo, index=False)


