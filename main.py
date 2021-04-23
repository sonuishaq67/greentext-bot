import praw
import time
import bot
from decouple import UndefinedValueError

reddit = bot.auth()
try:
    bot.extract(reddit)
    inp = input("Do you want to post now?")
    if inp:
        bot.post(reddit)
except UndefinedValueError as err:
    print("Please create a .env file using the Readme.md")
