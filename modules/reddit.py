import praw
from modules.printers import progress_bar

reddit = praw.Reddit(
    client_id="0l1Xch2xeRe7Bw",
    client_secret="NyehBhWxZQvdRj09tIPGgOh1KZ8",
    user_agent="astrobutera-agent"
)
# print(reddit.read_only)


def get_subreddits(subreddits, number_of_submissions):
    i = 0
    progress_bar(i, number_of_submissions*len(subreddits), prefix='Getting comments:', suffix='Complete', length=50)
    data = []
    for name in subreddits:
        subreddit = reddit.subreddit(name)
        subreddit.submissions = []
        for submission in subreddit.hot(limit=number_of_submissions):
            submission.comments.list()
            # todo: don't add submissoins with 0 comments
            submission.comments.replace_more(limit=0)
            progress_bar(i+1, number_of_submissions*len(subreddits), prefix='Getting comments:', suffix='Complete', length=50)
            i = i+1
            subreddit.submissions.append(submission)
        data.append(subreddit)
    return data
