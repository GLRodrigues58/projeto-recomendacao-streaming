# 🎬 Sistema de Recomendação de Filmes - MovieLens

Este projeto desenvolve um motor de recomendação capaz de processar milhões de avaliações de usuários para identificar similaridades entre títulos e sugerir conteúdos personalizados. 🚀

## 📊 Sobre o Projeto
O objetivo principal foi transformar dados brutos de streaming em uma estrutura matemática que o computador consiga processar, utilizando técnicas de **Big Data** e **Machine Learning** para suporte à tomada de decisão.

## 🛠️ Tecnologias e Técnicas Utilizadas
* **Linguagem:** Python.
* **Manipulação de Dados:** Pandas para limpeza, merge de tabelas e agregações complexas (`groupby`).
* **Engenharia de Atributos:** **One-Hot Encoding** para conversão de gêneros cinematográficos (variáveis categóricas) em matrizes binárias.
* **Métricas Analíticas:** Cálculo de nota média e volume de votos para filtragem de relevância (Filmes Populares).
* **Interface:** Protótipo em desenvolvimento utilizando Streamlit.

## 📈 Resultados Alcançados
* Processamento eficiente de um dataset volumoso (MovieLens).
* Criação de uma matriz de 23 colunas representando a "identidade" de cada filme.
* Implementação de filtros de relevância para garantir a qualidade das recomendações (mínimo de 50 avaliações).
* Processamento em Larga Escala: Conversão de DataFrames para Matrizes Esparsas (CSR) usando SciPy, reduzindo drasticamente o uso de memória RAM.
* Algoritmo de Recomendação: Implementação da Similaridade de Cosseno (Scikit-Learn) para calcular a afinidade entre filmes.
* Busca Inteligente: Função de busca por títulos com tratamento de strings e mapeamento de IDs.

  <img width="996" height="469" alt="image" src="https://github.com/user-attachments/assets/1fdc5c86-8d16-459d-871a-4e243fc83881" />


## 🚀 Próximos Passos
- [ ] Finalização da interface interativa no Streamlit.
<img width="1600" height="896" alt="image" src="https://github.com/user-attachments/assets/b0ad5cb5-8cf7-4e40-887e-d7e1f763cbfc" />


---
**Desenvolvido por Guilherme Rodrigues** [LinkedIn](https://www.linkedin.com/in/guilherme584rodrigues/) | [GitHub](https://github.com/GLRodrigues58)
