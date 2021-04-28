import json
import urllib.request
import requests

uri = "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json"

def get_weather_without_library():
    request = urllib.request.Request(uri)
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read())

def get_weather_with_library():
    response = requests.get(uri)
    return response.json()