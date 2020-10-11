
from modules.tfidf_custom import TfIdfCustom
from modules.tfidf import TfIdf
from modules.word_stats import WordStats
from modules.classifiers.knn import Knn
from modules.data import fetch_fresh, load_pickle, save_pickle, create_df_from_reddit_data
# from scipy.stats import binned_statistic
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
parser.add_argument("--save-pickle", dest="save_pickle", nargs="?", type=str, help="Use to save comment data to a pickle")
parser.add_argument("--load-pickle", dest="load_pickle", nargs="?", type=str, help="Use to load comment data to a pickle")
parser.add_argument("--subreddits",  dest="subreddits", nargs="+", default=default_subreddits, help="Which subreddits to parse for commments")
parser.add_argument("--submissions", dest="submissions", nargs="?", default=100, type=int, help="How many submissions to fetch for each subreddit")
arguments = vars(parser.parse_args())

arg_fetch_fresh = arguments.get("fetch_fresh", False)
arg_load_pickle = arguments.get("load_pickle", "comments.p")
arg_save_pickle = arguments.get("save_pickle", "comments.p")
arg_number_of_submissions = arguments.get("submissions", 100)
arg_subreddits = arguments.get("subreddits", default_subreddits)

if arg_load_pickle:
    df = load_pickle(arg_load_pickle)
    # df = create_df_from_reddit_data(data)
    sys.exit("Pickle loaded.")
    print("Pickle loaded.")

elif arg_fetch_fresh:
    df = fetch_fresh(arg_subreddits, arg_number_of_submissions)
    print("Data fetched from subreddits.")

try:
    df = df
except NameError:
    sys.exit("No data loaded.")

if arg_save_pickle:
    save_pickle(df, arg_save_pickle)
    sys.exit("Pickle saved.")


# ANALYSIS:

# scores = [item["score"] for item in document]
# DON'T bin labels on regression
# print(scores)
# bins = binned_statistic(score, score, bins=2, range=[0,1])
# bins = binned_statistic(scores, scores, range=[-10, 0,100,1000])


# FEATURES:

word_stats = WordStats()
df = word_stats.measure(df)

tfidf_custom = TfIdfCustom()
df = tfidf_custom.measure(df)

# tfidf = TfIdf()
# tfidf.measure(document)

print(df[[
    "tfidf_custom_score",
    "words_count"
    "stop_words_count"
    "bad_words_count"
    "bad_words"
]])

exit("Exited.")

feature_list_to_classify = [
    "words_count",
    "stop_words_count",
    "bad_words_count",
    "tfidf_custom_score",
]

knn = Knn(df=df, split=0.9, feature_list=feature_list_to_classify, n_neighbors_max=26)
print(knn)
