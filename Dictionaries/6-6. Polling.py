"""Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll. """

favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

candidates = ['sarah', 'jon', 'edward', 'jack', 'lionel', 'mark']

for name in candidates:
    if name in favorite_languages:
        print(f"{name.title()}, thank you for completing the poll.\n")
    else:
        print(f"{name.title()}, please take the poll at your earliest convienance.\n")



