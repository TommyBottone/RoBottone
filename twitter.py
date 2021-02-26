
import os
import tweepy

def authenticate_twitter():
  consumer_key = os.getenv('CONSUMER_KEY')
  consumer_secret = os.getenv('CONSUMER_SECRET')

  access_token = os.getenv('ACCESS_TOKEN')
  access_secret_token = os.getenv("ACCESS_TOKEN_SECRET")

  callback_uri = 'oob'
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
  auth.set_access_token(access_token, access_secret_token)
  api = tweepy.API(auth)
  return api
