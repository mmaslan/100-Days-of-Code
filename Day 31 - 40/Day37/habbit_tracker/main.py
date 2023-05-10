import requests
from datetime import datetime

USERNAME = "mmaslan"
TOKEN = ""
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creator_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "data": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),

}

# response = requests.post(url=pixel_creator_endpoint, json=pixel_data, headers=headers)
# print(response)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graph/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graph/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

requests.delete(url=delete_endpoint, headers=headers)