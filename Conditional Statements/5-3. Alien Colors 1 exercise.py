"""Imagine an alien was just shot down in a game. Create a variable
called alien_color and assign it a value of 'green', 'yellow', or 'red'.
    • Write an if statement to test whether the alien’s color is green. 
    If it is, print a message that the player just earned 5 points.
    • Write one version of this program that passes the if test and another 
    that fails. (The version that fails will have no output.)"""

alien_color_1 = 'green'

# Version that passes conditional if test
if alien_color_1 == 'green':
    print('\nPlayer has earned 5 points!')

elif alien_color_1 == 'yellow':
    print('\nPlayer color is yellow!')
else:
    print("    ")


alien_color_2 = 'red'

# Verison that fails conditional if test
if alien_color_2 == 'green':
    print('\nPlayer has earned 5 points!')
elif alien_color_2 == 'yellow':
    print('\nPlayer color is yellow!')
else:
    print("")