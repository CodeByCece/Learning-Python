"""Program with a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the 
sandwichthat’s being ordered."""

def sandwich_order(bread, *other):
    """Accepts a list of items for a sandwich order."""
    print(f"Make a {bread} sandwich with the following items:")
    print(f"- {other}\n")

sandwich_order('sourdough','mayo', 'lettuce', 'tomato', 'turkey', 'cheddar cheese' )
sandwich_order('pita', 'kebab', 'white sauce', 'lettuce' )
sandwich_order('wheat', 'mayo', 'ham', 'swiss cheese', 'lettuce')
    

