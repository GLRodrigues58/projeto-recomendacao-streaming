import streamlit as st
import pandas as pd
import os
from notebooks.modelagem import criar_matriz_esparsa_com_df, recomendar_filmes

st.set_page_config(page_title='Streamlit - Recomendação', page_icon='🎥')

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_titulos = os.path.join(diretorio_atual, '..', 'data', 'conferindo_dummies.csv')
caminho_ratings = os.path.join(diretorio_atual, '..', 'data', 'rating.csv')

@st.cache_resource #para não processar a matriz toda vez que clicar no botão
def carregar_sistema_filmes():
    df_titulos = pd.read_csv(caminho_titulos)
    df_notas = pd.read_csv(caminho_ratings)
    df_notas.rename(columns={'movieId': 'filmeId'}, inplace=True)
    #Filtro para rodar melhor
    df_notas_filtrado = df_notas[df_notas['filmeId'].isin(df_titulos['filmeId'])]

    matriz, dataframe_pivot = criar_matriz_esparsa_com_df(df_notas_filtrado)
    return df_titulos, matriz, dataframe_pivot

#Interface Principal
st.title('🎥 Sistema de Recomendação de Filmes')
st.write('Carregando base de dados e processando inteligência...')

with st.spinner('Recomendando filmes...'):
    df_titulos, matriz, dataframe_pivot = carregar_sistema_filmes()
st.success('Sistema Pronto!')

#Seleção do Filme
filme_selecionado = st.sidebar.selectbox(
    "Digite ou selecione um filme:",
    df_titulos['titulo'].values)

if st.button('Recomendar'):
    st.write(f'### Você selecionou: {filme_selecionado}')

    resultados = recomendar_filmes(filme_selecionado, df_titulos, matriz, dataframe_pivot)

    if resultados:
        st.write('#### 🍿 Filmes parecidos que você pode gostar:')
        for filme in resultados:
            st.info(filme)
    else:
        st.error('Infelizmente não encontramos recomendações para este título.')

#streamlit run app/app.py
#python -m streamlit run app/app.py
