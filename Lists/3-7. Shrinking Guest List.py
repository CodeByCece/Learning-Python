"""Shrinking Guest List: You just found out that your new dinner table will not
arrive in time for the dinner, and you have space for only two guests.
    • Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
    • Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you are sorry you can not invite
them to dinner.
    • Print a message to each of the two people still on your list, letting them
know they are still invited.
    • Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program."""

guest_list = ['mark', 'brandon', 'jim', 'emily']

print('\nThe resturant has informed me a bigger table is available.')
guest_list.insert(0, 'mary')
guest_list.insert(2, 'hillary')
guest_list.append('sally')

print('\nHere is the updated guest list.')
print(guest_list)

print('\nThe bigger table will not be available in time. I can invite only 2 people.')
popped_1 = guest_list.pop(0)
print(f'\nSorry, {popped_1.title()}, I can no longer invite you to the party.')
popped_2 = guest_list.pop(0)
print(f'Sorry, {popped_2.title()}, I can no longer invite you to the party.')
popped_3 = guest_list.pop(0)
print(f'Sorry, {popped_3.title()}, I can no longer invite you to the party.')
popped_4 = guest_list.pop(0)
print(f'Sorry, {popped_4.title()}, I can no longer invite you to the party.')
popped_5 = guest_list.pop(0)
print(f'Sorry, {popped_5.title()}, I can no longer invite you to the party.')

print('\nNelson and Sally are still attending')

count = 0
for guest in guest_list:
    count = count + 1
    message = f'Hello {guest.title()}, you are still invited to my dinner party!'
    print(message)
    if count == 3:
        break

del guest_list[0]
del guest_list[0]

print(f'\nHere is the empty guest list:{guest_list}.')