#4-11 My Pizzas, Yours Pizzas from #4-1 exercise
 
pizza_types = ['pepperoni', 'sausage', 'cheese'] # list of pizza toppings
for pizza in pizza_types:
    print(f"I would like to try {pizza} on my pizza.")
    print(f"I like {pizza} pizza.\n")
print("\nI really love to eat pizza whenever I get the opportunity to visit NYC. \nIt's the best food in the world to eat. \nI really love pizza!")

friend_pizzas = pizza_types[:]

pizza_types.append('pineapple')
friend_pizzas.append('buffalo chicken')

print("My favorite pizzas are:")
for favorite in pizza_types:
    print(pizza_types[:])

print("\nMy friend's favorite pizzas are:")
for friends_favorite in friend_pizzas:
    print(friend_pizzas[:])


