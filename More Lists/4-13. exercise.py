"""A buffet-style restaurant offers only five basic foods. 
Think of five simple foods, and store them in a tuple.
    • Use a for loop to print each food the restaurant offers.
    • Modify one of the items, and make sure that Python rejects the change.
    • The restaurant changed its menu, replace 2 items with different foods. 
    Add a line that rewrites the tuple, and then use a for loop to print
    each of the items on the revised menu."""

buffet = ('chicken', 'dumplings', 'fortunte cookies', 'rice', 'melon')
print("This is the original buffet menu:")
for food in buffet:
    print(food)

# Modification that Python rejects
# buffet[2] = 'drumbsticks'

# Changed restuarant menu
buffet = ('apples', 'fishsticks', 'orange chicken', 'bourbon chickent', 'sticky rice')
print("\nThis is the modified buffet menu:")
for food in buffet:
    print(food)
