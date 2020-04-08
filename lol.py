



# string = gpt2.generate(sess, length=850, return_as_list=True)[0]
# subreddit = reddit.subreddit('BotsParadise')
# post = string.split('.')
# lista = post.pop()
# post = list(dict.fromkeys(post))
# text = '.'.join(post)
# text1 = text + '.'
# subreddit.submit(title= 'I have written a bot who autocreates post based on the stories subreddit', selftext=text1)





import gpt_2_simple as gpt2
import time
import random
import tarfile
import requests
import os
from datetime import datetime, timedelta
import praw
import pandas as pd

reddit = praw.Reddit(client_id='RNwsyJXptJ1qZg', 
                     client_secret='dElzzt5VKRxqePiY689MmdSYc2A', 
                     user_agent='author_bot', 
                     username='Author_bot', 
                     password='qwerty1234')

filepath="checkpoint_run1.tar"
googefileid= "1uO-U5_P5dQU8XXFlfbn14JBa3jukwbe-"

#https://drive.google.com/open?id=1uO-U5_P5dQU8XXFlfbn14JBa3jukwbe-



def extract():
    """Copies the checkpoint folder from a mounted Google Drive."""
    with tarfile.open(filepath, 'r') as tar:
        tar.extractall()
    os.remove(filepath)
    print("File",filepath, "Removed!")





def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)


download_file_from_google_drive(googefileid,filepath)
extract()
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)


def createpost():
    string = gpt2.generate(sess, length=500, return_as_list=True)[0]   
    post = string.split('.')
    lista = post.pop()
    post = list(dict.fromkeys(post))
    text = '.'.join(post)
    redditpost = text + '.'
    return redditpost

def post_tweet(redditpost, now):
    try:
        subreddit = reddit.subreddit('BotsParadise')
        redditpost = subreddit.submit(title= 'I have written a bot who autocreates post based on the stories subreddit', selftext=redditpost)
    except:
        print('Post failed')

while True: 
    redditpost = createpost()  
    now = datetime.now()
    post_tweet(redditpost, now)
    sleeptime= random.randint(60000,75000)
    now_plus = now + timedelta(seconds=sleeptime)
    print("Next tweet will be in ",str(timedelta(seconds=sleeptime)), " at " ,now_plus )
    time.sleep(sleeptime)