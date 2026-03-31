"""Utilizing Archived message.py this program uses the send_messages()
 with a copy of the list of messages."""

def show_messages(messages):
    """Accepts list of short text messages and prints each one"""
    for message in messages:
        print(f"Message sent: {message}")

def send_messages(short_txt, sent_messages):
    """prints each text message and moves each message to a new list (sent 
    messages list) as it's printed."""
    while short_txt:
        current_msg = short_txt.pop()
        print(f"Message recently sent: {current_msg}")
        sent_messages.append(current_msg)


short_txt = ['lol', 'ttyl', 'wyd', 'gtg', 'lmao', 'hiya', 'cyl']
sent_messages = [] 

show = show_messages(short_txt)
text = send_messages(short_txt[:], sent_messages)

print(f"\nHere is the original test message list: {short_txt}")
print(f"Here are the messages that were sent: {sent_messages}")