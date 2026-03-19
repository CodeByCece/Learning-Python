# 6-3 Glossary

skills = {
    'get( )' : "method that returns a value from dictionary in the case the key doesn't exist",
    'an if-elif-else statement' : "conditional statement that uses Boolean values to check one condition at a time",
    'append( )' : 'method to attach a new object to a list',
    'title ( )' : 'string method used to convert a string into title case',
    'range ( )' : ' range function allows you  to generate a series of integers'}

for key, value in skills.items():
    print(f"This past month I learned how to use {key} in Python.")
    print(f"For context, {key} is a {value}.\n")
    
