
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

# Create instance
restaurant = Restaurant('Blue Lagoon', 'mexican fusion')

# Print attributes individually
print(f"{restaurant.name}")
print(f"{restaurant.cuisine}")

# Call both methods
restaurant.des_restaurant()
restaurant.open_restaurant()





