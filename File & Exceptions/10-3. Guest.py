"""Program that prompts the user for their name.
When the suer responds, their name is add to a txt file."""

filename = 'text_files/guest.txt'

with open(filename, 'a') as file_object:
    prompt = input("Enter your full name: ")
    file_object.write(prompt)
    



