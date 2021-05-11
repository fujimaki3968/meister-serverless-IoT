import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

base_url = ""
API_KEY = os.environ.get("TASK01_KEY")

params = {"first_name": "Haruki", "last_name": "Fujimaki"}
headers = {
    "x-api-key": API_KEY
}

response = requests.post(base_url+"/chapter02/task01", json=params, headers=headers)

print(response.json())