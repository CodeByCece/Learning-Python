#5-9 No Users based on 5-8

usernames = []

if usernames: #if usernames list is empty, Python will ignore the if statement and automatically execute the else statement
    for name in usernames:
        print(f"Hello {name}, welcome to the game.")
else:
    print("We need to find some users!")