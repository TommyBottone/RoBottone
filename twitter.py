
import os
import tweepy

def authenticate_twitter():
  consumer_key = os.getenv('CONSUMER_KEY')
  consumer_secret = os.getenv('CONSUMER_SECRET')
  callback_uri = 'oob'
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
  api = tweepy.API(auth)
  return api
