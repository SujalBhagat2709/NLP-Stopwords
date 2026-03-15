from nltk.corpus import stopwords
import nltk

nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

print("Total stopwords:", len(stop_words))

print(list(stop_words)[:20])