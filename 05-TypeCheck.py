# Type Check (https://pythonprinciples.com/challenges/Type-check/)
# Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.
# For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

def only_ints(int1, int2):
    if type(int1) == int and type(int2) == int:
        return True
    else:
        return False
        
print(only_ints(2,'hello'))
print(only_ints(1, True))
print(only_ints("hello", 2))
