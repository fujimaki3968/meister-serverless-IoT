import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")

base_url = "https://4rddu45n7e.execute-api.us-east-1.amazonaws.com/default/ch02/judge"

student_number = int(input('学籍番号: '))
check_url = input('APIのベースURL: ')
check_api_key = input('API KEY: ')

params = {
    "student_number": student_number,
    "base_url": check_url,
    "api_key": check_api_key
}

headers = {"x-api-key": API_KEY}

response = requests.post(base_url, json=params, headers=headers)

print(response.json())
