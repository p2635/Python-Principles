# Thousands separator
# Write a function named format_number that takes a non-negative number as its only parameter.
# Your function should convert the number to a string and add commas as a thousands separator.
# For example, calling format_number(1000000) should return "1,000,000".
#
# For god's sake, I realized after solving this challenge,
# there is a built-in function 'return "{:,}".format(n)''
def format_number(num):
    
    # Check if the number is more than zero
    if(num < 0):
        return "Error, this function does not take negative numbers."
        
    # Convert int to a list of characters
    string = list(str(num))
    
    # Iterate over the list and insert a comma at the right place
    for i in range(len(string)-3, 0, -3):
        string.insert(i, ",")
    
    # Rebuild the string and return it
    result="".join(str(elem) for elem in string)
    return result

print(format_number(-3)) # this should fail
print(format_number(0)) # this should be ok
print(format_number(1000)) # this should add a comma
print(format_number(1292193102)) # this should print 1,292,193,102
