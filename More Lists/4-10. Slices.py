"""Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
    • Use a slice to print the first three items from that program’s list.
    • Use a slice to print three items from the middle of the list.
    • Use a slice to print the last three items in the list."""

# Using program from Animals.py script
animals = ['leopard', 'tiger', 'panther', 'cheetah', 'cougar','lion', 'jaguar']
for animal in animals:
    print(f"A {animal} would be a great pet to have.")
print(f"\nThe leopard, tiger, panther and cheetah are all members of the Felidae family.\nThey would not make a great pet to have at home but you can see them in a zoo.")

# Outputs first three elements in the list
print("\nThe first three items in the list are:")
print(animals[0:3])

# Outputs three elements from the middle of the list
print("\nThree items from the middle of the list are:")
print(animals[3:6])

# Outputs last three elements in the list.
print("\nThe last three items in the list are:")
print(animals[-3:])
