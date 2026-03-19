# Learning about Loops
#magicians = ['alice', 'david', 'carolina'] # Defines the list
#for magician in magicians: # Retrieves a value from the list and associates it w/ magician variable. The for loop iterates through each value in the list.
#    print(f"{magician.title()}, that was a great trick!")
#    print(f"I can't wait to see your next trick, {magician.title()}.\n")
#print("Thank you, everyone. That was a great magic show!")

for value in range(1,6):
    print(value)
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = [] # Defined an empty list with the variable squares
for value in range(1, 11): # for every value in this range pass it to value variable
    squares.append(value**2) #adds resultant value into the list called squares
print(squares)

squares = [value**2 for value in range(1, 11)] #ex of list comprehension
print(squares)

