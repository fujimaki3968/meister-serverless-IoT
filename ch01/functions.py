import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")

headers = {"x-api-key": API_KEY}

def tutorial_post(name: str):
    params = {"name": name}

    # 辞書型のデータをJSONに変換
    param_json = json.dumps(params)
    response = requests.post("https://4rddu45n7e.execute-api.us-east-1.amazonaws.com/default/ch01/post", data=param_json, headers=headers)
    return response.json()