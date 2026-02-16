import streamlit as st
import pandas as pd
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_movies = os.path.join(diretorio_atual, '..', 'data', 'movie.csv')


st.set_page_config(page_title='Streamlit - Recomendação', page_icon='🎥')

st.title('🎥 Sistema de Recomendação de Filmes')
st.write('Bem-vindo ao protótipo do projeto de recomendação utilizando MovieLens')

@st.cache_data
def load_data():
    df = pd.read_csv(caminho_movies)
    df.rename(columns={'title': 'titulo'}, inplace=True)
    return df

df = load_data()

filme_selecionado = st.sidebar.selectbox("Digite ou selecione um filme:", df['titulo'].values)

if st.button('Recomendar'):
    st.write(f'Você selecionou: {filme_selecionado}')
    st.info('Em breve: #Recomendações baseadas em similaridade de cosseno')

#streamlit run app/app.py