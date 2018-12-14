# coding=utf-8
from dotenv import load_dotenv # imports module for dotenv
load_dotenv(dotenv_path='PROPERTIES.env')
load_dotenv(dotenv_path='API_KEYS.env') # loads .env from root directory

import argparse
import json
from news import news
from mta import mta
from weather import weather
from twitter import twitter
from welcome import welcome
import os
import random

from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

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
            if k == 'welcome':
                feed.append(welcome.get_msg())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Mark\'s RPI Scrolling LED sign arguments',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', type=int, default=4, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=-90, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')
    parser.add_argument('--speed', type=float, default=0.3, help='Speed. Between 0 and 1. Default=0.2')

    args = parser.parse_args()

    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=args.n or 4, block_orientation=args.block_orientation or -90, rotate=args.rotate or 0)

    while True:

        if feed:
            msg = feed.pop()
            print(msg)
            show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=args.speed or 0.2)
        else:
            add_to_feed()
