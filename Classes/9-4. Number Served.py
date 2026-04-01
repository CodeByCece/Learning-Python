"""Utilized restaurants.py program to add a new attribute called number_served to 
represent the number of customers the restaurant has served so far. This attribute 
is intially assigned a default value of 0 but throughout this program the number_served attribute is 
is modifed through direct value assignment, modification through method and incremented through a method."""


class Restaurant:
    # Assign default value to number_served
    def __init__(self,name, cuisine, number_served=0): 
        """Initializes cuisine attributes"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = number_served 

    def des_restaurant(self):
        """decribes restaurant name and cuisine speciality."""
        print(f"The name of the restaurant is {self.name} and their cuisine speciality is {self.cuisine}.")
    
    def open_restaurant(self):
        """prints message indicating restaurant is open."""
        print(f"The {self.name} restaurant is now open!")
    
    def set_number_served(self,served):
        """sets the number of customers that have been served."""
        print(f"{restaurant.name} has served {served}.")
        
    def increment_number_served(self, increment):
        """increments the number of customers who've been served."""
        print(f"{restaurant.name} has now served {increment}.")

# Create instance
restaurant = Restaurant('Blue Lagoon', 'mexican fusion')

# print restaurant name and number served
print(f"{restaurant.name} has served {restaurant.number_served} customers.")

# Modify the attribute directly
restaurant.number_served = 44

# print restaurant name and number served
print(f"{restaurant.name} has just now served {restaurant.number_served} customers.")

# Modify attribute through set_number_served method
restaurant.set_number_served(50) # 50 argument passes to served parameter

# Increment number_served attribute through increment_number_served method
restaurant.increment_number_served(100) # 100 argument passes to increment parameter
