from modules.bag_of_words import BagOfWords
from modules.bigram_of_words import BigramOfWords
import matplotlib.pyplot as plt
from modules.tfidf_custom import TfIdfCustom
from modules.tfidf import TfIdf
from modules.word_stats import WordStats
from modules.similarity import Similarity
from models.knnreg import KnnReg
from modules.data import fetch_fresh, load_pickle, save_pickle
from modules.stats import score_distribution_plot, words_count_plot, tfidf_custom_score_plot, topic_similarity_score_plot
# from scipy.stats import binned_statistic
import sys
import argparse
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
parser.add_argument("--fetch-fresh", dest="fetch_fresh", action="store_true", default=False, help="Use to fetch new comments")
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





# FEATURES:

#bigram_of_words = BigramOfWords()
#df = bigram_of_words.score(df)

# bag_of_words = BagOfWords()
# df = bag_of_words.score(df)

#similarity = Similarity()
#similarity.score(df) # "topic_similarity"

#word_stats = WordStats()
#df = word_stats.score(df) # "words_count", "stop_words_count", "bad_words_count", "bad_words"

#tfidf_custom = TfIdfCustom()
#df = tfidf_custom.score(df) # "tfidf_custom_score"

# tfidf = TfIdf()
# tfidf.score(df) # "tf_idf"

df = df.drop([
    "topic_similarity", "words_count",
    "bigram_of_words", "tfidf_score",
    "stop_words_count", "bad_words_count", "bad_words",
    "reichenbach_tense", "emoticons", "aspectual_class", "common_word", "letter_count", "tfidf_custom_score", "length", "sentences"
], axis="columns")
print(df)



# ANALYSIS:

# score_distribution_plot(df)
# words_count_plot(df)
# tfidf_custom_score_plot(df)
# topic_similarity_score_plot(df)
# plt.show()
