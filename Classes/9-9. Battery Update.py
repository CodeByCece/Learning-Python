"""Modification of electric_car.py"""

class Car:
    """Class representing general aspects of a car."""

    def __init__(self, make, model, year):
        """Initalize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Assign defualt value
    
    def get_descriptive_name(self):
        """Reformat and print description of car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print current mileage on odometer."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """Updates mileage on odometer reading."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Adds the given mileage to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """Class representing aspects of a battery for an electric car."""
     # Assign default value to battery size
    def __init__(self, battery_size=75): 
        """Initialize the battery's attribute's."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Prints a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Prints a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a {self.battery_size}% charge.")
    
    def upgrade_battery(self, size):
        """Checks battery size"""
        if size != 100: # Checks battery size
            self.battery_size = 100 # Resets battery capacity to 100
        elif size == 100:
            print("Battery is at full capacity.") 

class ElectricCar(Car):
    """Class representing aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()
        

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery(99) 
my_tesla.battery.get_range()


