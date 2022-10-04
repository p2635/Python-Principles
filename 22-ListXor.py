# List xor
# Define a function named list_xor. Your function should take three parameters: n, list1 and list2.
# Your function must return whether n is exclusively in list1 or list2.
# In other words, if n is in both lists or in none of the lists, return False. If n is in only one of the lists, return True.

def list_xor(n, list1, list2):
    # if count is exactly 1 then return true, else false
    if(list1.count(n) > 0 and list2.count(n) == 0):
        return True
    elif(list1.count(n) == 0 and list2.count(n) > 0):
        return True
    else:
        return False
    
# Tests
test1 = list_xor(1, [1, 2, 3], [4, 5, 6])
test2 = list_xor(1, [0, 2, 3], [1, 5, 6])
test3 = list_xor(1, [1, 2, 3], [1, 5, 6])
test4 = list_xor(1, [0, 0, 0], [4, 5, 6])

print(test1)
print(test2)
print(test3)
print(test4)