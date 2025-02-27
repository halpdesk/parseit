from parseit.data import fetch_fresh, load_pickle, save_pickle
from parseit.printers import print_subreddits_overview
import sys
import argparse

description="""
This programs needs data from live reddit or stored pickle. Therefore, one of
the command-line options --fetch-fresh or --load-pickle must be provided.
If --fetch-fresh is supplied it would be good to --save-pickle as well.
"""

epilog="""
Written in oct 2020 for a private project in linguistics at Göteborg Universitet.
By Daniel Leppänen.
"""

# Example commands:
# python main.py --fetch-fresh --save-pickle 10-nov.p --subreddits askreddit science --submissions 4
# python main.py --fetch-fresh --load-pickle 10-nov.p

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

arg_fetch_fresh = arguments.get("fetch_fresh")
arg_load_pickle = arguments.get("load_pickle")
arg_save_pickle = arguments.get("save_pickle")
arg_number_of_submissions = arguments.get("submissions")
arg_subreddits = arguments.get("subreddits")

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
if arg_save_pickle or arg_fetch_fresh:
    save_pickle(df, arg_save_pickle or "comments.p")
    sys.exit("Pickle saved.")


print(df)
