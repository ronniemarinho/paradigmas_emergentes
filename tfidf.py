import nltk
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
stopwords = nltk.corpus.stopwords.words('portuguese')
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

corpus = ['no meio do caminho tinha uma pedra',
          'tinha uma pedra no meio do caminho',
          'tinha uma pedra',
          'no meio pedra doi caminho tinha uma pedra']

vectorizer = CountVectorizer(stop_words=stopwords)
vetores = vectorizer.fit_transform(corpus)
print("Vetores", vetores)
#vocabulario
vocab = vectorizer.get_feature_names_out()
print(vocab)

df_count = pd.DataFrame(data=vetores.toarray(), columns=vocab)
print("\nCount\n")
print(df_count)

vectorizer = TfidfVectorizer(stop_words=stopwords)
vectors = vectorizer.fit_transform(corpus)
print(vectors)

vocab_tfidf = vectorizer.get_feature_names_out()
print("Vocabulario TF-IDF")
print(vocab_tfidf)

df_tfidfvect = pd.DataFrame(data=vectors.toarray(), columns=vocab_tfidf)
print("\nTF-IDF Vectorizer\n")
print(df_tfidfvect)

df_count.to_csv('count.csv', index=False)
df_tfidfvect.to_csv('tfidf.csv', index=False)

palavras_tfidf= df_tfidfvect.sum().to_dict()

#Criar a nuvem de palavra com base nos valores tf idf
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      min_font_size=10).generate_from_frequencies(palavras_tfidf)

#exibir a nuvem de palavras
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
