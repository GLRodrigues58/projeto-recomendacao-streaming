import os
import pandas as pd

# Configuração de caminhos
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_movies = os.path.join(diretorio_atual, '..', 'data', 'movie.csv')
caminho_ratings = os.path.join(diretorio_atual, '..', 'data', 'rating.csv')

# 1. Importando bases de dados
filmes_df = pd.read_csv(caminho_movies)
rate_df = pd.read_csv(caminho_ratings)

# 2. Mesclando e renomeando
filmes_df = filmes_df.merge(rate_df, on='movieId', how='inner')
filmes_df.rename(columns={'movieId':'filmeId', 'genres':'genero', 'title':'titulo'}, inplace=True)

# 3. One-Hot Encoding dos gêneros
generos_dummies = filmes_df['genero'].str.get_dummies('|')
filmes_completos = pd.concat([filmes_df, generos_dummies], axis=1)

# 4. Agrupamento Inteligente
# Criando um dicionário que diz: "Para os gêneros use o máximo (1), para o rating use média e contagem"
agregacoes = {col: 'max' for col in generos_dummies.columns}
agregacoes['rating'] = ['mean', 'count']
agregacoes['filmeId'] = 'first'

# Criando a tabela final agrupada por título
filmes_final = filmes_completos.groupby('titulo').agg(agregacoes).reset_index()

# 5. Achatando as colunas
filmes_final.columns = ['titulo'] + list(generos_dummies.columns) + ['nota_media', 'total_votos', 'filmeId']

# 6. Filtro de Relevância e Ordenação
filmes_populares = filmes_final[filmes_final['total_votos'] > 500].copy()
filmes_populares.sort_values(by='nota_media', ascending=False, inplace=True)

print("✅ Tabela Final com Gêneros e Métricas:")
print(filmes_populares.head())

filmes_populares.to_csv('conferindo_dummies.csv', index=False)
