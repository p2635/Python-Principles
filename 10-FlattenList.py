# Flatten Lists
# Write a function that takes a list of lists and flattens it into a one-dimensional list.
# Name your function flatten. It should take a single parameter and return a list.

def flatten(lists):
    flattened = []
    # For each list in the list of lists
    for i in lists:
        # Add that value to the flattened list
        for j in i:
            flattened.append(j)
    # Finally return the new list
    return flattened

# This list of lists...
test = [[1,2],[3,4]]
# Should return the list: [1, 2, 3, 4]
print(flatten(test))