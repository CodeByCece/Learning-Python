# 6-9 Favorite places exercise 
# Pull code from 6-2 exercise
# Make it such that each person can have more than one favorite #

favorite_numbers = { # created dictionary of users and their favorite #
    'Casey' : [5, 8, 10, 11],
    'Devin' : [14, 7],
    'Judy' : [13, 9, 444],
    'Clarissa' : [11, 22, 33],
    'John' : [88, 55, 2],
    }

 # Loop through each key-value pair in dictionary
for names, numbers in favorite_numbers.items():
    print(f"{names.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
