"""Program that contains a list with a series of short text messages
and  Pass the list to a function called show_messages(), which prints each text message."""

def show_messages(messages):
    """Accepts list of short text messages and displays each one"""
    for message in messages:
        print(message)

# Create a list containing short text messages
short_txt = ['lol', 'ttyl', 'wyd', 'gtg', 'lmao', 'hiya', 'cyl']

text = show_messages(short_txt)
