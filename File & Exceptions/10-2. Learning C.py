"""Program that reads a file and prints its contents three times."""
filename = 'text_files/learning_python.txt'
filename.replace('Python', 'C')


# Loop through file object by each line
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

