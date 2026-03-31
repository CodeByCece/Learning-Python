"""If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you would like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner."""

guest_list = ['mark', 'brandon', 'jim', 'emily']
count = 0
for guest in guest_list:
    count = count + 1
    message = f'Hello {guest.title()}, you are invited to my dinner party!'
    print(message)
    if count == 4:
        break