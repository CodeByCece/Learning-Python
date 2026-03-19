#8-4 Large shirts

# Modify 8-3 code so that shirts are large by default
# Assign default values to message and size parameters
def make_shirt(size = 'large', message = 'I love Python'): 
    """make_shirt accepts a size and text of a message to be printed on the shirt."""
    print(f"I have a size {size.title()} t-shirt that says {message}!\n")

make_shirt() # function call creates a large shirt with the default message
make_shirt('medium') # Function call creates a medium shirt with the default message
make_shirt('small', 'I love C++') # Function call creates a small shirt with a different message



