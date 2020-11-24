from functools import lru_cache

def lemmatize(word, tag):
    from nltk.stem import WordNetLemmatizer

    l = WordNetLemmatizer()
    wordnet_tag = tag[0].lower()
    wordnet_tag = wordnet_tag if wordnet_tag in ["a", "s", "r", "n", "v"] else None # (another guide shows ['a', 'r', 'n', 'v'])
    if not wordnet_tag:
        lemma = l.lemmatize(word.lower())
    else:
        lemma = l.lemmatize(word.lower(), wordnet_tag)
    return str(lemma).lower()


def tokenize(document, method="nltk", by="word"):
    from nltk import pos_tag, word_tokenize, sent_tokenize
    import re

    if method == "nltk":
        words = word_tokenize(document) if by == "word" else sent_tokenize(document)
    else:
        words = re.split("\W+", document)

    filtered_empty = [word for word in words if re.match("\w", word)]
    return pos_tag(filtered_empty)


@lru_cache
def stopwords():
    from nltk.corpus import stopwords as stop_words
    return set(stop_words.words("english"))


@lru_cache
def badwords():
    import os
    root_path = f"/home/halpdesk/CODE/reddit-parser"
    filename = f"{root_path}/datasets/fb-bad-words.csv"
    bad_words = []
    with open(filename) as f:
        for line in f:
            for word in line.split(","):
                bad_words.append(word.lower().strip())
    return bad_words


# Interface lemma tokenizer from nltk with sklearn
# class LemmaTokenizer:
#     ignore_tokens = [',', '.', ';', ':', '"', '``', "''", '`', '[removed]', '>', '*', '_', "&", "$"]
#     def __init__(self):
#         from nltk.stem import WordNetLemmatizer
#         self.wnl = WordNetLemmatizer()
#     def __call__(self, doc):
#         from nltk import word_tokenize
#         return [self.wnl.lemmatize(t) for t in word_tokenize(doc) if t not in self.ignore_tokens]

# Interface lemma tokenizer from nltk with sklearn
class LemmaTokenizer:
    ignore_tokens = [',', '.', ';', ':', '"', '``', "''", '`', '[removed]', '>', '*', '_', "&", "$"]
    stopwords = []
    vocab = []
    def __init__(self, stopwords=[], vocabulary=[]):
        from nltk.stem import WordNetLemmatizer
        self.wnl = WordNetLemmatizer()
        self.stopwords = stopwords
        self.vocab = vocabulary
    def __call__(self, doc):
        from nltk import word_tokenize
        sig_words = []
        for token in doc:
            word = self.wnl.lemmatize(token)
            if word not in self.stopwords + self.ignore_tokens and word in self.vocab:
                sig_words.append(word)
        return sig_words
