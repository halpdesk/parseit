from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import *
from pprint import pprint
from functools import cached_property
import math

# much help from https://towardsdatascience.com/text-summarization-using-tf-idf-e64a0644ace3


class TfIdfCustom:

    def __init__(self):
        pass

    # def __init__(self, document: list):
    #     self.document = document

    # @cached_property
    # def document(self) -> list:
    #     return self.document

    # @cached_property
    # def number_of_messages(self) -> int:
    #     return len(self.document)

    def _create_frequency_matrix(self, messages):
        """ Uses stemmer for english """
        frequency_matrix = {}
        stop_words = set(stopwords.words("english"))
        ps = PorterStemmer()

        for i in range(len(messages)):
            msg = messages[i]
            freq_table = {}
            words = word_tokenize(msg)
            for word in words:
                word = word.lower()
                word = ps.stem(word)
                if word in stop_words:
                    continue

                if word in freq_table:
                    freq_table[word] += 1
                else:
                    freq_table[word] = 1

            frequency_matrix[i] = freq_table

        return frequency_matrix

    def _create_tf_matrix(self, frequency_matrix):
        """ Calculate tf for each message """
        tf_matrix = {}

        for msg, f_table in frequency_matrix.items():
            tf_table = {}

            count_words_in_sentence = len(f_table)
            for word, count in f_table.items():
                tf_table[word] = count / count_words_in_sentence

            tf_matrix[msg] = tf_table

        return tf_matrix

    def _create_documents_per_words(self, frequency_matrix):
        word_per_doc_table = {}

        for sent, f_table in frequency_matrix.items():
            for word, count in f_table.items():
                if word in word_per_doc_table:
                    word_per_doc_table[word] += 1
                else:
                    word_per_doc_table[word] = 1

        return word_per_doc_table

    def _create_idf_matrix(self, frequency_matrix, count_doc_per_words, total_documents):
        idf_matrix = {}

        for sent, f_table in frequency_matrix.items():
            idf_table = {}
            for word in f_table.keys():
                idf_table[word] = math.log10(total_documents / float(count_doc_per_words[word]))
            idf_matrix[sent] = idf_table

        return idf_matrix

    def _create_tf_idf_matrix(self, tf_matrix, idf_matrix):
        tf_idf_matrix = {}

        for (sent1, f_table1), (sent2, f_table2) in zip(tf_matrix.items(), idf_matrix.items()):
            tf_idf_table = {}
            for (word1, value1), (word2, value2) in zip(f_table1.items(),
                                                        f_table2.items()):  # here, keys are the same in both the table
                tf_idf_table[word1] = float(value1 * value2)
            tf_idf_matrix[sent1] = tf_idf_table

        return tf_idf_matrix

    def _score_messages(self, tf_idf_matrix) -> dict:
        """
        score a message by its word's TF
        Basic algorithm: adding the TF frequency of every non-stop word in a sentence divided by total no of words in a sentence.
        :rtype: dict
        """

        message_score = {}

        for sent, f_table in tf_idf_matrix.items():
            total_score_per_message = 0

            count_words_in_message = len(f_table)
            for word, score in f_table.items():
                total_score_per_message += score

            message_score[sent] = total_score_per_message / count_words_in_message

        return message_score

    def _find_average_score(self, message_value) -> int:
        """
        Find the average score from the sentence value dictionary
        :rtype: int
        """
        sum_values = 0
        for entry in message_value:
            sum_values += message_value[entry]

        # Average value of a sentence from original summary_text
        average = (sum_values / len(message_value))

        return average

    def _generate_summary(self, messages, message_value, threshold):
        message_count = 0
        summary = ''

        for i in range(len(messages)):
            message = messages[i]
            if i in message_value and message_value[i] >= (threshold):
                summary += " " + message
                message_count += 1

        return summary

    def measure(self, document):
        # sentences = sent_tokenize(comment)
        messages = [item["body"] for item in document]
        total_documents = len(document)
        frequenzy_matrix = self._create_frequency_matrix(messages)
        tf_matrix = self._create_tf_matrix(frequenzy_matrix)
        count_doc_per_words = self._create_documents_per_words(frequenzy_matrix)
        idf_matrix = self._create_idf_matrix(frequenzy_matrix, count_doc_per_words, total_documents)
        tf_idf_matrix = self._create_tf_idf_matrix(tf_matrix, idf_matrix)
        message_scores = self._score_messages(tf_idf_matrix)
        threshold = self._find_average_score(message_scores)
        summary = self._generate_summary(messages, message_scores, 1.3 * threshold)

        for i in range(len(document)):
            document[i]["features"]["tfidf_score"] = message_scores[i]
            document[i]["features"]["tf_matrix"] = tf_matrix[i]
            document[i]["features"]["idf_matrix"] = idf_matrix[i]
        return document
        # pprint(summary)

        # return tf_matrix
        # total_documents = len(sentences)
