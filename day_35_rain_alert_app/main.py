import requests
from twilio.rest import Client

# Coordinates
MY_LAT = 40.951476
MY_LNG = 29.128793

# Openweathermap API
OWM_END_POINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "69f04e4613056b159c2761a9d9e664d2"
weather_paramaters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "exclude": "current, minutely, daily",
}

# Twilio API
account_sid = "AC7c357bb2c70d78979800071781270f39"
auth_token = "0549b71f9a1e07f77368c2e0bac53485"

# Request to data from Openweathermap
response = requests.get(OWM_END_POINT, params=weather_paramaters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for index in range(0, 12):
    condition_code = weather_data["hourly"][index]["weather"][0]["id"]
    if condition_code <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember bring to an umbrella!!!",
        from_='your twilio number',
        to='your verified number'
    )
    print(message.status)
