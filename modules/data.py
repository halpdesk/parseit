import os
import sys
from modules.reddit import get_subreddit_comments
from modules.printers import print_subreddits_overview
import pandas as pd
import pickle

def fetch_fresh(subreddits, number_of_submissions):
    reddit_data = get_subreddit_comments(subreddits, number_of_submissions)
    df = create_df_from_reddit_data(reddit_data)
    return df

def load_pickle(pickle_file_name):
    if not os.path.isfile(pickle_file_name):
        sys.exit("Pickle file not found")
    df = pickle.load(open(pickle_file_name, "rb"))
    return df

def save_pickle(data, pickle_file_name):
    pickle.dump(data, open(pickle_file_name, "wb"))
    # print_subreddits_overview(data, only_outlier_comments=False)

def create_df_from_reddit_data(reddit_data):
    document = {}
    i = 0
    for subreddit in reddit_data:
        for submission in subreddit.submissions:
            for comment in submission.comments:
                document[i] = {
                    "body": comment.body,
                    "subreddit": subreddit.display_name,
                    "submission": submission.title,
                    "label": comment.score,
                }
                i = i+1
    return pd.DataFrame.from_dict(document, "index")

# It is very slow to append to df for some reason:
# https://stackoverflow.com/questions/27929472/improve-row-append-performance-on-pandas-dataframes
# def create_df_from_data_slow_append(data):
#     df = pd.DataFrame(columns=[
#         "tf_matrix",
#         "idf_matrix",
#         "tfidf_score",
#         "tfidf_custom_score",
#         "length",
#         "sentences",
#         "common_word",
#         "words_count",
#         "stop_words_count",
#         "bad_words_count",
#         "bad_words",
#         "letter_count",
#         "emoticons",
#         "aspectual_class",
#         "reichenbach_tense",
#         "topic_similarity",
#     ])
#     for subreddit in data:
#         for submission in subreddit.submissions:
#             for comment in submission.comments:
#                 df.append({
#                     "body": comment.body,
#                     "subreddit": subreddit.display_name,
#                     "submission": submission.title,
#                     "tfidf_custom_score": 0,
#                     "words_count": 0,
#                     "stop_words_count": 0,
#                     "bad_words_count": 0,
#                     "bad_words": "",
#                     "score": comment.score,
#                 }, ignore_index=True)
#     return df
