"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    for i in range(len(items)):
        items[i] = str(items[i])   
        
    itemsSet = set(items)
    for item in itemsSet:
        frequencies[item] = items.count(item)
        

    return frequencies



