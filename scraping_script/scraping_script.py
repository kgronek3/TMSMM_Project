import praw
import os

os.chdir("/home/oic/Projects/TMSMM_Project/scraping_script")

from credentials import * 

reddit = praw.Reddit(client_id = my_client_id,
                     client_secret = my_secret,
                     user_agent = my_user_agent,
                     password = my_password,
                     username = my_username)

# /r/AskMen top posts of all time
subreddit = reddit.subreddit('AskMen')

AskMen_tp = reddit.subreddit('AskMen').top(limit = 50,
                                           time_filter = 'all')

for post in AskMen_tp:
    print(post.title)

for post in AskMen_tp:
    print(post.comments)


# submission = reddit.submission("3g1jfi")
# 
# submission
# 
# for top_level_comment in submission.comments:
#     print(top_level_comment.body)

subreddit = reddit.subreddit('askmen')
#hot_python = subreddit.hot(limit = 3)
hot_python = subreddit.top(limit = 2,
                           time_filter = 'all')
for submission in hot_python:
    submission.comments.replace_more(limit = 0)
    if not submission.stickied:
        print('Title: {}, up: {}, down: {}, Have we visited {}'.format(submission.title,
                                                                       submission.ups,
                                                                       submission.downs,
                                                                       submission.visited))
        comments = submission.comments
        for comment in comments:
            print(20 * '-')
            print(comment.author, ' : ', comment.body)









