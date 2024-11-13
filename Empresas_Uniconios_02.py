#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

import warnings
warnings.filterwarnings('ignore')
#%%

Base_Dados = pd.read_csv('unicórnios até setembro de 2022.csv',sep=',')
Base_Dados
#%%
# verificar dimensão
Base_Dados.shape
#%%
#primeiros registros
Base_Dados.head()
#%%
# Verificar colunas 
Base_Dados.columns

#%%
# Renomear
Base_Dados.rename( columns={
    'Company' : 'Empresa',
    'Valuation ($B)' : 'Valor ($)',
    'Date Joined' : 'Data de Adesão',
    'Country' : 'Pais',
    'City' : 'Cidade',
    'Industry': 'Setor',
    'Select Investors': 'Investidores',
}, inplace=True )

Base_Dados
#%%
# Verificar Tipo do informação
Base_Dados.info()
#%%
# Campos nulos
Base_Dados.isnull().sum()
#%%
# Grafica
plt.figure( figsize=(15,6) )
plt.title('Analisando Campos Nulos')
sns.heatmap( Base_Dados.isnull(), cbar=False )
plt.show()
#%%

# Campos unicos
Base_Dados.nunique()
#%%
# Valores Unicos
Base_Dados['Setor'].unique()
Base_Dados['Setor']
#%%
# Valores Unicos - Rank
Base_Dados['Setor'].value_counts()
#%%
# Valores Unicos normalize  - Rank por porcentagem 
Base_Dados['Setor'].value_counts( normalize=True )
#%%
plt.figure( figsize=(15,6) )
plt.title('Analise dos Setores')
plt.bar( Base_Dados['Setor'].value_counts().index, Base_Dados['Setor'].value_counts()  )
plt.xticks( rotation=45, ha='right' )
plt.show()
#%%
Analise = round( Base_Dados['Pais'].value_counts( normalize=True ) * 100, 1 )
Analise
#%%
# Plot geral dos Paises
plt.figure( figsize=(30,6) )
plt.title('Analise dos Paises gerador de Unicornios')
plt.pie(
    Analise,
    labels = Analise.index,
    shadow=True,
    startangle=90,
    autopct='%1.1f%%'
)
plt.show()
#%%
# Plot dos top 5 paises 
plt.figure( figsize=(15,6) )
plt.title('Analise dos Paises gerador de Unicornios - Top 5')
plt.pie(
    Analise.head(5),
    labels = Analise.index[0:5],
    shadow=True,
    startangle=90,
    autopct='%1.1f%%'
)
plt.show()
#%%
# Conversão para Data
Base_Dados['Data de Adesão'] = pd.to_datetime( Base_Dados['Data de Adesão'] )
Base_Dados['Data de Adesão'].head()
#%%
# Extrair o Ano e Mes
Base_Dados['Mes'] = pd.DatetimeIndex( Base_Dados['Data de Adesão'] ).month
Base_Dados['Ano'] = pd.DatetimeIndex( Base_Dados['Data de Adesão'] ).year
Base_Dados.head()


#%%
# Tabela Analitica 
soma_por_pais = Base_Dados.groupby('Pais')['Valor ($)'].sum().reset_index()
soma_por_pais
#%%
# Tabela organizada do maior para o menor
soma_por_pais = soma_por_pais.sort_values(by='Valor ($)', ascending=False)
soma_por_pais
#%%
#Grafico 
plt.figure( figsize=(15,6) )
plt.plot( soma_por_pais['Pais'], soma_por_pais['Valor ($)'] )
plt.title('Analise do Valor por Pais')
plt.xticks( rotation=45, ha='right')
plt.show()