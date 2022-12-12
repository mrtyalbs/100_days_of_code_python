import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "SZORFWBINOW13NDD"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "bd553d325cf242f9b4d3b49717f10cc6"

# Twilio API
account_sid = "AC7c357bb2c70d78979800071781270f39"
auth_token = "0549b71f9a1e07f77368c2e0bac53485"


# Get yesterday's closing stock price.
stock_price_api_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_price_api_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

# Find the positive difference between
positive_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)


# Get percentage difference
percentage_difference = (positive_difference / yesterday_closing_price) * 100


# If percentage is greater than 5 then print("Get News").
if percentage_difference > 1:
    # Get articles related to the COMPANY_NAME.
    news_params = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    # Create a list that contains the first 3 articles.
    three_articles = articles[:3]

    # Create a new list of the first 3 article's headline and description using list comprehension.
    headlines = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    # Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)
    for headlines in three_articles:
        message = client.messages \
            .create(
            body=headlines,
            from_='your twilio number',
            to='your verified number',
        )
        print(message.status)


