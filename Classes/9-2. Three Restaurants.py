

class Restaurant:

    def __init__(self,name, cuisine):
        """Initializes cuisine attributes"""
        self.name = name
        self.cuisine = cuisine

    def des_restaurant(self):
        """decribes restaurant name and cuisine speciality."""
        print(f"The name of the restaurant is {self.name} and their cuisine speciality is {self.cuisine}.\n")
    
    #def open_restaurant(self):
    #    """prints message indicating restaurant is open."""
    #    print(f"The {self.name} restaurant is now open!")

restaurant_1 = Restaurant('Blue Lagoon', 'mexican fusion')
restaurant_1.des_restaurant()

restaurant_2 = Restaurant('Panda city', 'taiwanese')
restaurant_2.des_restaurant()

restaurant_3 = Restaurant('Down South Cooking', 'soul food')
restaurant_3.des_restaurant()
