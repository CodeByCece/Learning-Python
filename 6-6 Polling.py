# 6-6 Polling exercise

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



