"""Using person.py. Make two new dictionaries representing different people, 
and store all three dictionaries in a list called people.
 Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

person_1 = {
    'first_name': 'Chantal', 
    'last_name' : 'Douglas',
    'age' : 32,
    'city' : 'Philadelphia'}

person_2 = {
    'first name': 'Hannah',
    'last name': 'Gerald',
    'age': 40,
    'city': 'Pittsburgh'}

person_3 = {
    'first name': 'Jessica',
    'last name': 'Botland',
    'age': '30',
    'city': 'Chicago'}

# Store the dictionary's in a list 
people = [person_1, person_2, person_3]

# for loop to cycle through each dictionary
for person in people:
    print(person)
    
          