from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import heapq

class BagOfWords:

    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.ps = PorterStemmer()

    def _all_words(self, messages):
        """ Uses stemmer for english """

        all_words = []
        for i in range(len(messages)):
            msg = messages[i]
            words = word_tokenize(msg)
            for word in words:
                word = self.ps.stem(word.lower())
                if word not in self.stop_words:
                    all_words.append(word)

        return list(set(all_words))

    def score(self, df):

        # most_freq = heapq.nlargest(200, wordfreq, key=wordfreq.get)
        ps = PorterStemmer()
        messages = df.get("body")
        all_words = self._all_words(messages)

        bag_of_words_list = [[]] * len(messages)
        for i in range(len(messages)):
            sentence = messages[i]
            tokens = word_tokenize(sentence)
            vector = [0] * len(all_words)
            for j in range(len(tokens)):
                word = self.ps.stem(tokens[j].lower())
                if word not in self.stop_words:
                    index = all_words.index(word)
                    vector[index] = vector[index] + 1
            bag_of_words_list[i] = vector

        df["bag_of_words"] = bag_of_words_list

        return df
