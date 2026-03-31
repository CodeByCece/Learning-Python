"""Utilizing sending messages.py, this program uses a function called send_messages() 
that prints each text message and moves each message to a new list called sent_messages 
as it’s printed."""

def show_messages(messages):
    """Accepts list of short text messages and prints each one"""
    for message in messages:
        print(f"Message displayed: {message}")

def send_messages(short_txt, sent_messages):
    """prints each text message and moves each message to a new list (sent 
    messages list) as it's printed."""
    while short_txt:
        current_msg = short_txt.pop()
        print(f"Messages sent: {current_msg}")
        sent_messages.append(current_msg)


short_txt = ['lol', 'ttyl', 'wyd', 'gtg', 'lmao', 'hiya', 'cyl']
sent_messages = [] 

show = show_messages(short_txt)
text = send_messages(short_txt, sent_messages)

print(f"\nOriginal text messages: {short_txt}")
print(f"Messages recently sent: {sent_messages}")
