# 6-4 Glossary Part 2 exercise

skills = {
    'get( )' : "method that returns a value from dictionary in the case the key doesn't exist",
    'an if-elif-else statement' : "conditional statement that uses Boolean values to check one condition at a time",
    'append( )' : 'method to attach a new object to a list',
    'title( )' : 'string method used to convert a string into title case',
    'range( )' : ' range function allows you  to generate a series of integers',
    'del'       : 'used to remove a key-value pair from a dictionary',
    'value( )' : 'method to return a list of values w/o the keys',
    'set( )' : 'function that allows you to pull values from a dictionary without repetition',
    'keys( )' : 'method used to pull all keys from a dictionary',
    '.items( )' : 'method used to loop through dictionary',
}


for key, value in skills.items():
    print(f"This past month I learned how to use {key} in Python.")
    print(f"For context, {key} is a {value}.\n")
    
