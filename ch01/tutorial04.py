from functions import tutorial_post

name = input("あなたの名前は？ : ")
response = tutorial_post(name)

print(response)