import matplotlib.pyplot as plt
import seaborn as sns

def score_distribution_plot(df):
    sns.displot(df, x="label", binwidth=1000)

def words_count_plot(df):
    g = sns.jointplot(x="words_count", y="label", data=df[["words_count", "label"]],
        kind="reg", truncate=False,
        # xlim=(0, 60), ylim=(0, 12),
        color="m", height=7)

def tfidf_custom_score_plot(df):
    g = sns.jointplot(x="tfidf_custom_score", y="label", data=df[["tfidf_custom_score", "label"]],
        kind="reg", truncate=False,
        # xlim=(0, 60), ylim=(0, 12),
        color="m", height=7)
