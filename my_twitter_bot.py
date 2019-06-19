import tweepy

print("this is my twitter bot")

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

#mention3 id = 1140455381732216832
last_seen_id = open_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
for mention in reversed(mentions):
    #save_last_seen_id(mention.id, FILE_NAME)
    if ("#helloworld" in mention.full_text.lower()):
        print("Responding to: ")
        print(str(mention.id) + " - " + mention.full_text)
        api.update_status('@'+ mention.user.screen_name + ' #HelloWorld test', mention.id)
