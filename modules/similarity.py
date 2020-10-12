from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# https://towardsdatascience.com/how-to-rank-text-content-by-semantic-similarity-4d2419a84c32

# Interface lemma tokenizer from nltk with sklearn
class LemmaTokenizer:
    ignore_tokens = [',', '.', ';', ':', '"', '``', "''", '`', '[removed]', '>', '*', '_']
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc) if t not in self.ignore_tokens]


class Similarity:

    def __init__(self):
        pass

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
            cosine_similarities = linear_kernel(doc_vectors[0:1], doc_vectors).flatten()
            similarity_scores = [item.item() for item in cosine_similarities[1:]]
            submission_df["topic_similarity"] = similarity_scores
            # print(f"-- {submission_df[['body', 'submission', 'topic_similarity']]}") # SEEMS TO WORK WELL!

            df.update(submission_df) # updates all indexes in place

        return df
