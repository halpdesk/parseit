from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from modules.helpers import LemmaTokenizer, stopwords
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
# from sklearn.metrics.pairwise import linear_kernel


class TfIdf:

    @staticmethod
    def score(df):

        messages = df.get("body")


        # Lemmatize the stop words
        tokenizer=LemmaTokenizer()
        stop_words = stopwords()
        token_stop = tokenizer(' '.join(stop_words))


        # use all stop words (and ignore_tokens) with the tokenizer interfaced for sklearn above
        tfidf_vectorizer = TfidfVectorizer(stop_words=token_stop, tokenizer=tokenizer)
        tfidf_sparse_matrix = tfidf_vectorizer.fit_transform(messages)
        tfidf_dataframe = pd.DataFrame.sparse.from_spmatrix(tfidf_sparse_matrix)

        df = pd.concat([df, tfidf_dataframe], axis=1, sort=False)


        # submissions = set(df.get("submission"))
        # for submission in submissions:
        #     submission_df = df[df.submission == submission][["index", "body"]]
        #     doc_vectors = tfidf_vectorizer.fit_transform([submission] + submission_df.get("body").values.tolist())
        #     tf_idf_scores = doc_vectors.toarray()
        #     submission_dataframe = pd.DataFrame(tf_idf_scores[1:], index=submission_df.index)

        return df
