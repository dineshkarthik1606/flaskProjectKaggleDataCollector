import requests
import json
response_API = requests.get('http://127.0.0.1:5000/get-kaggle-data/andrewmvd/us-schools-dataset?select=Private_Schools.csv')
print(response_API.status_code)
print(response_API.text)