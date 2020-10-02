from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


class Knn:

    def __init__(self, df, split, feature_list=[], n_neighbors=3):
        le = preprocessing.LabelEncoder()

        training_data, test_data = self._split_training_test(df, split)

        label=le.fit_transform(training_data["label"])

        # TODO: same with trainig set as test set
        # train
        encoded = []
        for feature in feature_list:
            # TODO: order might be important?
            transform = le.fit_transform(training_data[feature])
            encoded.append(transform)

        features = list(zip(*encoded))
        # labels = list(zip(*label))
        model = KNeighborsClassifier(n_neighbors=n_neighbors)
        model.fit(features, label)

        return self.predict(model, labels)


    def predict(self, model, labels):
        predicted = model.predict(labels)
        return predicted

    def _split_training_test(self, df, split):
        training = df[:split]
        test = df[split:]
        return training, test
