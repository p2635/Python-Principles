# Boolean and
# Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
#
# Isn't this similar to the all() function?
# Reference from w3schools: https://www.w3schools.com/python/ref_func_all.asp
#
def triple_and(par1, par2, par3):
    return par1 and par2 and par3
    
# This should return true
test = triple_and(True, True, True)
print(test)
# This should return false
test = triple_and(True, False, True)
print(test)
