import json
import difflib
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        most_related = get_close_matches(word, data.keys())[0]
        user_res = input("Did you mean %s instead? (y/n): " % most_related)

        if user_res.lower() == "y":
            return data[most_related]
        else:
            return "Word not found"
    else:
        return "Word not found"

word = input("Enter word: ")

print(translate(word))