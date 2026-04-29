"""program that continously asks why people like programming.
Each time someone enters a reason, it's added to a file
that stores all responses."""

filename = 'text_files/programming_poll.txt'

prompt = "\nEnter your reason why you like programming:"
prompt += "\nEnter 'quit' to end the program."
message = ''

while message != 'quit':
    message = input(prompt)
    with open(filename, 'a') as file_object:
        file_object.write(f"{message}\n")
        


