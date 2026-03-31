"""Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, 
print a message saying they’ll have to wait for a table. 
Otherwise, report that their table is ready."""


seat = input("How many people are in your dinner group: ")

seat = int(seat) # Convert the user's input to an integer

if seat > 8:
    print("\nYou will have to wait for a table.")

else: 
    print("Your table is ready.")