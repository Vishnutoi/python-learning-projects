#Make your first API call
#Using the Requests module, send a request to "https://api.genderize.io/?name=your_name"
#and by using formatted strings, replace your_name with an inputted name! Output the guessed gender.

import requests

r = requests.get("https://api.genderize.io/?name=your_name")

a = r.status_code
print(r)
# basically if you receive 200 as output it means the response is good

data = r.json()
print(data)

#data['name'] = input(" input the name : ")



