"""Working with one of the programs from Exercises 3-4
through 3-7 (page 42), use len() to print a message indicating the number
of people you are inviting to dinner."""

guest_list = ['mark', 'brandon', 'jim', 'emily']
count = 0
for guest in guest_list:
    count = count + 1
    message = f'Hello {guest.title()}, you are invited to my dinner party!'
    print(message)
    if count == 4:
        break

print(f"\nI am offically inviting {len(guest)} people to the dinner party. ")
