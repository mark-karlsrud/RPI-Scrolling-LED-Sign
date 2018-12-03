# coding=utf-8
import tweepy
import os
import re
import logging

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []

def get_a_tweet():
    global tweets, api
    if not tweets:
        print('\nrefilling tweets\n')
        tweets = api.home_timeline()
    tweet = tweets.pop()
    return '@{user}: {text}'.format(user= tweet.user.screen_name, text=re.sub('https://t.co/\w+', '', tweet.text.encode('utf-8')))
