"""Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python 
can add a million numbers."""

# Generate an empty list
list = []

# Use for loop to generate a list of numbers from 1 - 1,000,000
for value in range(1, 1000001):
    list.append(value)

# Print minimum and maximum values in list
print(f"Minimum: {min(list)}")
print(f"Maximum: {max(list)}")
