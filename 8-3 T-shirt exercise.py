# 8-3 T-shirt

def make_shirt(message, size):
    """make_shirt accepts a size and text of a message to be printed on the shirt."""
    print(f"I have a size {size.title()} t-shirt that says {message}!\n")

make_shirt('We Out - Rosa Parks', 'large') # Call function using positional arguments
make_shirt('We Out - Rosa Parks', size = 'medium') # Call function using keyword arguments


