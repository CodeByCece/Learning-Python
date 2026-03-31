"""Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output."""
skills = {
    'get( )' : "method that returns a value from dictionary in the case the key doesn't exist",
    'an if-elif-else statement' : "conditional statement that uses Boolean values to check one condition at a time",
    'append( )' : 'method to attach a new object to a list',
    'title ( )' : 'string method used to convert a string into title case',
    'range ( )' : ' range function allows you  to generate a series of integers'}

for skill in skills.items():
    print(skill)    
