#Lyrics Finder Project in Python Using JSON API

import requests

artist_input = input("Please input artist name : ")
song_input = input("please input song name : ")

url = "https://api.lyrics.ovh/v1/"+ artist_input + "/" + song_input

get_api = requests.get(url)

read_data = get_api.json()
print(read_data['lyrics'])

