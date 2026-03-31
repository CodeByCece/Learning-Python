"""Make a list of five or more usernames, including the name 'admin'. 
Imagine you are writing code that will print a greeting to each user
after they log in to a website.
 Loop through the list, and print a greeting to each user:
    • If the username is 'admin', print a special greeting, 
    • Otherwise, print a generic greeting.
"""
usernames = ['nando', 'bill92', 'halo4eva', 'N4S', 'gamer123', 'admin']

for name in usernames:
    if name == 'admin':
        print("\nHello admin, would you like to see a status report?")
    else:
        print(f"\nHello {name}, thank you for logging in again.")
