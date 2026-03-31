"""Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should 
print a statement, such as You really like bananas!"""

favorite_fruits = ['mango', 'pineapple', 'watermelon']
if 'mango' in favorite_fruits:
    print("I really like eating mango's!")

if 'pineapple' in favorite_fruits:
    print("\nI like eating pineapples!")

# 'lyche' is excluded from favorite_fruits list.
# So this if statement will not produce a print statement
if 'lyche' in favorite_fruits:
    print("I like eating lyche's!")

if 'watermelon' in favorite_fruits:
    print("\nI like watermelon's!")

if 'banana' in favorite_fruits:
    print("I like banana's!")
