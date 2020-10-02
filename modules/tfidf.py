from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import pandas as pd

class TfIdf:

    def __init__(self):
        stop_words = set(stopwords.words("english"))
        self.vectorizer = TfidfVectorizer(**{
            "min_df":1,
            # "max_df":2,
            # "stop_words":stop_words,
            "stop_words":"english",
            "ngram_range":(1,2)
        })

    def measure(self, document):
        messages = [item["body"] for item in document]
        tfidf = self.vectorizer.fit_transform(messages)

        pairwise_similarity = tfidf * tfidf.T

        dense = tfidf.todense()
        denselist = dense.tolist()
        df = pd.DataFrame(denselist)
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            print(df)
        # df = pd.DataFrame(denselist, columns=feature_names)
