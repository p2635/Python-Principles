# Min-maxing
# Define a function named largest_difference that takes a list of numbers as its only parameter.
# Your function should compute and return the difference between the largest and smallest number in the list.

def largest_difference(numbers):
    diff = max(numbers) - min(numbers)
    return diff

# 92 -- 98 = 190
test_list = [1, 2, 5, 7, 30, -98, 92, 3, 1, 3]
# Should return 190
print(largest_difference(test_list))