"""You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list."""

guest_list = ['mark', 'brandon', 'jim', 'emily']

print('\nThe resturant has informed me a bigger table is available.')
guest_list.insert(0, 'mary')
guest_list.insert(2, 'hillary')
guest_list.append('sally')

print('\nHere is the updated guest list.')
print(guest_list)