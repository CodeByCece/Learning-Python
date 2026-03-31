"""A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free;
if they are between 3 and 12, the ticket is $10;
and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket."""

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
        