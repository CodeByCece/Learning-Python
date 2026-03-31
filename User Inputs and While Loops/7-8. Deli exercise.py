"""Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made."""

sandwich_orders = ['italian', 'cheesesteak', 'blt', 'po boy', 'hoagie']

# Create an empty list
finished_sandwiches = []

# Set condition for the while loop
while sandwich_orders: 
    sandwich = sandwich_orders.pop() # Assign variable to items removed from sandwich_orders list
    print(f"I have printed your {sandwich.title()} sandwich.") # Display current value in sandwich variable
    finished_sandwiches.append(sandwich) # Move items from sandwich_orders list to finished_sandwiches list

# Display completed sandwiches
print("\nAll of the sandwiches have been made.")
print(f"Here are your finished sandwiches: \n{finished_sandwiches}")