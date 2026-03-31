"""Modify your program from Exercise 6-2 (page 99)
so each person can have more than one favorite number. Print each person’s
name along with their favorite numbers."""

favorite_numbers = { 
    'Casey' : [5, 8, 10, 11],
    'Devin' : [14, 7],
    'Judy' : [13, 9, 444],
    'Clarissa' : [11, 22, 33],
    'John' : [88, 55, 2],
    }

for names, numbers in favorite_numbers.items():
    print(f"{names.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
