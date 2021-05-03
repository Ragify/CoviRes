import tweepy
from tweepy import OAuthHandler
import pandas as pd
import os
import config

access_token = 'xxxxxxx'
access_token_secret = 'xxxxxxx'
consumer_key = 'xxxxxxx'
consumer_secret = 'xxxxxxx'

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token,config.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets = []

new_search = "verified Mumbai (ICU OR icu) -'not verified' -'un verified' -urgent -unverified -needed -required -need -needs -requirement since:2021-4-27"

for tweet in tweepy.Cursor(api.search, q=new_search, lang="en").items(5):

	try: 
		data = [tweet.id]
		print(f"https://twitter.com/anyuser/status/"+str(data[0]))
        

	except tweepy.TweepError as e:
		print(e.reason)
		continue

	except StopIteration:
		break
