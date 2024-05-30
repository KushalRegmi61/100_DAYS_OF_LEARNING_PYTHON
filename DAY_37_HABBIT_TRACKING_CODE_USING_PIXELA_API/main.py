import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

#getting hold of today Date and time

# today = datetime(2024, 5,24)
today = datetime.now()
DATE = today.strftime("%Y/%m/%d")
print(DATE)


#setting the variable values

USERNAME = os.getenv("pixela_username")
TOKEN = os.getenv("my_password")
GRAPH_ID = "codegraph"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
coding_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

header = {
    "X-USER-TOKEN": TOKEN
}


#TODO CREATING A NEW ID ON PIXELA API
# user_params = {
#     "token": TOKEN,
#     "username":USERNAME,
#     "agreeTermsOfService":"yes",
#     "notMinor": "yes"
# }
#response = requests.post(url=pixela_endpoint, json=user_params)


#TODO CREATING A CYLING CURVE GRAPH IN PIXELA API 
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Coding Curve",
#     "unit": "mins",
#     "type": "float",
#     "color": "momiji"
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)


#TODO POSTING THE DAILY CODING HOURS TO PIXELA API 
post_config = {
    "date":DATE,
    "quantity":input("How many minutes did you code today? ")
}
response = requests.post(url=coding_graph_endpoint, json=post_config, headers=header)
print(response.text)


#TODO  updating the data using put() method
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240524"
# update_config = {
#     "quantity":"30"
# }
# response = requests.put(url=update_endpoint, json=update_config, headers=header)
# print(response.text)


#TODO DELETING A PIXEL(DATA) USING delete() method
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240524"
# response = requests.delete(url=delete_endpoint,headers=header)
# print(response.text) 




