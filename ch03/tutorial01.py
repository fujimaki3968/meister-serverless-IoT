import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")

base_url = "https://4rddu45n7e.execute-api.us-east-1.amazonaws.com/default/ch03/"

headers = {"x-api-key": API_KEY}

### PUT
print('------- PUT -------')

student_number = input("学籍番号: ")
food = input("2番目に好きな食べ物は？ : ")
data = {
    'student_number': student_number,
    'food': food
}
response = requests.post(base_url+'dynamodb/put', json=data, headers=headers)


### GET
print('------- GET -------')

response = requests.post(base_url+'dynamodb/get', json={'student_number': student_number}, headers=headers)
print(response.json())

### SCAN
print('------- SCAN -------')

response = requests.post(base_url+'dynamodb/scan', headers=headers)
print(response.json())

### QUERY
print('------- QUERY -------')

data = {
    'task_name': 'chapter02',
    'class_name': '4J'
}
response = requests.post(base_url+'dynamodb/query', json=data, headers=headers)
print(response.json())

### UPDATE
print('------- UPDATE -------')

food = input("一番好きな食べ物は？ : ")
data = {
    'student_number': student_number,
    'food': food
}
response = requests.post(base_url+'dynamodb/update', json=data, headers=headers)


### DELETEは割愛