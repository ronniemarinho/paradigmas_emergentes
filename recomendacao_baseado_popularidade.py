import pandas as pd
#carrega os dados dos filmes, especificando o separador, a codificação e a ausencia de cabeçalho
movies_df = pd.read_csv('C:/Users/professor.SERVER/Downloads/ml-100k/u.item', sep='|',
                        encoding='latin-1',header=None)
# renomear as colunas do movie_df
movies_df.columns = ['movie_id','title','release_date','video_release_date','imdb_url','unknown','action',
                     'adventure','animation','children','comedy','crime','documentary','drama','fantasy',
                     'film_noir','horror','musical','mystery','romance','sci_fi','thriller','war','western']

ratings_df= pd.read_csv('C:/Users/professor.SERVER/Downloads/ml-100k/u.data', sep='\t',
                        encoding='latin-1',header=None)

# renomear as colunas de ratings_df
ratings_df.columns = ['user_id','movie_id','rating','timestamp']

# Calcular a contagem de avaliações para cada filme
#Agrupa as avaliações por filme e calcula a contagem de avsaliações para cada filme.
movie_ratings_count = ratings_df.groupby('movie_id')['rating'].count().reset_index()

# Renomear as colunas do dataframe movie_ratings_count
movie_ratings_count.columns = ['movie_id','ratings_count']

#ordenar os filmes por contagem de avaliações em ordem decrescente
popular_movies = movie_ratings_count.sort_values('ratings_count', ascending=False)

#Exibir as reomendaçoes dos filmes mais populares
num_recommendations=50 #define o número de filmes a serem recomendados
#seleciona os primeiros num_recommendations filmes mais popuçlares como recomendações
recommended_movies= popular_movies.head(num_recommendations)
# juntar as informações dos filmes.recomendados
#combina as informações dos filmes recomendados com as infor completas dos filmes com base no movie_id
recommended_movies= pd.merge(recommended_movies, movies_df[['movie_id','title']],
                             on='movie_id',how='left')

print("Recomendações de filmes populares")
#imprime as recomendaçoes de filmes populares
print(recommended_movies[['movie_id','title','ratings_count']])
