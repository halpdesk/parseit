from nltk.tokenize import sent_tokenize
from nltk.stem.porter import *

# much help from https://towardsdatascience.com/text-summarization-using-tf-idf-e64a0644ace3

def _create_frequency_matrix(sentences):
    frequency_matrix = {}
    stopWords = set(stopwords.words("english"))
    ps = PorterStemmer()

    for sent in sentences:
        freq_table = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            word = ps.stem(word)
            if word in stopWords:
                continue

            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1

        frequency_matrix[sent[:15]] = freq_table

    return frequency_matrix

def tf(comment):
    sentences = sent_tokenize(comment)
    total_documents = len(sentences)
    print(sentences)
    # total_documents = len(sentences)
