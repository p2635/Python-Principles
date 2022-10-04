# Double letters (https://pythonprinciples.com/challenges/Double-letters/)
# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

def double_letters(string):
    for i in range(len(string)):
        if(string[i] == string[i-1]):
            return True
    return False
        
print(double_letters("hello"))
print(double_letters("helo"))