import gpt_2_simple as gpt2
import time
import random
import tarfile
import requests
import os
from datetime import datetime, timedelta
import praw

reddit = praw.Reddit(client_id = "vvT6zwSKNTzn7g", 
                     client_secret = "lLSIepmEv64ezqLpncuaSSCk-c8",     
                     user_agent = "unpopular_bot", 
                     username = "abblinkas", 
                     password = "qwerty123")

filepath="checkpoint_run1.tar"
googefileid= "1ZC3fGu4EOMcOmmKK3ug6dJ3gBWvRMDXn"

def extract():
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
                if chunk:
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

def check_if_post_exist(string):
    with open('data.txt') as f:
        datafile = f.readlines()
    for line in datafile:
        if string in line:
            return True
    return False

def generate_post():
    print("Generating posts...")
    raw_text = gpt2.generate(session, return_as_list=True)[0]
    posts = raw_text.split("\n")
    possible_post = []
    for post in posts:
        if "*****" in post and not check_if_post_exist(post):
            possible_post.append(post.split("*****"))
    if len(possible_post) == 0:
        print("No possible posts found. Trying again...")
        return generate_text()
    else:
        post = min(possible_post, key=len)
        return_title = post[0].replace("\\", "")
        return_body = post[1].replace("\\", "")
        best_post = {"title": return_title, "body": return_body}
        print("Generation done")
        return best_post

def post(title, body, now):
    try:
        reddit.subreddit("BotsParadise").submit(title, selftext=body)
        print('Successfully posted at', now)
    except:
        print('Post failed')

while True:    
    now = datetime.now()
    best_post = generate_post()
    post(best_post["title"], best_post["body"], now)
    sleeptime = 10800
    now_plus = now + timedelta(seconds=sleeptime)
    print("Next tweet will be in ",str(timedelta(seconds=sleeptime)), " at " , now_plus )
    time.sleep(sleeptime)