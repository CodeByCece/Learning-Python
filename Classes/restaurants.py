"""A set of classes used to represent restuarants."""

class Restaurant:

    def __init__(self,name, cuisine):
        """Initializes restaurant attributes"""
        self.name = name
        self.cuisine = cuisine

    def des_restaurant(self):
        """decribes restaurant name and cuisine type."""
        print(f"The name of the restaurant is {self.name} and their speciality is {self.cuisine}.\n")
    
    def open_restaurant(self):
        """prints message indicating restaurant is open."""
        print(f"The {self.name} restaurant is now open!")
