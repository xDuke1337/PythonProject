#Add json libary
import json

#Opening the json file (data.json)
data = json.load(open("data.json"))

#printing simple value from data
#print(data['rain'])

#create function will return the word typed from data
def search(w):
    d = '' + w + '';
    print(data['rains'])

#Get user input & print word value
word = input("Enter your search: ")
search(word)
