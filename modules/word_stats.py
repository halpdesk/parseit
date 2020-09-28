from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from functools import lru_cache
import os

# bad words from:
# https://github.com/snguyenthanh/better_profanity/blob/master/better_profanity/profanity_wordlist.txt
# https://github.com/ani10030/bad-words-detector/blob/master/datasets/english.csv

class WordStats:

    def __init__(self):
        self.stop_words = set(stopwords.words("english"))

    @lru_cache
    def _list_bad_words(self):
        root_path = f"{os.path.dirname(os.path.realpath(__file__))}/.."
        filename = f"{root_path}/datasets/bad-words.csv"
        bad_words = []
        with open(filename) as f:
            for word in f:
                bad_words.append(word[:-1])
        # don't return the last empty line
        result = bad_words[:-1]
        return result

    def _count_words(self, messages):
        """ Uses stemmer for english """
        bad_words_corp = self._list_bad_words()
        words_count_list = [0] * len(messages)
        bad_words_count_list = [0] * len(messages)
        bad_words_list = [None] * len(messages)
        stop_words_count_list = [0] * len(messages)
        stop_words = set(stopwords.words("english"))
        ps = PorterStemmer()

        for i in range(len(messages)):
            word_count = 0
            stop_words_count = 0
            bad_words_count = 0
            bad_words = ""
            msg = messages[i]
            freq_table = {}
            words = word_tokenize(msg)
            for word in words:
                word = ps.stem(word.lower())
                if word in bad_words_corp:
                    bad_words_count = bad_words_count + 1
                    bad_words = f"{bad_words},{word}"
                if word in stop_words:
                    stop_words_count = stop_words_count + 1
                else:
                    word_count = word_count + 1

            words_count_list[i] = word_count
            stop_words_count_list[i] = stop_words_count
            bad_words_count_list[i] = bad_words_count
            bad_words_list[i] = bad_words[1:]

        return words_count_list, stop_words_count_list, bad_words_count_list, bad_words_list

    def measure(self, document):
        messages = [item["body"] for item in document]

        word_count_list, stop_words_count_list, bad_words_count_list, bad_words_list = self._count_words(messages)

        for i in range(len(document)):
            document[i]["features"]["words_count"] = word_count_list[i]
            document[i]["features"]["stop_words_count"] = stop_words_count_list[i]
            document[i]["features"]["bad_words_count"] = bad_words_count_list[i]
            document[i]["features"]["bad_words"] = bad_words_list[i]
        return document
