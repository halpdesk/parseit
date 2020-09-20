import time
from colored import fg, bg, attr
import pendulum
import string


def safe(s: str):
    safechars = string.ascii_lowercase + string.ascii_uppercase + string.digits + ".- "
    s.replace("%", "PERCENT")
    return ''.join([c for c in s if c in safechars])


def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def print_subreddit(subreddit):
    print(
        f"\n%s%sSubreddit:%s%s {subreddit.display_name} - {safe(subreddit.title)}%s"
        % (fg(2), attr(1), attr(0), fg(15), attr(0))
    )
    # print(subreddit.description)


def print_submission(submission):
    print(
        f"  %s{str(submission.score).rjust(5, ' ')} points %s- %s{safe(submission.title)[0:140]}%s -%s ({len(submission.comments)} comments)%s"
        % (fg(4), attr(0), fg(30), attr(0), fg(1), attr(0))
    )
    # print(submission.id, submission.url)


def print_comment(comment):
    print(
        f"     %s{str(comment.score).rjust(5, ' ')} points %s[{str(comment.relative_score)[0:4]}]%s- %s{safe(f'{comment.author}:').rjust(20, ' ')} %s- %s{safe(comment.body)[0:140]}%s"
        % (fg(3), fg(54), attr(0), fg(2), attr(0), fg(7), attr(0))
    )


def print_comment_body(comment):
    author = f"{comment.author}{'(-op-)' if comment.is_submitter else ''}"
    timestamp = pendulum.from_timestamp(comment.created_utc).to_datetime_string()
    title = f"--{f'[{author}]'.ljust(30, '-')}(points: {comment.score})--{'[E]' if comment.edited else '---'}----{timestamp}--"
    print(f"%s{title}%s" % (fg(3), attr(0)))
    print(comment.body)
    print("\n")


def print_subreddits_overview(subreddits, only_outlier_comments=True):
    shown_comments = 0
    for subreddit in subreddits:
        print_subreddit(subreddit)
        for submission in subreddit.submissions:
            # time.sleep(0.01)
            print_submission(submission)
            total_comment_score = sum([comment.score for comment in submission.comments])
            number_of_comments = len(submission.comments)
            avarege_comment_score = total_comment_score/(number_of_comments if number_of_comments != 0 else 1)
            for comment in submission.comments:
                # time.sleep(0.001)
                # comment.relative_score = comment.score/((total_comment_score - comment.score) if comment.score != total_comment_score else 1)
                comment.relative_score = comment.score/avarege_comment_score
                if comment.author != None and (comment.relative_score > 0.7 or comment.score < 0):
                    print_comment(comment)
                    shown_comments = shown_comments + 1

    tot_comments = sum([sum([len(submission.comments) for submission in subreddit.submissions]) for subreddit in subreddits])
    print(f"\nShown comments: %s{shown_comments} (of {tot_comments} total comments)%s" % (fg(1), attr(0)))


def print_comments(subreddits):
    print(f"\nComments in {subreddits[0].submissions[0].title}")
    for comment in subreddits[0].submissions[0].comments:
        print_comment(comment)
