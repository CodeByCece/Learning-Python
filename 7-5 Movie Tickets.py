# 7-5 Movie Tickets

prompt = "\nPlease enter your age: "
prompt += "\nEnter 'quit' to exit the program."

active = True # active serves as the flag variable for the while loop

while active: # while active is true
    age = input(prompt)
    if age == 'quit':
        active = False # Changes boolean value in active to False
        break 

    age = int(age) # Changes value in age variable from a string to an integer
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("The cost of your ticket is $10.")
    else:
        print("The cost of your ticket is $15.")
        