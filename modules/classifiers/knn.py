import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


class Knn:

    # def __init__(self, df, split, feature_list=[], n_neighbors=3):
    #
    #     le = preprocessing.LabelEncoder()
    #     label = le.fit_transform(training_data["label"])
    #
    #     # TODO: same with trainig set as test set
    #     # train
    #     encoded = []
    #     for feature in feature_list:
    #         # TODO: order might be important?
    #         transform = le.fit_transform(training_data[feature])
    #         encoded.append(transform)
    #     features = list(zip(*encoded))
    #     model = KNeighborsClassifier(n_neighbors=n_neighbors)
    #     predicted = model.predict(label)
    #     return predicted
    #
    # def _split_training_test(self, df, split):
    #     training = df[:split]
    #     test = df[split:]
    #     return training, test

    def __init__(self, df, split, feature_list=[], n_neighbors_max=26):

        y = df.pop('score')
        X = df[feature_list]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split, random_state=1)

        k_range = range(1, n_neighbors_max)
        # scores = {}
        scores_list = []

        for k in k_range:
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(X_train, y_train)

            y_pred = knn.predict(X_test)

            score = metrics.accuracy_score(y_test, y_pred)
            # scores[k] = score
            scores_list.append(score)

        plt.plot(k_range, scores_list)
        plt.xlabel("Value of K for KNN")
        plt.ylabel("Testing accuracy")
        plt.show()
        # pd.DataFrame({"k_range": k_range, "score": scores_list})
        # print(pd)
        # sns.lineplot(x="k_range", y="score", data=pd)
        # plt.show()
