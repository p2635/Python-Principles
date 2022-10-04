# Custom zip
# The built-in zip function "zips" two lists. Write your own implementation of this function.
# Define a function named zap. The function takes two parameters, a and b. These are lists.
# Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
# You may assume a and b have equal lengths.

def zap(a, b):
    # Two lists a and b, assume equal length
    # I think it's a loop to build a new list
    # Create a tuple and just add to list
    # The function returns a list, the list contains tuples
    zaplist = []
    for i in (range(len(a))):
        zaptup = (a[i], b[i])
        zaplist.append(zaptup)
    return zaplist

# The solution revealed a list comprehension version, so I want to try and implement a version of this

def zap2(a, b):
    # Return a list
    # The list contains tuples with exactly 2 values in them (one from a, one from b)
    return [(a[i], b[i]) for i in range(len(a))]
