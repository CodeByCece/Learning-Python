#5-8 Hello Admin

usernames = ['nando', 'bill92', 'halo4eva', 'N4S', 'gamer123', 'admin']

for name in usernames:
    if name == 'admin':
        print("\nHello admin, would you like to see a status report?")
    else:
        print(f"\nHello {name}, thank you for logging in again.")
