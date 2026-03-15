import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

def remove_stopwords(text):
    words = text.split()
    filtered = [w for w in words if w.lower() not in stop_words]
    return " ".join(filtered)


text = "This is a simple example of natural language processing"

print(remove_stopwords(text))