
import pickle
from pprint import pprint

from modules.printers import print_comment, print_subreddits_overview, print_comments, progress_bar
from modules.reddit import get_subreddits
from modules.tfidf_custom import TfIdfCustom
from modules.tfidf import TfIdf
from modules.word_stats import WordStats
from modules.classifiers.knn import Knn
from scipy.stats import binned_statistic
import sys
import argparse
import pandas as pd
import numpy as np

## Command line usage and arg parsing

description="""
This programs needs data from live reddit or stored pickle. Therefore, one of
the command-line options --fetch-fresh or --load-pickle must be provided.
If --fetch-fresh is supplied it would be good to --save-pickle as well.
"""

epilog="""
Written in october 2020 for a private project in linguistics at Göteborg Universitet.
By Daniel Leppänen.
"""

default_subreddits = [
    "askreddit",
    "science",
    "worldnews",
    "todayilearned",
    "news",
    "askscience",
    "explainlikeimfive",
    # "dataisbeautiful",
]

parser = argparse.ArgumentParser(prog="python3.8 main.py", description=description, epilog=epilog)
parser.add_argument("--fetch-fresh", dest="use_reddit", action="store_true", default=False, help="Use to fetch new comments")
parser.add_argument("--save-pickle", dest="save_pickle", action="store_true", default=False, help="Use to save comment data to a pickle")
parser.add_argument("--load-pickle", dest="load_pickle", action="store_true", default=False, help="Use to load comment data to a pickle")
parser.add_argument("--subreddits",  dest="subreddits", nargs="+", default=default_subreddits, help="Which subreddits to parse for commments")
parser.add_argument("--submissions", dest="submissions", nargs="?", default=100, type=int, help="How many submissions to fetch for each subreddit")
arguments = vars(parser.parse_args())


fetch_fresh = arguments.get("use_reddit", False)
load_picle = arguments.get("load_pickle", False)
save_pickle = arguments.get("save_pickle", False)
number_of_submissions = arguments.get("submissions", 100)
subreddits = arguments.get("subreddits", default_subreddits)

data = []

# data = np.random.rand(1000)
# bins = binned_statistic(data, data, bins=3, range=[0,10])
# print(bins)
# print(bins[0])
# exit("Exited.")


if load_picle:
    data = pickle.load(open("comments.p", "rb"))
    print("Pickle loaded.")

if fetch_fresh:
    data = get_subreddits(subreddits, number_of_submissions)

if save_pickle:
    pickle.dump(data, open("comments.p", "wb"))
    print_subreddits_overview(data, only_outlier_comments=False)
    sys.exit("Pickle saved.")

if len(data) == 0:
    sys.exit("No data loaded.")


# print_subreddits_overview(data, only_outlier_comments=False)
# exit("Exited.")


# re-order do message-document format
# document = several (messagag =
#   several (sentence =
#       several (word =
#           several character)))
document = []
for subreddit in data:
    for submission in subreddit.submissions:
        for comment in submission.comments:
            document.append({
                "body": comment.body,
                "score": comment.score,
                "subreddit": subreddit.display_name,
                "submission": submission.title,
                "features": {
                    "tf_matrix": [],
                    "idf_matrix": [],
                    "tfidf_score": 0,
                    "tfidf_custom_score": 0,
                    "length": 0,
                    "sentences": 0,
                    "common_word": 0,
                    "words_count": 0,
                    "stop_words_count": 0,
                    "bad_words_count": 0,
                    "bad_words": "",
                    "letter_count": 0,
                    # "swear_words": False, --- called bad_words
                    "emoticons": False,
                    "aspectual_class": 0,
                    "reichenbach_tense": 0,
                    "topic_similarity": 0,
                }
            })

scores = [item["score"] for item in document]
# DON'T bin labels on regression
# print(scores)
# bins = binned_statistic(score, score, bins=2, range=[0,1])
# bins = binned_statistic(scores, scores, range=[-10, 0,100,1000])


df = pd.DataFrame(data={
    "body": [item["body"] for item in document],
    "tfidf_custom_score": [item["features"]["tfidf_custom_score"] for item in document],
    "words_count": [item["features"]["words_count"] for item in document],
    "stop_words_count": [item["features"]["stop_words_count"] for item in document],
    "bad_words_count": [item["features"]["bad_words_count"] for item in document],
    "bad_words": [item["features"]["bad_words"] for item in document],
    "score": scores,
})

# TODO: add another pickle here so we do not need to transform every time

word_stats = WordStats()
df = word_stats.measure(df)

tfidf_custom = TfIdfCustom()
df = tfidf_custom.measure(df)

print(df)

# exit("Exited.")

feature_list_to_classify = [
    "words_count",
    "stop_words_count",
    "bad_words_count",
    "tfidf_custom_score",
]

knn = Knn(df=df, split=0.9, feature_list=feature_list_to_classify, n_neighbors_max=26)
print(knn)


# Mark with features

# print(data[1].submissions[2].comments[4].body)



# # tfidf = TfIdf()
# # tfidf.measure(document)
# pprint(document)
