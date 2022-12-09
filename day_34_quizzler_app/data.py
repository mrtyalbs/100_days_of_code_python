import requests

AMOUNT = 10
TYPE = "boolean"

parameters = {
    "amount": AMOUNT,
    "type": TYPE,
}

response = requests.get(f"https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]



