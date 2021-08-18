import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0 :
        print("Did you mean %s instead ? " %get_close_matches(word, data.keys())[0])
        decide = input('Press y for Yes or n for No : ')
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("Thanks and good bye")
        else:
            return("You have return Wrong input please enter y or n")

    else: 
        print("You have entered wrong word please check it again !!!")




word = input('Enter the Word you want to Search : ')
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)