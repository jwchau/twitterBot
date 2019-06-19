import tweepy

print("this is my twitter bot")

CONSUMER_KEY ='mpaaboVnOVC6gGpthcDOVCu8x'
CONSUMER_SECRET = 'z8YZFXsC7yAWk4eeiHmqi2IWwniryhFEHYgDKlIsP6J47oBs8n'
ACCESS_KEY = '1140413739805450240-diBMg7EAagX47tGLbpfOo7HbTjbNCE'
ACCESS_SECRET = 'G7tLkwzZYWJnpTmcrShFZwe2nRafTGvMk330EoNYseS5c'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print("finished initialization of api")
