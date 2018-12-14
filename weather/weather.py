# coding=utf-8
import requests
import os

api_key = os.environ['WEATHER_API_KEY']
city_id = os.environ['CITY_ID']

def get_weather():
    global api_key, city_id
    current_weather = requests.get('http://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={api_key}&units=imperial'.format(
        city_id=city_id, api_key=api_key)).json()

    if current_weather['cod'] == 200:
        return('Today\'s weather: {description}, with a high of {high}* and a low of {low}*. It is currently {current_temp}*.'.format(
            description=current_weather['weather'][0]['description'],
            high=int(current_weather['main']['temp_max']),
            low=int(current_weather['main']['temp_min']),
            current_temp=int(current_weather['main']['temp'])))
    return 'Error getting weather.'
