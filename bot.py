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
        user_agent=config("user_agent"),
    )
    print("logged into reddit successfully")
    return reddit


def extract(reddit):
    with open("subreddits", "r+") as subs:
        substrs = subs.readline().strip()
    try:
        links_file = open(f"./img/posts", "w")
        print(substrs)
        subreddit = reddit.subreddit(substrs)
        for submission in subreddit.hot(limit=25):
            img_url = submission.url
            image_ext = str(img_url).split("/")[-1].split(".")[-1]
            title = submission.title
            links_file.write(f'"{title}"\t{img_url}\n')
    except Exception as err:
        print(err)


def post(reddit):
    with open("subreddits", "r+") as subs:
        subs.readline()
        substrs = subs.readline()
        print(substrs)
    try:
        links_file = open(f"./img/posts", "r+")
        subreddit=reddit.subreddit(substrs)
        for line in links_file.readlines():
            data = line.split("\t")
            title = data[0].strip('"')
            url = data[1]
            print(f"posting {title}")
            subreddit.submit(title=title,url=url)
            print(f"posted {title}")
    except Exception as err:
        print(err)