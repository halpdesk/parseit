
import pickle
import pprint

from modules.printers import print_comment, print_subreddits_overview, print_comments, progress_bar
from modules.reddit import get_subreddits
from modules.tfidf import TfIdf

# parameters

use_pickle = True
store_pickle = True
subreddits = [
    "Coronavirus",
    # "dataisbeautiful",
    # "explainlikeimfive",
    "science",
    "todayilearned",
    # "Awwducational",
]
number_of_submissions=10


if use_pickle:
    data = pickle.load(open("comments.p", "rb"))
else:
    data = get_subreddits(subreddits, number_of_submissions)
    if store_pickle:
        pickle.dump(data, open("comments.p", "wb"))

# print_subreddits_overview(data, only_outlier_comments=True)

# re-order do message-document format
# document = several (messagag =
#   several (sentence =
#       several (word =
#           several character)))
messages = []
for subreddit in data:
    for submission in subreddit.submissions:
        for comment in submission.comments:
            messages.append({
                "body": comment.body,
                "score": comment.score,
                "subreddit": subreddit.display_name,
                "submission": submission.title,
                "features": {
                    "tf": 0,
                    "idf": 0,
                    "tfidf": 0,
                    "length": 0,
                    "sentences": 0,
                    "common_word": 0,
                    "swear_words": False,
                    "emoticons": False,
                    "aspectual_class": 0,
                    "reichenbach_tense": 0,
                    "topic_similarity": 0,
                }
            })

# Mark with features

# print(data[1].submissions[2].comments[4].body)
tfidf = TfIdf()
tfidf.tf(messages)
# print_comments(data)
