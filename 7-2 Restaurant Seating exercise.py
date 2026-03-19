# 7-2 Restaurant Seating exercise

# Prompt user on how many people are in their dinner part
# Store the user's input in the variable, seat
seat = input("How many people are in your dinner group: ")

seat = int(seat) # Convert the user's input to an integer

if seat > 8:
    print("\nYou will have to wait for a table.")

else: 
    print("Your table is ready.")