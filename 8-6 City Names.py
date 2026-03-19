#8-6 City Names

def city_country(city, country):
    """Accepts the name of a city and it's country."""
    formatted = f"{city.title()}, {country.title()}"
    return formatted

# Call function using three times with different city-country pairs 
travel = city_country('santiago', 'chile')
print(travel)
travel_1 = city_country('tianjin', 'china')
print(travel_1)
travel_2 = city_country('new york city', 'united states')
print(travel_2)