import requests
from datetime import *
import smtplib
import time

# Mail username and password
USER = "your@mail.com"
PASSWORD = "password"

MAIL_TO_SEND = "mail_to_send@mail.com"

# Coordinates of my location
MY_LAT = 40.951476
MY_LNG = 29.128793


def is_iss_overhead():
    # Request to ISS position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    # Request to sunrise and sunset time
    time_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    time_response.raise_for_status()

    time_data = time_response.json()
    sunrise_time = int(time_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_time = int(time_data["results"]["sunset"].split("T")[1].split(":")[0])

    # Current time
    current_time = datetime.now().time().hour
    # Check is it dark
    if current_time >= sunset_time or current_time <= sunrise_time:
        return True


while True:
    # Wait 300 sec for running this script
    time.sleep(300)

    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.office365.com", 587) as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(from_addr=USER,
                                to_addrs=MAIL_TO_SEND,
                                msg="Subject:Look up!!!\n\nThe ISS is above you in the sky."
                                )
