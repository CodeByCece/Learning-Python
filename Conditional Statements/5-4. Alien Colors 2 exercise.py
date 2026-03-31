"""Choose a color for an alien as you did in Exercise 5-3, 
and write an if-else chain.
• If the alien’s color is green, print a statement that the player 
just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that 
the player just earned 10 points.
• Write one version of this program that runs the if block
and another that runs the else block."""

# Version 1 prints if statement block
alien_color = 'green'
if alien_color == 'green':
    print("Player earned 5 points for shooting the alien!")
else:
    print("The player just earned 10 points!")

# Version 2 prints else statement block
alien_color = 'yellow'
if alien_color == 'green':
    print("\nPlayer earned 5 points for shooting the alien!")
else:
    print("\nThe player just earned 10 points!")