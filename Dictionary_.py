import json
import difflib
data=json.load(open(r'C:\Users\dharmesh\Documents\PYTHON\data.json'))

def dictionary(word):
    word.lower()
    if word in data.keys():
        return data[word]
    elif len(difflib.get_close_matches(word,data.keys()))>0:
        yn=input(f'Do you mean {difflib.get_close_matches(word,data.keys())[0]} ,enter Y for yes and N for no=')
        if yn == 'Y':
            return data[difflib.get_close_matches(word,data.keys())[0]]
        elif yn == 'N':
            return 'No such words are present'    


    else:
        return 'No such words are present'


print(dictionary(input('ENTER word to find its meaning=')))

