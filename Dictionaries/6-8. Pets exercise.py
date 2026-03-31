"""Make several dictionaries, 
where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your 
list and as you do, print everything you know about each pet."""

owner_1 ={
    'owner_name': 'owen',
    'pet': 'dog',
}

owner_2 = {
    'owner_name': 'emily',
    'pet': 'cat'
}

owner_3 = {
    'owner_name': 'hannah',
    'pet': 'rabbit'
}

owner_4 = {
    'owner_name': 'jack',
    'pet': 'iguana'
}

owner_5 = {
    'owner_name': 'don',
    'pet': 'snake'
}

owner_6 = {
    'owner_name': 'brandy',
    'pet': 'ferret'
}

# Store dictionaries in a list
pets = [owner_1, owner_2, owner_3, owner_4, owner_5, owner_6]

for pet in pets:
    print(pet)
