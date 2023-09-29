"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(len(items) -1):
        items[i] = str(items[i])
        
    itemsSet = set(items)
    for item in itemsSet:
        frequencies[item] = items.count(item)
        

    return frequencies



print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4']))
