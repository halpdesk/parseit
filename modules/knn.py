from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


class KNN:

    def __init__(self):
        le = preprocessing.LabelEncoder()
        # features=list(zip(weather_encoded,temp_encoded))

        model = KNeighborsClassifier(n_neighbors=3)
        # model.fit(features,label)

    def add_features_from_document(self, document):
        feature_list = [
            "words_count",
            "stop_words_count",
            "bad_words_count",
            "bad_words",
            "letter_count",
            "tfidf_score",
        ]


    def split_training_test(self, document, split):
        training = document[:split]
        test = document[split:]

    def fit(self):
        pass
