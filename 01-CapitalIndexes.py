# Capital indexes (https://pythonprinciples.com/challenges/Capital-indexes/)
#
# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters. For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(str):
    # loop through string and apply isupper
    # if isupper is true, append to the index to a list
    caplist = []
    for i in range(len(str)):
        if str[i].isupper():
            caplist.append(i)
        else:
            pass
    return caplist
    
print(capital_indexes("heLlO"))
