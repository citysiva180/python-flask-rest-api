import requests

BASE = "http://127.0.0.1:5000/"


# get requests
# response = requests.get(BASE+"helloworld")
# print(response.json())

# # post requests
# response = requests.post(BASE+"helloworld")
# print(response.json())


# get requests
response = requests.get(BASE+"helloworld/Siv")
print(response.json())
