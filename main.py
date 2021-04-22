import praw
import time
import bot
from decouple import UndefinedValueError

reddit = bot.auth()
while reddit:
    try:
        bot.extract(reddit)
    except UndefinedValueError as err:
        print("Please create a .env file using the Readme.md")
