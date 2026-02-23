# 🎬 Movie Recommendation Engine: De Dados Brutos à Experiência do Usuário

Este projeto consiste em um motor de recomendação de filmes desenvolvido com Python, utilizando o dataset MovieLens. O objetivo principal foi transformar milhões de interações de usuários em recomendações personalizadas em tempo real, focando em eficiência de memória e precisão matemática.

## 📌 1. O Problema (The "Why")
Em plataformas de streaming modernas, o excesso de opções gera a "fadiga de decisão". Este projeto resolve esse problema ao entregar sugestões semanticamente relevantes baseadas no comportamento histórico de consumo, simulando a inteligência de curadoria de grandes players do mercado.

**Público-alvo:** Usuários que buscam descoberta de conteúdo personalizada.
**Relevância:** Demonstra a viabilidade de sistemas de filtragem colaborativa item-item otimizados para ambientes com recursos limitados.

## 🛠️ 2. Decisões Técnicas & Stack
A arquitetura foi pautada em **eficiência computacional** e **escalabilidade**:

* **Python & Pandas:** Base para o ETL e tratamento inicial dos dados.
* **SciPy (Sparse Matrices):** Decisão crítica para viabilizar o projeto. Matrizes densas de interação consumiriam >10GB de RAM. A conversão para **CSR Matrix** reduziu drasticamente a pegada de memória.
* **Cosine Similarity (Sklearn):** Algoritmo utilizado para calcular a proximidade vetorial entre os itens da matriz.
* **Streamlit:** Framework utilizado para o deploy da interface, garantindo uma experiência de usuário (UX) fluida e interativa.

## 🚀 3. Desafios de Engenharia & Maturidade Técnica
O desenvolvimento envolveu a superação de gargalos técnicos reais:

* **Otimização de Memória:** O sistema inicialmente falhou ao tentar alocar 10.8 GiB. 
    * *Solução:* Implementação de filtros de relevância estatística (>500 votos por filme), garantindo performance sem perda de qualidade.
* **Tratamento de Strings & RegEx:** A busca por títulos que continham o ano entre parênteses causava erros de interpretação. 
    * *Solução:* Ajuste do motor de busca para correspondência literal (`regex=False`), elevando a confiabilidade da busca.
* **Arquitetura Modular:** Separação clara entre tratamento de dados (`tratamento.py`), motor matemático (`modelagem.py`) e interface (`app.py`).

## 📈 4. Impacto & Resultados
* **Performance:** Respostas em milissegundos para o usuário final.
* **Qualidade:** Recomendações altamente correlacionadas, como a trilogia *The Godfather* e clássicos do mesmo gênero.
* **Eficiência:** Sistema otimizado para rodar em hardware comum ou instâncias de nuvem gratuitas.

## 🔮 O que eu faria diferente? (Próximos Passos)
1.  **Abordagem Híbrida:** Unir a filtragem colaborativa com metadados (gêneros) para resolver o problema de "Cold Start".
2.  **Persistência em SQL:** Migrar dos CSVs para um banco de dados relacional (PostgreSQL) para suportar atualizações em tempo real.

 <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/1af9bc62-c09c-4a9c-aff0-bc8c19adb258" />

---
**Desenvolvido por Guilherme Rodrigues** [LinkedIn](https://www.linkedin.com/in/guilherme584rodrigues/) | [GitHub](https://github.com/GLRodrigues58)
