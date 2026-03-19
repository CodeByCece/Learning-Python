# 7-4 Pizza Toppings

pizza_toppings = "Enter a pizza topping you would like: "
pizza_toppings += "\nEnter 'quit' to exit the program."

pizza = " " # Variable that keeps track of value the user inputs

while pizza != 'quit':
    pizza = input(pizza_toppings)

    if pizza != 'quit': # Prints value in pizza only when pizza != 'quit'
        print(f"I'll add {pizza} to your pizza!")