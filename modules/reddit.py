import praw
from modules.printers import progress_bar

reddit = praw.Reddit(
    client_id="0l1Xch2xeRe7Bw",
    client_secret="NyehBhWxZQvdRj09tIPGgOh1KZ8",
    user_agent="astrobutera-agent"
)
# print(reddit.read_only)


def get_subreddits(subreddits, number_of_submissions):
    print(f"Fetching comments from {len(subreddits)} subreddits, {number_of_submissions} submissions from each...")
    data = []
    for name in subreddits:
        comment_count = 0
        i = 0
        progress_bar(i, number_of_submissions, prefix=f"{str(name).rjust(24, ' ')}:", suffix=f"Complete ({comment_count} comments in {i} submissions)", length=100)
        subreddit = reddit.subreddit(name)
        subreddit.submissions = []
        submissions = subreddit.top("month")
        for submission in submissions:
            if i > number_of_submissions:
                continue
            submission.comments.list()
            submission.comments.replace_more(limit=0)
            comment_count = comment_count + len(submission.comments)
            subreddit.submissions.append(submission)
            progress_bar(i, number_of_submissions, prefix=f"{str(name).rjust(24, ' ')}:", suffix=f"Complete ({comment_count} comments in {i} submissions)", length=100)
            i = i+1
        data.append(subreddit)
        print("")
    return data
