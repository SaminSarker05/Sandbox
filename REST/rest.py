import requests
import json

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
print(response.status_code)

data = response.json()
for question in data['items']:
  print(question['title']) 