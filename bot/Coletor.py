# -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler

#variaveis
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)


#dilma or impeachment or "michel temer" or eduardo cunha or golpe or golpista or pt or globo or coxinha or mortadela or psdb or pmdb or golpista or corrputo or lava jato

for tw in tweepy.Cursor(api.search, q='impeachment or "michel temer"',result_type='recent', count=500).items():
    print(u"{0}",tw.text.encode('utf-8'))