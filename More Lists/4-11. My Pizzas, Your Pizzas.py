"""Start with your program from Exercise 4-1. 
Make a copy of the list of pizzas, and call it friend_pizzas.
    • Add a new pizza to the original list.
    • Add a different pizza to the list friend_pizzas.
    • Prove that you have two separate lists. Print the message My favorite
pizzas are:, and then use a for loop to print the first list. 
Print the message My friend’s favorite pizzas are:, 
and then use a for loop to print the second list.
 Make sure each new pizza is stored in the appropriate list."""

pizza_types = ['pepperoni', 'sausage', 'cheese'] 

friend_pizzas = pizza_types[:] # Copies elements in pizza_types list

pizza_types.append('pineapple')
friend_pizzas.append('buffalo chicken')

print("My favorite pizzas are:")
for favorite in pizza_types[:1]:
    print(pizza_types)

print("\nMy friend's favorite pizzas are:")
for friends_favorite in friend_pizzas[:1]:
    print(friend_pizzas)


