"""Cleaned up code from Exercise 6-3 by replacing series of print()
calls with a loop that runs through the dictionary’s keys and values. When
the loop works, add five more Python terms to the glossary.
When you run your program again, these new words and meanings should
automatically be included in the output."""

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
    print(f"{key}: {value}")
    
    
