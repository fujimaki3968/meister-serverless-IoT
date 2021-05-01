import os

import requests
import json

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")

headers = {"x-api-key": API_KEY}

'''
出席APIにPOSTするコード
'''

#### キーボード入力から各パラメーターを入力させてください。




####

params = {
    # 仕様にそってパラーメーターを記述してください。
}
param_json = json.dumps(params)
response = requests.post("https://4rddu45n7e.execute-api.us-east-1.amazonaws.com/default/ch01/attendance", data=param_json, headers=headers)

response_json = response.json()

if response_json['statusCode'] == 200:
    print(response_json['body'])
elif response_json['statusCode'] == 400:
    print("エラー")
    print(response_json['message'])
else:
    print("予期せぬエラーが発生しました。")