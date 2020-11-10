import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

class BigramOfWords:

    @staticmethod
    def score(df):

        messages = df.get("body")
        c_vector = CountVectorizer(ngram_range=(2,2), # to use bigrams ngram_range=(2,2)
                                stop_words='english')
        #transform
        count_data = c_vector.fit_transform(messages)

        #create dataframe
        cv_dataframe=pd.DataFrame(count_data.toarray(),columns=c_vector.get_feature_names())

        #df["bag_of_words"] = cv_dataframe
        df = pd.concat([df, cv_dataframe], axis=1, sort=False)
        # df.update(cv_dataframe)
        return df
        #df.update(submission_df)
