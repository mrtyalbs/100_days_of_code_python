import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

URL = "https://www.amazon.com/Lenovo-Ideapad-Touchscreen-i3-1005G1-Processor/dp/B08B6F1NNR/ref=sr_1_3?keywords=laptop&qid=1672136183&sprefix=laptop%2Caps%2C231&sr=8-3&th=1"

USER = "your@mail.com"
PASSWORD = "password"

BUY_PRICE = 200

# HTTP header
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept_Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = requests.get(URL, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")
price = soup.find(class_="a-offscreen").getText()
price_without_currency = float(price.split("$")[1])
title = soup.find(id="productTitle").getText()


if price_without_currency <= BUY_PRICE:
    with SMTP("smtp.office365.com", 587) as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER, to_addrs="adress to send",
                            msg=f"Subject:Price Alert\n\n{title} is now {price}")


