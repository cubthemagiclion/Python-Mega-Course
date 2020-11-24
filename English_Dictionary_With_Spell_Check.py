import json
import os
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json","r"))

def look_up_from_dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    else:
        list_of_possible_matches = get_close_matches(w, data.keys(),cutoff=0.8)
        if(len(list_of_possible_matches) == 0):
            return "Word currently unavailable."
        else:
            if_typed_wrong = input("Do you mean one of the following words? %s Write Y or N: " % list_of_possible_matches)
            if if_typed_wrong == "Y":
                correct_number = int(input("Please enter which one is your intended word by number: "))
                return data[list_of_possible_matches[correct_number-1]]
            else:
                return "Word currently unavailable."

word = input("Please enter the word you want to look up (enter exit to end the program.): ")
while word!= "exit":
    output = look_up_from_dictionary(word)
    if type(output) == list and len(output) > 1: #for multiple definitions.
        for index,item in (enumerate(output)):
            print("Definition " + str(index+1) + ": " + item)
    elif type(output) == list:
        print("Definition: " + output[0]) #The ones with only 1 defition.
    else:
        print(output) #This will be "Word currently unavailable."


    word = input("Please enter the word you want to look up (enter exit to end the program.): ")

print("Program ended.")