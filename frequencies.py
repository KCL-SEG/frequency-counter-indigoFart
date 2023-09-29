"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    stringItems = []
    for item in items:
        stringItems.append(str(item))
    itemsSet = set(stringItems)
    for item in itemsSet:
        frequencies[str(item)] = stringItems.count(item)
        

    return frequencies



print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4']))
