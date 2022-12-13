from datetime import datetime
import requests

USERNAME = "malambilam"
TOKEN = "12345678mya"
GRAPH_ID = "graph1"

# Create user account
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)

# Create a graph
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Weight Chart",
    "unit": "kilogram",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_parameters, headers=headers)
# print(response.text)

# Post value to the graph
date = str(datetime.today().date())
today = date.replace("-", "")

today_quantity = "86.3"

VALUE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

value_paramaters = {
    "date": today,
    "quantity": today_quantity,
}

# response = requests.post(url=VALUE_ENDPOINT, json=value_paramaters, headers=headers)
# print(response.text)

# Update the data in the graph
updated_value_date = "20221213"
updated_data = "45.5"
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{updated_value_date}"

update_params = {
    "quantity": updated_data,
}

# response = requests.put(url=UPDATE_ENDPOINT, json=update_params, headers=headers)
# print(response.text)

# Delete the data from graph
deleted_value_date = "20221213"
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{deleted_value_date}"

# response = requests.delete(url=UPDATE_ENDPOINT, headers=headers)
# print(response.text)
