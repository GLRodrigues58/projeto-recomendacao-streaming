import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse as sp


def criar_matriz_esparsa_com_df(df_filtrado):

    print(f"Processando {len(df_filtrado)} interações para a matriz...")

    # Criando a Pivot Table: User-Item Matrix
    user_item_matrix = df_filtrado.pivot_table(index='userId', columns='filmeId', values='rating').fillna(0)

    print("Convertendo para CSR matrix (otimização SciPy)...")
    matriz_esparsa = sp.csr_matrix(user_item_matrix.values)

    return matriz_esparsa, user_item_matrix


def buscar_index_filme(nome_busca, df_titulos):
    """
    Busca o filmeId baseado em um trecho do nome informado pelo usuário.
    """
    # Filtra usando a coluna 'titulo'
    resultados = df_titulos[df_titulos['titulo'].str.contains(nome_busca, case=False, na=False, regex=False)]

    if resultados.empty:
        print(f'Filme "{nome_busca}" não encontrado.')
        return None

    print(f"✅ Filmes encontrados:\n{resultados[['filmeId', 'titulo']]}")
    # Retorna o ID do primeiro resultado encontrado
    return resultados.iloc[0]['filmeId']


def recomendar_filmes(nome_filme, df_titulos, matriz_esparsa, user_item_matrix):
    """
    Calcula a similaridade de cosseno e retorna os 5 filmes mais parecidos.
    """
    id_filme = buscar_index_filme(nome_filme, df_titulos)

    if id_filme is not None:
        try:
            # Localiza a posição da coluna do filme selecionado na matriz pivot
            posicao = user_item_matrix.columns.get_loc(id_filme)

            # Extraindo o vetor do filme (coluna) e transportando para o cálculo
            # Matriz original é User x Filme, então compara colunas entre si
            vetor_filme = matriz_esparsa[:, posicao].T
            similaridades = cosine_similarity(vetor_filme, matriz_esparsa.T).flatten()

            # Pega os índices dos 5 filmes com maior similaridade (excluindo o próprio filme na última posição)
            indices_similares = similaridades.argsort()[-6:-1][::-1]

            print(f'\n🎬 Recomendações para quem assistiu "{nome_filme}":')

            recomendacoes = []
            for i in indices_similares:
                # Recupera o filmeId da coluna correspondente
                id_rec = user_item_matrix.columns[i]

                # Busca o nome do filme no dataframe de títulos tratados
                titulo_rec = df_titulos[df_titulos['filmeId'] == id_rec]['titulo'].values[0]
                score = similaridades[i]

                print(f'- {titulo_rec} ({score:.2%})')
                recomendacoes.append(titulo_rec)

            return recomendacoes

        except KeyError:
            print(f'⚠️ O filme "{nome_filme}" não possui avaliações suficientes na matriz.')
            return None


# --- BLOCO DE EXECUÇÃO ---
if __name__ == "__main__":
    # Caminhos dinâmicos
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_ratings = os.path.join(diretorio_atual, '..', 'data', 'rating.csv')
    caminho_titulos = os.path.join(diretorio_atual, '..', 'data', '../data/conferindo_dummies.csv')

    try:
        # 1. Carregar títulos tratados (Dicionário de Filmes)
        df_titulos = pd.read_csv(caminho_titulos)

        # 2. Carregar e padronizar ratings (Interações)
        df_notas = pd.read_csv(caminho_ratings)
        df_notas.rename(columns={'movieId': 'filmeId'}, inplace=True)

        # 3. Filtrar apenas interações dos filmes que estão no CSV tratado (mais de 50 votos)
        df_notas_filtrado = df_notas[df_notas['filmeId'].isin(df_titulos['filmeId'])] #economiza RAM

        # 4. Criar a base matemática
        matriz, dataframe_pivot = criar_matriz_esparsa_com_df(df_notas_filtrado)

        # 5. Teste Prático
        recomendar_filmes("Toy Story 3 (2010)", df_titulos, matriz, dataframe_pivot)

    except FileNotFoundError as e:
        print(f"❌ Erro: Arquivo não encontrado. Verifique a pasta 'data'. Detalhe: {e}")
