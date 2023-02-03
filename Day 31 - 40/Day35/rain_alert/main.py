import json
import requests
import datetime

OMW_Endpoint = 'http://api.openweathermap.org/data/2.5/onecall'
api_key = '588237482f885cef420a4fa9796cd1b9'

weather_params = {
    'lat': 54.356030,
    'lon': 18.646120,
    'appid': api_key,
    'exclude': 'currently,minutely,daily',
}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    print(hour_data["weather"])
