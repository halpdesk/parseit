from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from modules.helpers import LemmaTokenizer, stopwords
import pandas as pd

# https://towardsdatascience.com/how-to-rank-text-content-by-semantic-similarity-4d2419a84c32
class Similarity:

    @staticmethod
    def score(df):

        stop_words = stopwords()

        # Lemmatize the stop words
        tokenizer=LemmaTokenizer()
        token_stop = tokenizer(' '.join(stop_words))

        df["simil"] = None

        submissions = set(df.get("submission"))

        for submission in submissions:
            submission_df = df[df.submission == submission][["index", "body"]]
            # use all stop words (and ignore_tokens) with the tokenizer interfaced for sklearn above
            vectorizer = TfidfVectorizer(stop_words=token_stop, tokenizer=tokenizer)
            doc_vectors = vectorizer.fit_transform([submission] + submission_df.get("body").values.tolist())
            cosine_similarities = linear_kernel(doc_vectors[0:1], doc_vectors).flatten()
            similarity_scores = [item.item() for item in cosine_similarities[1:]]
            submission_df["topic_similarity"] = similarity_scores
            # print(f"-- {submission_df[['body', 'submission', 'topic_similarity']]}") # SEEMS TO WORK WELL!

            sim_dataframe = pd.DataFrame(similarity_scores, columns=["simil"], index=submission_df.index) # use indexes for this submission
            df.update(sim_dataframe) # updates all indexes in place

        return df
