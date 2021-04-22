from decouple import config
import praw
import time
import requests
import random

def auth():
    reddit = praw.Reddit(
     client_id=config("client_id"),
     client_secret=config("client_secret"),
     password=config("password"),
     username=config("username"),
     user_agent=config("user_agent")
    )
    print("logged into reddit successfully")
    return reddit



def extract(reddit):
    with open('subreddits', 'r+') as subs:
        substrs = subs.read()
    try:
        print(substrs)
        subreddit = reddit.subreddit(substrs)
        for submission in subreddit.hot(limit=25):
             img_url = submission.url
             image_ext=str(img_url).split('/')[-1].split('.')[-1]
             title=submission.title
             print(image_ext)
             r = requests.get(img_url, allow_redirects=True)
             open(f'./img/{title}.{image_ext}', 'wb').write(r.content)
        exit(0)
    except Exception as err:
        print(err)
        time.sleep(20)


