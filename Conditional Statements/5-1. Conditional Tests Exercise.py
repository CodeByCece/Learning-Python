"""Write a series of conditional tests. 
Print a statement describing each test and your prediction of each test.
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False."""

car = 'subaru'
print("Is your car == 'subaru'? I predict True.")
print(car == 'subaru')

car = 'audi'
print("Is your car == 'audi'? I predict True.")
print(car == 'audi')

car = 'bmw'
print("Is your car == 'bmw'? I predict True.")
print(car == 'bmw')

car = 'VW'
print("Is your car == 'VW'? I predict True.")
print(car == 'VW')

car = 'toyota'
print("Is your car == 'toyota'? I predict True.")
print(car == 'toyota')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi') # The output of this is false 
#The value of car is already assigned to the string 'subaru' 

print("Is car == 'VW'? I predict False.")
print(car == 'VW') 


print("Is your car == 'bmw'? I predict False.")
print(car == 'bmw')


print("Is your car == 'subaru'? I predict False.")
print(car == 'subaru')


print("Is your car == 'audi'? I predict False.")
print(car == 'audi')
