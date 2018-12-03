from dotenv import load_dotenv # imports module for dotenv
load_dotenv(dotenv_path='PROPERTIES.env')
load_dotenv(dotenv_path='API_KEYS.env') # loads .env from root directory

import json
from news import news
from mta import mta
from weather import weather
from twitter import twitter
import os
import random

config_file = os.environ['CONFIG_FILE']
config = {}

def update_config(_config):
    global config
    config = _config

# Load config
with open(config_file, 'r') as f:
    update_config(json.load(f))

    #update frequency bounds
    acc = 0.0
    for k, v in config.iteritems():
        v['lower_bounds'] = acc
        v['upper_bounds'] = acc + v['frequency']
        acc = v['upper_bounds']

# for k,v in config:

feed = []

def add_to_feed():
    global config
    rand = random.random()
    for k, v in config.iteritems():
        if v['lower_bounds'] < rand and v['upper_bounds'] >= rand:
            print k
            if k == 'news':
                try:
                    if config['news']['enabled']:
                        feed.append(news.get_headline())
                        break
                except:
                    print('\nError getting news\n')
            if k == 'mta':
                try:
                    if config['mta']['enabled']:
                        feed.append(mta.get_train_times())
                        break
                except:
                    print('\nError getting mta\n')
            if k == 'weather':
                try:
                    if config['weather']['enabled']:
                        feed.append(weather.get_weather())
                        break
                except:
                    print('\nError getting weather\n')
            if k == 'twitter':
                try:
                    if config['twitter']['enabled']:
                        feed.append(twitter.get_a_tweet())
                        break
                except:
                    print('\nError getting twitter\n')

# while True:

if not feed:
    add_to_feed()
print(feed.pop())
