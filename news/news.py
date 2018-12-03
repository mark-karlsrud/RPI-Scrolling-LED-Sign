# coding=utf-8
import json
import os
from newsapi import NewsApiClient
import logging

api_key = os.environ['NEWS_API_KEY']
news_sources_file = os.environ['NEWS_SOURCES_FILE']

news_sources = {}

def update_config(sources) :
    global news_sources
    news_sources = sources

# Load news_sources
with open(news_sources_file, 'r') as f:
    update_config(json.load(f))

# Init
news_api = NewsApiClient(api_key=api_key)

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(category='business',
#                                           language='en',
#                                           country='us')
top_headlines = []

def get_headline():
    global top_headlines, news_api, news_sources
    if not top_headlines:
        print('\nrefilling news\n')
        top_headlines = news_api.get_top_headlines(sources=','.join([str(x) for x in {k:v for k,v in news_sources.iteritems() if v['enabled']}]),
                                                  language='en')['articles']
    article = top_headlines.pop()
    return '{source}: {title}'.format(source=article['source']['name'].encode('utf-8'), title=article['title'].encode('utf-8'))