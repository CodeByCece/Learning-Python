# 8-5 Cities

# Define function
def describe_city(city, country = 'china'): # Assign a default value to country parameter
    """describe_city accepts a name of a city and it's country"""
    print(f"{city.title()} is located in {country.title()}.\n")

# Call describe_city for three different cities
describe_city('beijing')
describe_city('tianjin')
describe_city('massachusetts', country = 'the United States')