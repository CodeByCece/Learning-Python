#5-10 Checking Usernames

current_users = ['nando', 'bill92', 'halo4eva', 'N4S', 'gamer123', 'admin']
new_users = ['melissa89', 'N4S', 'Cary', 'gamer123', 'melody']

for name in new_users:
    if name in current_users:
        print(f"\nUsername you selected is {name}.")
        print('Player needs to enter a new username.')
    else:
        print(f"\nUsername you selected is {name}.")
        print('Username is available.')

        