from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from functools import lru_cache
import re
import os

def lemmatize(word, tag):
    l = WordNetLemmatizer()
    wordnet_tag = tag[0].lower()
    wordnet_tag = wordnet_tag if wordnet_tag in ["a", "s", "r", "n", "v"] else None # (another guide shows ['a', 'r', 'n', 'v'])
    if not wordnet_tag:
        lemma = l.lemmatize(word.lower())
    else:
        lemma = l.lemmatize(word.lower(), wordnet_tag)
    return str(lemma).lower()


def tokenize(document, method="re", by="\W+"):
    if method == "nltk":
        words = word_tokenize(document) if by == "word" else sent_tokenize(document)
    else:
        words = re.split("\W+", document)
    return pos_tag(words)


@lru_cache
def stopwords():
    return set(stopwords.words("english"))


@lru_cache
def badwords():
    root_path = f"{os.path.dirname(os.path.realpath(__file__))}/.."
    filename = f"{root_path}/datasets/bad-words.csv"
    bad_words = []
    with open(filename) as f:
        for word in f:
            bad_words.append(word[:-1])
    # don't return the last empty line
    result = bad_words[:-1]
    return result


# Interface lemma tokenizer from nltk with sklearn
class LemmaTokenizer:
    ignore_tokens = [',', '.', ';', ':', '"', '``', "''", '`', '[removed]', '>', '*', '_']
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc) if t not in self.ignore_tokens]
