import praw
import pickle
import pprint
import pendulum
import string
from colored import fg, bg, attr

use_pickle = True
safechars = string.ascii_lowercase + string.ascii_uppercase + string.digits + ".- "
reddit = praw.Reddit(client_id="0l1Xch2xeRe7Bw",
                     client_secret="NyehBhWxZQvdRj09tIPGgOh1KZ8",
                     user_agent="astrobutera-agent")
# print(reddit.read_only)


def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def get_comments(subreddits, number_of_submissions):
    i = 0
    progress_bar(i, number_of_submissions*len(subreddits), prefix='Getting comments:', suffix='Complete', length=50)
    data = {"subreddits": []}
    for name in subreddits:
        subreddit = reddit.subreddit(name)
        subreddit_data = {
            "title": subreddit.title,
            "display_name": subreddit.display_name,
            "submissions": []
        }
        for submission in subreddit.hot(limit=number_of_submissions):
            comments = submission.comments.list()
            subreddit_data["submissions"].append({
                "title": ''.join([c for c in submission.title if c in safechars]),
                "score": submission.score,
                "comments": comments,
                "number_of_comments": len(comments)
            })
            progress_bar(i+1, number_of_submissions*len(subreddits), prefix='Getting comments:', suffix='Complete', length=50)
            i = i+1
        data["subreddits"].append(subreddit_data)
    print("done")
    return data


def print_subreddits_overview(data):
    for subreddit in data["subreddits"]:
        print(
            f"\n%s%sSubreddit:%s%s {subreddit['display_name']} - {subreddit['title']}%s"
            % (fg(2), attr(1), attr(0), fg(15), attr(0))
        )
        # print(subreddit.description)
        for submission in subreddit["submissions"]:
            print(
                f"  %s{str(submission['score']).rjust(5, ' ')} points %s- %s{submission['title'][0:140]}%s -%s ({submission['number_of_comments']} comments)%s"
                % (fg(4), attr(0), fg(30), attr(0), fg(1), attr(0))
            )
            # print(submission.id, submission.url)

    tot_comments = sum([sum([item["number_of_comments"] for item in subreddit["submissions"]]) for subreddit in data["subreddits"]])
    print(f"\nTotal of comments: %s{tot_comments}%s" % (fg(1), attr(0)))


def print_comment(comment):
    author = f"{comment.author}{'(-op-)' if comment.is_submitter else ''}"
    timestamp = pendulum.from_timestamp(comment.created_utc).to_datetime_string()
    title = f"--{f'[{author}]'.ljust(30, '-')}(score: {comment.score})--{'[E]' if comment.edited else '---'}----{timestamp}--"
    print(f"%s{title}%s" % (fg(3), attr(0)))
    print(comment.body)
    print("\n")

if use_pickle:
    data = pickle.load(open("comments.p", "rb"))
else:
    data = get_comments([
        "Coronavirus",
        # "dataisbeautiful",
        # "explainlikeimfive",
        "science",
        "todayilearned",
        # "Awwducational",
    ], number_of_submissions=10)
    pickle.dump(data, open("comments.p", "wb"))



print_subreddits_overview(data)

print(f'\nComments in {data["subreddits"][0]["submissions"][2]["title"]}')
for comment in data["subreddits"][0]["submissions"][2]["comments"]:
    print_comment(comment)
