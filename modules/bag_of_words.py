from functools import lru_cache
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from modules.helpers import LemmaTokenizer, stopwords
from functools import lru_cache
import pandas as pd
import numpy as np

class BagOfWords:

    @staticmethod
    def score(df):

        # most_freq = heapq.nlargest(200, wordfreq, key=wordfreq.get)
        messages = df.get("body")

        # Lemmatize the stop words
        tokenizer=LemmaTokenizer()
        stop_words = stopwords()
        token_stop = tokenizer(' '.join(stop_words))

        count_vectorizer = CountVectorizer(stop_words=token_stop, tokenizer=tokenizer)
        count_data = count_vectorizer.fit_transform(messages)

        cv_dataframe = pd.DataFrame(count_data.toarray(),columns=count_vectorizer.get_feature_names())

        df = pd.concat([df, cv_dataframe], axis=1, sort=False)


        #bag_of_words = pd.DataFrame.sparse.from_spmatrix(tfidf_sparse_matrix)

        #df = pd.concat([df, bag_of_words], axis=1, sort=False)

        #countVec_count = countVectorizer.transform(messages)
        #occ = np.asarray(countVec_count.sum(axis=0)).ravel().tolist()
        #bowListFrame = pd.DataFrame({'term': countVectorizer.get_feature_names(), 'occurrences': occ})
        #bowListFrame.sort_values(by='occurrences', ascending=False).head(60)

        #tfidfTransformer = TfidfTransformer()
        #weights = tfidfTransformer.fit_transform(countVec_count)
        #weightsFin = np.asarray(weights.mean(axis=0)).ravel().tolist()

        #tfidfFrame = pd.DataFrame({'term': countVectorizer.get_feature_names(), 'weight': weightsFin})
        # tfidfFrame.sort_values(by='weight', ascending=False).head(20)
        # print(tfidfFrame)

        #df = pd.concat([df, tfidfFrame], axis=1, sort=False)


        return df
