# Create a list with the names of sandwiches
# Include 'pastrami' in that list at least three times
sandwich_orders = ['italian', 'pastrami', 'cheesesteak', 'blt', 'pastrami', 'po boy', 'pastrami', 'hoagie']

# Display print message
print("Sorry, the deli has run out of pastrami.\n")

# Create an empty list
finished_sandwiches = []

# Set condition of first while loop
# Remove each occurence of 'pasrtrami' from sandwich_orders list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Set condition of second while loop
# While sandwich_orders list contains items
while sandwich_orders:
    sandwich = sandwich_orders.pop() # Assign variable to items popped from sandwich_orders list
    print(f"I have printed your {sandwich.title()} sandwich.") # Display current value of sandwich variable
    finished_sandwiches.append(sandwich) # Move items from sandwich_orders list to finished_sandwiches list


# Display all completed sandwiches
print("\nAll of the sandwiches have been made.")
print(f"Here are your finished sandwiches: \n{finished_sandwiches}")