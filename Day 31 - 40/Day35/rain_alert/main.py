import os
import json
import requests
import datetime
from twilio.rest import Client

OMW_Endpoint = 'http://api.openweathermap.org/data/2.5/onecall'

api_key = os.environ['OPEN_WEATHER_KEY']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = os.environ['TWILIO_NUMBER']
personal_number = os.environ['TWILIO_PERSONAL_NUMBER']

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

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella.",
        from_=f'{twilio_phone_number}',
        to=f'{personal_number}'
    )

    print(message.sid)
