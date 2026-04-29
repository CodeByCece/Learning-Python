"""Program that reads a file and prints its contents three times."""
filename = 'text_files/learning_python.txt'
filename.replace('Python', 'C')

# Read and print entire file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

# Loop through file object by each line
with open(filename) as file_object:
    filename.replace('Python', 'C')
    for line in file_object:
        print(line.strip())

# Making a list of lines from a file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

