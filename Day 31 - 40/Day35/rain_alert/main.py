import json
import requests
import datetime

OMW_Endpoint = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = '588237482f885cef420a4fa9796cd1b9'

weather_params = {
    'lat': 54.356030,
    'lon': 18.646120,
    'appid': api_key
}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
# weather_data = data["weather"][""]
# print(weather_data)