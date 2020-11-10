from modules.helpers import lemmatize, tokenize, stopwords, badwords
import pandas as pd
import numpy as np

# bad words from:
# https://github.com/snguyenthanh/better_profanity/blob/master/better_profanity/profanity_wordlist.txt
# https://github.com/ani10030/bad-words-detector/blob/master/datasets/english.csv

class WordStats:

    @staticmethod
    def count_words(documents):
        bad_words = badwords()
        stop_words = stopwords()

        words_count_list = [0] * len(documents)
        bad_words_count_list = [0] * len(documents)
        bad_words_list = [[]] * len(documents)
        stop_words_count_list = [0] * len(documents)

        for i in range(len(documents)):
            c_word_count = 0
            c_stop_words_count = 0
            c_bad_words_count = 0
            c_bad_word = []
            document = documents[i]
            freq_table = {}
            for word, tag in tokenize(document):
                lemma = lemmatize(word, tag)
                if word in bad_words or lemma in bad_words:
                    c_bad_words_count = c_bad_words_count + 1
                    c_bad_word.append(word)
                if word in stop_words or lemma in stop_words:
                    c_stop_words_count = c_stop_words_count + 1
                else:
                    c_word_count = c_word_count + 1

            words_count_list[i] = c_word_count
            stop_words_count_list[i] = c_stop_words_count
            bad_words_count_list[i] = c_bad_words_count
            bad_words_list[i] = c_bad_word[1:]

        return words_count_list, stop_words_count_list, bad_words_count_list, bad_words_list

    @staticmethod
    def score(df):

        documents = df.get("body")
        word_count_list, stop_words_count_list, bad_words_count_list, bad_words_list = WordStats.count_words(documents)

        records = np.array([word_count_list, stop_words_count_list, bad_words_count_list])
        # print(records)
        wc_dataframe = pd.DataFrame.from_records(data=records.T, columns=["word_count", "stop_words_count", "bad_words_count"])

        df = pd.concat([df, wc_dataframe], axis=1, sort=False)
        # df["words_count"] = word_count_list
        # df["stop_words_count"] = stop_words_count_list
        # df["bad_words_count"] = bad_words_count_list
        # df["bad_words"] = bad_words_list

        return df
