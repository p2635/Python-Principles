# Consecutive zeros
# The goal of this challenge is to analyze a binary string consisting of only zeros and ones.
# Your code should find the biggest number of consecutive zeros in the string.

def consecutive_zeros(binary):
    # First we split the string using 1 as the delimiter
    split = binary.split("1")
    # Then we get the longest one with zeros
    # and also count how long it is after
    return len(max(split))
    
# This string should return 3
test = "1001101000110"
print(consecutive_zeros(test))