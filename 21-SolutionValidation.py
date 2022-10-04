# Solution validation
# The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.
# Write a function named validate that takes code represented as a string as its only parameter.
# https://pythonprinciples.com/challenges/Solution-validation/

def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    # is this meant to search for exact pairs of parens?
    if ("(" not in code) and (")" not in code):
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if  "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    else:
        return True
