"""Add an if test to hello_admin.py to verify the list of users is not empty.
    • If the list is empty, print the message We need to find some users!
    • Remove all of the usernames from your list, and make sure the correct
message is printed."""


usernames = ['nando', 'bill92', 'halo4eva', 'N4S', 'gamer123', 'admin']

for name in usernames:
    if name == 'admin':
        print("\nHello admin, would you like to see a status report?")
    else:
        print(f"\nHello {name}, thank you for logging in again.")

if usernames: 
    for name in usernames:
        print(f"Hello {name}, welcome to the game.")
else:
    print("We need to find some users!")

# Removes all usernames in list
del usernames[:]

# Evaluates if username's list is empty
if usernames: 
    for name in usernames:
        print(f"Hello {name}, welcome to the game.")
else:
    print("\nUsername list is empty. We need to find more users!")