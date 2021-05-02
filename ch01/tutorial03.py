# weather.pyからget_weather_without_libraryを呼び出す
from weather import get_weather_without_library

response = get_weather_without_library()

print(response)

print("---------------------")

print(response['targetArea'])
print(response['text'])