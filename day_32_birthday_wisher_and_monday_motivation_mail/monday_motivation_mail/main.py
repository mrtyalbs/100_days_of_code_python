import smtplib
import datetime
from random import choice

MY_EMAIL = "my_mail@hotmail.com"
PASSWORD = "my_password"

current_time = datetime.datetime.now()
current_day = current_time.weekday()

with open("quotes.txt") as quotes:
    quote = quotes.readlines()
    random_quote = choice(quote)


with smtplib.SMTP("smtp.office365.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    if current_day == 0:
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="muratalbas@outlook.com",
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
            )



