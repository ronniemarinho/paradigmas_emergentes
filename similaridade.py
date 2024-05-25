import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import manhattan_distances

#Exemplo de documentos

documents = ["Cano é eleito o melhor jogador do ano",
             "Novas regras no volleybal entra em vigor em 2025",
             "Ladrão rouba carro e deixa ferido",
             "Aprenda a fazer receita de macarrão ao molho madeira",
             "Palmeiras vence o Ituano por 1 a 0 e vai a final do paulista",
             "Receita de escondidinho de carne com abacaxi",
             "Plano para atacar Moro custou 1.2 milhões",
             "Lula concede aumento nos salários dos aposentados",
             "Messi discursa para torcida após 2 a 0 sobre Panamá",
             "Ostentação e até cão armado: como era a vida no rio de traficantes de outros estados",
             "Os estadios da copa do mundo"]

vectorizer = TfidfVectorizer()

#Calculando a matriz Tf-IDF
X = vectorizer.fit_transform(documents)
print(X)
similaridade = cosine_similarity(X)

noticia = 7 #índice da primeira notícia
similaridades_primeira = similaridade[noticia]
ranking_similaridades = np.argsort(similaridades_primeira)[::-1] #índices das similaridades ordenadas

# Imprima as 2 notícias mais similares à primeira
print('Similaridade do cosseno')
for i in range(1, 3):
    indice_noticia_similar = ranking_similaridades[i]
    similaridade_noticia = similaridades_primeira[indice_noticia_similar]
    print(f"Notícia {indice_noticia_similar + 1}: Similaridade de {similaridade_noticia:.2f}")
    print(f"Texto: {documents[indice_noticia_similar]}")
    print()

print('Distancia Euclidiana')
distancias = euclidean_distances(X)

distancias_primeira = distancias[noticia]
ranking_distancias = np.argsort(distancias_primeira)

for i in range(1,3):
    indice_documento_proximo = ranking_distancias[i]
    distancia_documento = distancias_primeira[indice_documento_proximo]
    print(f"Notícia {indice_documento_proximo + 1}: Similaridade de {distancia_documento:.2f}")
    print(f"Texto: {documents[indice_documento_proximo]}")
    print()

distancia_manhattan = manhattan_distances(X)
distancias_m = distancia_manhattan[noticia]
ranking_m = np.argsort(distancias_m)
print("Distancia de Manhattan")

for i in range(1,3):
    indice_documento_proximo = ranking_m[i]
    distancia_documento = distancias_m[indice_documento_proximo]
    print(f"Notícia {indice_documento_proximo + 1}: Similaridade de {distancia_documento:.2f}")
    print(f"Texto: {documents[indice_documento_proximo]}")
    print()



