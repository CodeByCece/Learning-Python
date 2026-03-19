# 6-9 Favorite places exercise

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