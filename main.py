
import pickle
import pprint

from modules.printers import print_comment, print_subreddits_overview, print_comments, progress_bar
from modules.reddit import get_subreddits
from modules.tfidf import tf

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


print_subreddits_overview(data, only_outlier_comments=True)

print(data[1].submissions[2].comments[4].body)
tf = tf(data[1].submissions[2].comments[4].body)
print(tf)
# print_comments(data)
