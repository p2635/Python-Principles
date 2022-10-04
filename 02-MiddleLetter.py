# Middle letter (https://pythonprinciples.com/challenges/Middle-letter/)
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".
# Got some help from https://www.programiz.com/python-programming/examples/odd-even

def mid(str):
    if(len(str) % 2) == 0:
        return ""
    else:
        midindex = (len(str)//2)
        return str[midindex]

print(mid("abc"))
