from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from modules.helpers import LemmaTokenizer, stopwords
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel


class TfIdf:

    @staticmethod
    def score(df):

        stop_words = stopwords()

        # Lemmatize the stop words
        tokenizer=LemmaTokenizer()
        token_stop = tokenizer(' '.join(stop_words))

        submissions = set(df.get("submission"))

        df["tf_idf_mean"] = None
        sub_dataframe = None

        for submission in submissions:
            submission_df = df[df.submission == submission][["index", "body"]]
            # use all stop words (and ignore_tokens) with the tokenizer interfaced for sklearn above
            vectorizer = TfidfVectorizer(stop_words=token_stop, tokenizer=tokenizer)
            doc_vectors = vectorizer.fit_transform([submission] + submission_df.get("body").values.tolist())
            tfidf_scores = []
            for i in range(doc_vectors.shape[0]):
                arr = doc_vectors[i].toarray()
                tfidf_scores.append(
                    # sum(arr[0]) / len(np.nonzero(arr[0]))
                    sum(arr[0])*100 / len(arr[0])
                )

            # the first one is the submission itself

            sub_dataframe = pd.DataFrame(tfidf_scores[1:], columns=["tf_idf_mean"], index=submission_df.index)
            #print(submission_df)
            # submission_df = pd.concat([submission_df, sub_dataframe], axis=1, sort=False)
            df.update(sub_dataframe)

        return df, sub_dataframe
