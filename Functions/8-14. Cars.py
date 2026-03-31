"""Program with a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the 
function with the required information and two other name-value pairs, 
such as a color or an optional feature.Print the dictionary that’s 
returned to make sure all the information was stored correctly."""

def make_car(manf, model, **car_info):
    """Stores info about cars in a dictionary."""
    car_info['manufacturer'] = manf
    car_info['model_name'] = model
    return car_info

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)
