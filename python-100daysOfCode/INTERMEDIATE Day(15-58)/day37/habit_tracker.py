import requests
from datetime import datetime
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = "jdwi8e882hnnsixxaxmxj77sjsj"
USERNAME = "shubhambatman"
GRAPH_ID = "shubhamgraph1"
user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
# #setting up a new account on pixela
# response = requests.post(url = PIXELA_ENDPOINT, json = user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}
# POST posting the graph
# response = requests.post(url=GRAPH_ENDPOINT,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today?"),
}
# # posting the pixel
response = requests.post(url=pixel_creation_endpoint,
                         json=pixel_data, headers=headers)
print(response.text)

# PUT Updating the pixel
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "18",

}
# response = requests.put(url=update_endpoint,
#                         json=new_pixel_data, headers=headers)

# print(response.text)


# DELETE deleting the pixel

# delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)


# graph
# 1 https://pixe.la/v1/users/shubhambatman/graphs/shubhamgraph1.html
# 2 https://pixe.la/v1/users/shubhambatman/graphs/shubhamgraph1
