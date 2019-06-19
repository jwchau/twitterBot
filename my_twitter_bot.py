import tweepy
import time
import random

print("twitter_bot start")

CONSUMER_KEY ='mpaaboVnOVC6gGpthcDOVCu8x'
CONSUMER_SECRET = 'z8YZFXsC7yAWk4eeiHmqi2IWwniryhFEHYgDKlIsP6J47oBs8n'
ACCESS_KEY = '1140413739805450240-diBMg7EAagX47tGLbpfOo7HbTjbNCE'
ACCESS_SECRET = 'G7tLkwzZYWJnpTmcrShFZwe2nRafTGvMk330EoNYseS5c'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

""" for testing
mentions = api.mentions_timeline()
#readable = mentions[0].__dict__.keys())
print("Printing all mentions")
"""

FILE_NAME = 'last_seen_id.txt'
COMPLIMENTS_FILE = 'compliments.txt'

def open_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def save_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def open_compliments(file_name):
    compliments = [line.rstrip('\n') for line in open(file_name)]
    return compliments

def pick_compliment():
    return random.choice(compliments)

def reply_to_mentions():
    #first chronological mention id = 1140455381732216832
    print('search and reply')
    last_seen_id = open_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        save_last_seen_id(mention.id, FILE_NAME)
        if ("#compliment" in mention.full_text.lower()):
            print("  Responding to: ")
            print("    " + str(mention.id) + " - " + mention.full_text)
            api.update_status('@'+ mention.user.screen_name + " " + pick_compliment(), mention.id)

compliments = open_compliments(COMPLIMENTS_FILE)
while True:
    reply_to_mentions()
    time.sleep(15)
