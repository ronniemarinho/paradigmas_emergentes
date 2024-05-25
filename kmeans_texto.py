from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
from nltk.corpus import stopwords

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

lowercase_list = [e.lower() for e in documents]

vectorizer = TfidfVectorizer(stop_words=stopwords.words('portuguese'))
X = vectorizer.fit_transform(lowercase_list)
print(X)

tf_idf = pd.DataFrame(data = X.toarray(), columns=vectorizer.get_feature_names_out())
print(tf_idf)

k = 4
model = KMeans(n_clusters=k, init='k-means++', random_state=0)
model.fit(X)
labels = model.labels_
print("Labels dos documentos")
print(labels)

order_centroids = model.cluster_centers_.argsort()[:,::-1]

terms = vectorizer.get_feature_names_out()
print()
print(terms)
print(len(terms))

for i in range(k):
    print("Cluster %d"% i),
    for ind in order_centroids[i,:4]:
        print(' %s' %terms[ind])

print("\n")


