import praw
import pandas as pd
import datetime as dt #only if you want to analyze the date created feature
import json

# I assigned reddit as the variable name, you can call it whatever you want to.
reddit = praw.Reddit(client_id='RNwsyJXptJ1qZg', 
                     client_secret='dElzzt5VKRxqePiY689MmdSYc2A', 
                     user_agent='author_bot', 
                     username='Author_bot', 
                     password='qwerty1234')
# IF YOU HAVE ANY SPACES BETWEEN THE CHARACTERS AND THE QUOTES, YOU WILL RECEIVE AN ERROR.
# GOOD: '14_CHARS_IDENTIFIER'
# BAD: ' 14_CHARS_IDENTIFIER '

title = []
body = []


subreddit1 = reddit.subreddit('stories')
tifu_subreddit = subreddit1.top(limit=1000)

for submission in tifu_subreddit:
    title.append(submission.title)
    body.append(submission.selftext)
 
file = open("data.txt", "w")


for i in range(len(title)):
    try:
        titletext = title[i].replace("\n", "")
        bodytext = body[i].replace("\n", "")
        file.write(bodytext + '\n'*4 + '*'*30 + '\n'*4) 
    except:
        pass   
    #print(titletext + " " + bodytext)   




