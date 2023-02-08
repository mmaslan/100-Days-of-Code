import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_PHONE = os.environ['TWILIO_GENERATED_NUMBER']
PERSONAL_NUMBER = os.environ['TWILIO_PERSONAL_NUMBER']

STOCK_API = os.environ['ALPHA_VANTAGE_API']
NEWS_API_KEY = os.environ['NEWSAPI']

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(float(yesterday_closing_price)) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = difference / float(yesterday_closing_price) * 100

if diff_percent > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_article_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH)
    for article in formatted_article_list:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE,
            to=PERSONAL_NUMBER,
        )
