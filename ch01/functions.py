import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")

headers = {"x-api-key": API_KEY}

def tutorial_post(name: str):
    params = {"name": name}
    response = requests.post("https://4rddu45n7e.execute-api.us-east-1.amazonaws.com/default/ch01/post", data=json.dumps(params), headers=headers)
    return response.json()