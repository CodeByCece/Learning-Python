# 6-2 Favorite Numbers exercise

favorite_numbers = { # created dictionary of users and their favorite #
    'Casey' : 5, 
    'Devin' : 14,
    'Judy' : 13,
    'Clarissa' : 55,
    'John' : 100}


for key, value in favorite_numbers.items(): # for loop to cycle through each key-value pair in dictionary
    print(f"My friend's name is {key} and their favorite number is {value}.")