"""Turn your if-else chain from Exercise 5-4 into an if-elifelse
chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien."""

# Executes if statement block when alien color is 'green'
alien_color = 'green'

if alien_color == 'green':
    print("Player has earned 5 points!")
elif alien_color == 'yellow':
    print("Player has earned 10 points!")
else:
    print("Player has earned 15 points!")

# Executes elif block when alien color is 'yellow'
alien_color = 'yellow'

if alien_color == 'green':
    print("Player has earned 5 points!")
elif alien_color == 'yellow':
    print("\nPlayer has earned 10 points!")
else:
        print("Player has earned 15 points!")

# Executes else block when alien color is not 'green' or 'yellow'
alien_color = 'red'

if alien_color == 'green':
    print("Player has earned 5 points!")
elif alien_color == 'yellow':
    print("Player has earned 10 points!")
else:
    print("\nPlayer has earned 15 points!")