# -*- coding: utf-8 -*-
"""List.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HlJjUG87nactL6XbtPf6ld70z3Y2Kz4p
"""

# 1. Write a  Python program to sum all the items in a list.
def sum_list(items):
  return sum(items)
print(sum_list([1, 2, -8]))

# 2. Write a Python program to multiply all the items in a list.
def multiply_list(items):
    thing = 1
    for x in items:
        thing *= x
    return thing

print(multiply_list([1, 2, 3, 4]))

# 3. Write a Python program to get the largest number from a list.
def max_list(items):
  return max(items)
print(max_list([1, 2, -8]))

# 4. Write a Python program to get the smallest number from a list.
def min_list(items):
    return min(items)
print(min_list([1,2,3]))

# 5. Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
def match_words(words):
    return sum(1 for word in words if len(word) > 1 and word[0] == word[-1])

print(match_words(['abc', 'xyz', 'aba', '1221']))

# 6. Write a Python program to get a list, sorted in increasing order by the last element
# in each tuple from a given list of non-empty tuples
def sort_list_tuples(tuples):
    return sorted(tuples, key=lambda x: x[-1])

print(sort_list_tuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# 7. Write a Python program to remove duplicates from a list.
def remove_duplicates(items):
    return list(set(items))

print(remove_duplicates([1,2,3,1,2,4,5]))

# 8. Write a Python program to check if a list is empty or not.
def is_list_empty(items):
    return not items

print(is_list_empty([]))
print(is_list_empty([1, 2]))

# 9. Write a Python program to clone or copy a list.
def clone_list(items):
    return items[:]

original_list = [1, 2, 3]
copied_list = clone_list(original_list)
print(copied_list)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def filter_long_words(words, n):
    return [word for word in words if len(word) > n]

print(filter_long_words(['hello', 'world', 'hi', 'name'], 3))

# (11) 21. Write a Python program to convert a list of characters into a string.
def list_to_string(char_list):
    string = ''.join(char_list)
    return string
char_list = ['a', 'z', 'c', 'x', 'y']
result_string = list_to_string(char_list)
print("List converted to string:", result_string)

# (12) 22. Write a Python program to find the index of an item in a specified list.
def find_index(lst, item):
    try:
        index = lst.index(item)
        return index
    except ValueError:
        return -1

# Example usage:
my_list = [1, 2, 3, 4, 5]
item_to_find = 3
index = find_index(my_list, item_to_find)
if index != -1:
    print(f"The index of {item_to_find} in the list is: {index}")
else:
    print(f"{item_to_find} is not present in the list.")

# (13) 37. Write a  Python program to find common items in two lists.
def find_common_items(list1, list2):
    common_items = []
    for item in list1:
        if item in list2:
            common_items.append(item)
    return common_items

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_items = find_common_items(list1, list2)
if common_items:
    print("Common items found in the lists:", common_items)
else:
    print("No common items found.")

# (14) 19. Write a Python program to calculate the difference between the two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
diff = list(set(list1) - set(list2))
print(diff)

# (15) 20. Write a Python program to access the index of a list.
my_list = [10, 20, 30, 40, 50]
for index, value in enumerate(my_list):
    print(index, value)

# (16) 23. Write a Python program to flatten a shallow list.
shallow_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in shallow_list for item in sublist]
print(flattened_list)

# (17) 24. Write a Python program to append a list to the second list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2.extend(list1)
print(list2)

# (18) 25. Write a Python program to select an item randomly from a list.
import random
my_list = [1, 2, 3, 4, 5]
random_item = random.choice(my_list)
print(random_item)

# (19) 26. Write a  Python program to check whether two lists are circularly identical.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 1, 2]
is_circular = ''.join(map(str, list1)) in ''.join(map(str, list2 * 2))
print(is_circular)

# (20) 27. Write a  Python program to find the second smallest number in a list.
my_list = [4, 5, 3, 2, 9, 8]
sorted_list = sorted(my_list)
second_smallest = sorted_list[1]
print(second_smallest)