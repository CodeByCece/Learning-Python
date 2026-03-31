""" write more conditional tests and add them to conditional_tests.py. 
Have at least one True and one False result for each of the following:
     • Tests for equality and inequality with strings
     • Tests using the lower() method
     • Numerical tests involving equality and inequality, greater than and
     less than, greater than or equal to, and less than or equal to
     • Tests using the and keyword and the or keyword
     • Test whether an item is in a list
     • Test whether an item is not in a list"""

car = 'subaru'
print("Is your car == 'subaru'? I predict True.")
print(car == 'subaru')

car = 'audi'
print("Is your car != 'audi'? I predict True.")
print(car != 'audi')

car = 'Subaru'
car.lower() == 'subaru'

car_1 = 12 
car_2 = 50
if car_1 == 12:
     print("\nThe car_1 is equal to the value 12. ")
if car_1 >= 10 and car_1 < car_2:
    print("\nCar_1 value is greater than 10 but less than car_2.")
if car_1 != 11:
        print("\nCar 1 is not equal to the value 11.")
if car_1 < 0 or car_2 <= 50:
     print("\nAt least one of the cars has a value greater than 1")
else:
    print("nothing")

friends = ['toya', 'alice', 'brandy', 'helda']
name = 'chantal'
name_2 = 'helda'
if name not in friends:
     print(f"\nHello {name.title()}! It's so nice to meet a new friend.")
if name_2 in friends:
     print(f"\nHey {name_2.title()}, it's so nice to see you again!")
else:
     print("nothing")

     



