"""Modification of make_shirt() function so that shirts are large
by default with a message that reads default message I love Python. 
The Function is capable of printing a large shirt and a medium shirt 
with the default message, and a shirt of any size with a 
different message."""

def make_shirt(size = 'large', message = 'I love Python'): 
    """make_shirt accepts a size and text of a message to be printed on the shirt."""
    print(f"I have a size {size.title()} t-shirt that says {message}!\n")

make_shirt() # function call creates a large shirt with the default message
make_shirt('medium') # Function call creates a medium shirt with the default message
make_shirt('small', 'I love C++') # Function call creates a small shirt with a different message



