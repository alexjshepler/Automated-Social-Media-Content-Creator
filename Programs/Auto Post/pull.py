import tweepy
import time
import json

jsonData = open("Programs/Auto Post/config.json")

data = json.load(jsonData)

consumer_key = data['twitter']['consumer_key']
consumer_secret = data['twitter']['consumer_secret']
access_key = data['twitter']['access_key']
access_secret = data['twitter']['access_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="Epoch_Industry")

tweets_cvs = [tweet.text for tweet in tweets]
for i in tweets_cvs:
    print(i)