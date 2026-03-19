# 6-7 People exercise
# Pull in program from 6-1 exercise
# Create 2 new dictionary for 2 new people

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

# Store the dictionary's into a list called people
people = [person_1, person_2, person_3]

# Create a for loop to cycle through the info stored in each dictionary
for person in people:
    print(person)
    
          