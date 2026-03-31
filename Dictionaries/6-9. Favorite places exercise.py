"""Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places."""

favorite_places = {
    'person_1': {
        'name': 'emily',
        'place': ['arizona', 'nevada'],
    },
    'person_2': {
        'name': 'ben',
        'place': ['colorado', 'new york'],
    },
    'person_3': {
        'name': 'brad',
        'place': ['germany', 'california', 'london'],
    }
}

 # Loop through each key-value pair in dictionary
for persons, names in favorite_places.items():
    name = f"{names['name']}"
    location = names['place']

    print(f"This is {name.title()} and their favorite places to visit are:")
    print(f"\t{location}\n")