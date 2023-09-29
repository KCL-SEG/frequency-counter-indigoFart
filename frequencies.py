"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    itemsSet = set(items)
    for item in itemsSet:
        frequencies[str(item)] = items.count(item or str(item))
        
    
           
            
        
           
            

    

    return frequencies

print(frequencies(["a", "b","a", "a", "b"]))
