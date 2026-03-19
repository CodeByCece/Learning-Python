#Chapter 5 exercises
#for loop checks for current value of car for 'bmw'
#if it is, then it prints 'bmw' in upper case 'BMW'
#for all other conditions, the string value car iterates through is title cased

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


requested_topping = 'mushrooms'
if requested_topping != 'anchioves':
    print('Hold the anchioves!')

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")