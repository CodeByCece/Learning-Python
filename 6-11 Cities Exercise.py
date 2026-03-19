# 6-11 Cities Exercise

cities = {
    'new york city': {
        'country': 'united states',
        'population': '8.3 million',
        'fact': 'NYC is home to the statue of liberty.',
    },

    'london': {
        'country': 'united kingdom',
        'population': '9.9 million',
        'fact': 'london is technically classifed as a forest.'
    },
    'los angeles': {
        'country': 'united states',
        'population': '3.8 million',
        'fact': ' Los angeles is the only city to have hosted the summer olympics twice.',
    }
}

for city, city_info in cities.items():
    print(f"City: {city.title()}")
    place = f"{city_info['country']}"
    pop = f"{city_info['population']}"
    fun_fact = f"{city_info['fact']}"

    print(f"\tCountry: {place.title()}")
    print(f"\tPopulation: {pop.title()}")
    print(f"\tFun fact: {fun_fact}\n")
