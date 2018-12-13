# RPI-Scrolling-LED-Sign
Display weather, tweets, news headlines, weather, and more on a scrolling LED sign hooked up to a Raspberry Pi

##Hardware Setup
TODO

##Software Setup
On your RPI, follow these steps:
https://luma-led-matrix.readthedocs.io/en/latest/install.html

1. ###Install pip

`sudo apt-get install python-dev python-pip`

2. ###Install Python packages

```
sudo pip install requests
sudo pip install max7219
```

3. ###Create API keys file 
Create file `API_KEYS.env` in the root directory.

```
# twitter
CONSUMER_KEY=
CONSUMER_SECRET=
ACCESS_TOKEN=
ACCESS_TOKEN_SECRET=

# mta
MTA_API_KEY=

# weather
WEATHER_API_KEY=

# news
NEWS_API_KEY=
```

4. ###Obtain API keys

#####New York Subway MTA API

```
sudo pip install --upgrade gtfs-realtime-bindings
sudo pip install protobuf3_to_dict
sudo pip install -U python-dotenv
```

Obtain your API key [here](https://datamine.mta.info/user/register), and add it to `API_KEYS.env`. 
Next, configure the `mta/MTA.env` file with the appropriate train information that you want displayed.

#####Weather

Obtain your API key [here](https://home.openweathermap.org/users/sign_up), and add it to `API_KEYS.env`.
Change city in `weather/WEATHER.env` using your city code found [here](http://bulk.openweathermap.org/sample/city.list.json.gz).

#####Twitter

`sudo pip install tweepy`

Obtain your API keys and tokens by creating an app [here](https://developer.twitter.com/en/apply-for-access.html), 
and add the details to `API_KEYS.env`.

#####News

`sudo pip install newsapi-python`

Obtain your API key [here](https://newsapi.org), and add it to `API_KEYS.env`.

5. ###Modify config

In `feed-config.json`, you can enable, disable, and change the frequency of each feed type. Make sure the frequencies add up to 1.

6. ###Run

`python feed.py`