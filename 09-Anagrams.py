# Anagrams
#
# Two strings are anagrams if you can make one from the other by rearranging the letters.
#
# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.
#

def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# This should return True
print(is_anagram("typhoon", "opython"))

# This should return False
print(is_anagram("Alice", "Bob"))