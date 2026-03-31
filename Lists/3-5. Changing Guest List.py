"""You just heard that one of your guests can not make the
dinner, so you need to send out a new set of invitations. You will have to think of
someone else to invite.
•   Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can not make it.
•    Modify your list, replacing the name of the guest who can not make it with
the name of the new person you are inviting.
•   Print a second set of invitation messages, one for each person who is still
in your list."""

guest_list = ['mark', 'brandon', 'jim', 'emily']

print(f'Emily can no longer attend the dinner.')
del guest_list[3]
guest_list.insert(3, 'Nelson')
print('So, here are the updated invitationals...\n')
count = 0
for guest in guest_list:
    count = count + 1
    message = f'Hello {guest.title()}, you are invited to my dinner party!'
    print(message)
    if count == 4:
        break