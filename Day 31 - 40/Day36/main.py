import os
import requests

api_key = os.environ['NEWSAPI']

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key,
}

response = requests.get(NEWS_ENDPOINT, params=stock_params)
stock_data = response.json()
print(stock_data)

