def read_file(filename):
    """Reads files and prints contents of file."""
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(f"{filename} exists. Here is the contents of this file:")
        print(contents)

filenames = ['text_files/cats.txt', 'text_files/dogs.txt']
for filename in filenames:
    read_file(filename)

