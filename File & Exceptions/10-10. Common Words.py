"""program that counts the number of words or phrases
that appears in a string."""

def count_words(filename):
    """reads content of a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, {filename} does not exist.")
    else:
        words = file_contents.split()
        num_words = len(words)
        line = 'the'
        line.lower().count('the')
        print(f"The file {filename} has {num_words} words.")
        print(f"In this file the phrase 'the' shows up {line.lower().count('the')} time(s).\n")


filenames = ['text_files/book of nature myths.txt', 'text_files/winnie the pooh.txt', 'text_files/through the looking glass.txt']
for filename in filenames:
    count_words(filename)