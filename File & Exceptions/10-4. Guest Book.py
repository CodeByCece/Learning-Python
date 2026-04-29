filename = 'text_files/guest_book.txt'
prompt = "\nEnter your full name:"
prompt += "\nEnter 'quit' to end the program."
message = ''

while message != 'quit':
    message = input(prompt)
    with open(filename, 'a') as file_object:
        file_object.write(f"{message}\n")
        print(f"Welcome {message}.")
        


