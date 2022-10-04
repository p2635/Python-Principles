# All equal
# Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
# For example, calling all_equal([1, 1, 1]) should return True.

def all_equal(mylist):
    for x in mylist:
        for y in mylist:
            if x == y:
                pass
            else:
                return False
    return True
    
test = [1, 1, 1]
print(all_equal(test))
    
