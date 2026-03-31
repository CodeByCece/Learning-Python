"""Think of at least five places in the world you would like to visit.
    • Store the locations in a list. Make sure the list is not in alphabetical order.
    • Print your list in its original order. Do not worry about printing the list neatly,
    just print it as a raw Python list.
    • Use sorted() to print your list in alphabetical order without modifying the
    actual list.
    • Show that your list is still in its original order by printing it.
    • Use sorted() to print your list in reverse alphabetical order without changing
    the order of the original list.
    • Show that your list is still in its original order by printing it again.
    • Use reverse() to change the order of your list. Print the list to show that its
    order has changed.
    • Use reverse() to change the order of your list again. Print the list to show
    it is back to its original order.
    • Use sort() to change your list so it is stored in alphabetical order. Print the
    list to show that its order has been changed.
    • Use sort() to change your list so it is stored in reverse alphabetical order.
    Print the list to show that its order has changed."""

bucket_list = ['South Africa', 'Brazil', 'Vienna', 'Albania', 'Iceland']

# Output list in it's original order.
print(f"Original list:") 
print(bucket_list)

# Sort and output list in alphabetical order.
print("\nAlphabetically sorted list:") 
print(sorted(bucket_list)) 

# Repeat print function to show the original list remains unchanged.
print(f"\nOriginal list:") 
print(bucket_list)

# Sort and output list in reverse-alphabetical order.
print("\nList sorted in reverse-alphabetical order:") 
print(sorted(bucket_list, reverse=True))

# Repeat print function to show the original list remains unchanged.
print(f"\nOriginal list:") 
print(bucket_list)

# Use reverse method to change order of list.
bucket_list.reverse()
print("\nList in reverse order.")
print(bucket_list)

# Use reverse method again to return list to original order.
bucket_list.reverse()
print(f"\nList back to original order again:")
print(bucket_list)

# Use sort() method to output list in alphabetical order.
bucket_list.sort()
print("\nAlphabetically sorted list:") 
print(bucket_list)

# Sort and output list in reverse-alphabetical order.
bucket_list.sort(reverse=True)
print("\nList sorted in reverse-alphabetical order:") 
print(bucket_list)