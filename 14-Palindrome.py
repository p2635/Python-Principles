# Palindrome
# A string is a palindrome when it is the same when read backwards.
# Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.

def palindrome(string):
    
    reverse = ""
    
    for i in reversed(string):
        reverse += i
    
    if string == reverse:
        return True
    else:
        return False

# Should be false        
print(palindrome("bobb"))

# Should be true        
print(palindrome("bobb"))
