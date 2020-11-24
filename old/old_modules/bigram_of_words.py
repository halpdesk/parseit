import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from modules.helpers import LemmaTokenizer, stopwords

class BigramOfWords:

    @staticmethod
    def score(df):

        messages = df.get("body")


        # Lemmatize the stop words
        tokenizer=LemmaTokenizer()
        stop_words = stopwords()
        token_stop = tokenizer(' '.join(stop_words))

        # to use bigrams ngram_range=(2,2)
        count_vectorizer = CountVectorizer(ngram_range=(2,2), stop_words=token_stop, tokenizer=tokenizer)
        #transform
        count_data = count_vectorizer.fit_transform(messages)

        #create dataframe
        cv_dataframe = pd.DataFrame(count_data.toarray(),columns=count_vectorizer.get_feature_names())

        #df["bag_of_words"] = cv_dataframe
        df = pd.concat([df, cv_dataframe], axis=1, sort=False)
        # df.update(cv_dataframe)
        return df
        #df.update(submission_df)
