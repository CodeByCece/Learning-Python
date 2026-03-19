
# Create a list with the names of sandwiches
sandwich_orders = ['italian', 'cheesesteak', 'blt', 'po boy', 'hoagie']

# Create an empty list
finished_sandwiches = []

# Set condition for the while loop
# While sandwich_orders list contains items
while sandwich_orders: 
    sandwich = sandwich_orders.pop() # Assign variable to items removed from sandwich_orders list
    print(f"I have printed your {sandwich.title()} sandwich.") # Display current value in sandwich variable
    finished_sandwiches.append(sandwich) # Move items from sandwich_orders list to finished_sandwiches list

# Display all completed sandwiches
print("\nAll of the sandwiches have been made.")
print(f"Here are your finished sandwiches: \n{finished_sandwiches}")