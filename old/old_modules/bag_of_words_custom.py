from functools import lru_cache
from modules.helpers import lemmatize, tokenize, stopwords, badwords
from functools import lru_cache

class BagOfWords:

    @staticmethod
    @lru_cache
    def all_words(messages):
        """ Uses stemmer for english """
        stop_words = stopwords()

        all_words = []
        for i in range(len(messages)):
            msg = messages[i]
            for word,pos in tokenize(msg):
                lemma = lemmatize(word, pos)
                if lemma not in stop_words:
                    all_words.append(lemma)

        return list(set(all_words))

    @staticmethod
    def score(df):

        # most_freq = heapq.nlargest(200, wordfreq, key=wordfreq.get)
        messages = df.get("body")
        all_words = BagOfWords.all_words(messages)
        stop_words = stopwords()

        bag_of_words_list = [[]] * len(messages)
        for i in range(len(messages)):
            sentence = messages[i]
            words_tags = tokenize(sentence)
            vector = [0] * len(all_words)
            for j in range(len(words_tags)):
                lemma = lemmatize(words_tags[j][0], words_tags[j][1])
                if lemma not in stop_words:
                    index = all_words.index(lemma)
                    vector[index] = vector[index] + 1
            bag_of_words_list[i] = vector

        df["bag_of_words"] = bag_of_words_list

        return df
