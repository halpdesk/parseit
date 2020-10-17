from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from nltk.corpus import stopwords
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np

class LemmaTokenizer:
    ignore_tokens = [',', '.', ';', ':', '"', '``', "''", '`', '[removed]', '>', '*', '_']
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc) if t not in self.ignore_tokens]

class TfIdf:

    def __init__(self):
        # stop_words = set(stopwords.words("english"))
        pass

    def slow_way(self, df):
        messages = df.get("body")
        cv=CountVectorizer()
        word_count_vector=cv.fit_transform(messages)
        word_count_vector.shape
        tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
        tfidf_transformer.fit(word_count_vector)
        # print idf values
        df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(),columns=["idf_weights"])

        # sort ascending
        df_idf.sort_values(by=['idf_weights'])

        # count matrix
        count_vector=cv.transform(messages)

        # tf-idf scores
        tf_idf_vector=tfidf_transformer.transform(count_vector)

        feature_names = cv.get_feature_names()

        #get tfidf vector for first document
        first_document_vector=tf_idf_vector[0]

        #print the scores
        df_tdidf = pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"])
        df_tdidf.sort_values(by=["tfidf"],ascending=False)

        return df_tfidf

    def fast_way(self, df):
        messages = df.get("body")

        # settings that you use for count vectorizer will go here
        tfidf_vectorizer=TfidfVectorizer(use_idf=True)

        # just send in all your docs here
        tfidf_vectorizer_vectors=tfidf_vectorizer.fit_transform(messages)

        # get the first vector out (for the first document)
        first_vector_tfidfvectorizer=tfidf_vectorizer_vectors[0]

        # place tf-idf values in a pandas data frame
        df_tfidf = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tfidf"])
        df_tfidf.sort_values(by=["tfidf"],ascending=False)

        return df_tfidf

    def score(self, df):

        stop_words = set(stopwords.words("english"))

        # Lemmatize the stop words
        tokenizer=LemmaTokenizer()
        token_stop = tokenizer(' '.join(stop_words))

        submissions = set(df.get("submission"))

        for submission in submissions:
            submission_df = df[df.submission == submission]
            # use all stop words (and ignore_tokens) with the tokenizer interfaced for sklearn above
            vectorizer = TfidfVectorizer(stop_words=token_stop, tokenizer=tokenizer)
            doc_vectors = vectorizer.fit_transform([submission] + submission_df.get("body").values.tolist())
            tfidf_scores = []
            for i in range(doc_vectors.shape[0]):
                arr = doc_vectors[i].toarray()
                tfidf_scores.append(
                    sum(arr[0]) / len(np.nonzero(arr[0]))
                )
            submission_df["tfidf_score"] = tfidf_scores[1:] # the first one is the submission itself
            df.update(submission_df)

        return df
