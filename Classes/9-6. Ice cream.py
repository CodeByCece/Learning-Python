"""Ice cream stand inheritance example."""

class Restaurant:

    def __init__(self,name, cuisine):
        """Initializes cuisine attributes"""
        self.name = name
        self.cuisine = cuisine

    def des_restaurant(self):
        """decribes restaurant name and cuisine speciality."""
        print(f"The name of the restaurant is {self.name} and their cuisine speciality is {self.cuisine}.")
    
    def open_restaurant(self):
        """prints message indicating restaurant is open."""
        print(f"The {self.name} restaurant is now open!")

class IceCreamStand(Restaurant):
    def __init__(self,name, cuisine):
        """Initalizes attributes of the parent class.
        Define flavor attribute specific to the Ice Cream Stand.
        flavor stores a list of ice cream flavors"""
        super().__init__(name, cuisine)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def display_flavor(self):
        """display ice cream flavors"""
        print(f"Current ice cream stand flavors are: {self.flavors}.")

# Create new instance 
ice_cream = IceCreamStand('Ice Cream Stand', 'ice cream')

# Call display_flavor method 
ice_cream.display_flavor()

"""
# Create instance
restaurant = Restaurant('Blue Lagoon', 'mexican fusion')

# Print attributes individually
print(f"{restaurant.name}")
print(f"{restaurant.cuisine}")

# Call both methods
restaurant.des_restaurant()
restaurant.open_restaurant()



"""

