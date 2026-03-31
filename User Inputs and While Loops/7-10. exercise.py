"""Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll."""

# Establish empty dictionary
poll = {}

# Set flag variable and initalize state to be true
polling_active = True

while polling_active:
    name = input("What is your name? ")
    result = input("What is your dream vacation? ")

    # Store result in poll dictionary with it's correspongig key ['name']
    poll[name] = result

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False # Change in flag state exits the while loop

# Display polling results
print("\n ---Poll Results--- ")
for name, result in poll.items():
    print(f"{name}'s dream vacation is {result}.")

