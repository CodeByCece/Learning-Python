#practice questions
#3-4. guest list and 3.5 changing guest list
guest_list = ['Chantal', 'Brandon', 'Mark', 'Emily']
count = 0
for i in guest_list:
    count = count + 1
    message = f'Hello {i}, you are invited to my dinner party!'
    print(message)
    if count == 4:
        break

#3-5 changing guest list
print(f'\nEmily can no longer attend the dinner.\n')
del guest_list[3]
guest_list.insert(3, 'Nelson')
print('Here are the updated invitationals')
count = 0
for friend in guest_list:
    count = count + 1
    message = f'Hello {friend}, you are invited to my dinner party!'
    print(message)
    if count == 4:
        break
#3-6 More Guests
print('\nThe resturant has informed me a bigger table is available')
guest_list.insert(0, 'Mary')
guest_list.insert(3, 'Hillary')
guest_list.append('Sally')

print('\nHere is the updated guest list')
print(guest_list)

#3-7 Shrinking guest list
print('\nThe bigger table will not be available in time. I can invite only 2 people.')
popped_1 = guest_list.pop(0)
print(f'\nSorry, {popped_1}, I can no longer invite you to the party.')
popped_2 = guest_list.pop(0)
print(f'Sorry, {popped_2}, I can no longer invite you to the party.')
popped_3 = guest_list.pop(0)
print(f'Sorry, {popped_3}, I can no longer invite you to the party.')
popped_4 = guest_list.pop(0)
print(f'Sorry, {popped_4}, I can no longer invite you to the party.')
popped_5 = guest_list.pop(0)
print(f'Sorry, {popped_5}, I can no longer invite you to the party.')

print('\nNelson and Sally are still attending')

count = 0
for int in guest_list:
    count = count + 1
    message = f'Hello {int}, you are still invited to my dinner party!'
    print(message)
    if count == 3:
        break

del guest_list[0]
del guest_list[0]

print(f'\nHere is the final guest list:{guest_list}.')
