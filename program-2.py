import json 
from difflib import get_close_matches

data = json.load(open("../data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())):
        yn = input("did you mean %s insted ? type Y if yes tye N if NO : " % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "The word does not exists."
        else:
            return "Did not under stand your query"
    else:
        return "The word does not exists"

word = input("enter the word :")

output = translate(word)

if type(output) == list:
    for out in output:
        print(out)
else:
    print(output)