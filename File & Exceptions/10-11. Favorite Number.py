# program that prompts a user for their favorite number
import json

fav_number = input("What is your favorite number? ")

filename = 'fav_number.json'
with open(filename, 'w') as f:
    json.dump(fav_number,f)

"""reads value and prints it out"""
filename = 'fav_number.json'
with open(filename) as f:
    numbers = json.load(f)

print(f"Your favorite number is {numbers}")