# -*- coding: utf-8 -*-
"""Dictionary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12GSL3evYXpF4sti6uFqxyYoOYynH6NKH
"""

# 1. Write a  Python script to sort (ascending and descending) a dictionary by value.
def sort_dict_by_value(d, ascending=True):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))
    return sorted_dict

example_dict = {'d': 4, 'e': 6, 'f': 5}

sorted_dict_asc = sort_dict_by_value(example_dict)
print(sorted_dict_asc)

sorted_dict_desc = sort_dict_by_value(example_dict, ascending=False)
print(sorted_dict_desc)

# 2. Write a Python script to add a key to a dictionary.
def add_key_to_dict(d, key, value):
    d[key] = value
    return d

sample_dict = {0: 10, 1: 20}
new_key = 2
new_value = 30

result = add_key_to_dict(sample_dict, new_key, new_value)
print("Expected Result:", result)

# 3. Write a  Python script to concatenate the following dictionaries to create a new one.
def concatenate_dicts(*dicts):
    concatenated_dict = {}
    for d in dicts:
        concatenated_dict.update(d)
    return concatenated_dict

dict1 = {1: 'a', 2: 'b'}
dict2 = {3: 'c', 4: 'd'}
dict3 = {5: 'e', 6: 'f'}

concatenated_dict = concatenate_dicts(dict1, dict2, dict3)
print("Concatenated Dictionary:", concatenated_dict)

# 4. Write a Python script to check whether a given key already exists in a dictionary.
def check_key_in_dict(d, key):
    return key in d

sample_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'c'

if check_key_in_dict(sample_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

# 5. Write a Python program to iterate over dictionaries using for loops.
sample_dict = {'a': 1, 'b': 2, 'c': 3}

print("Iterating over keys:")
for key in sample_dict:
    print(key)

print("\nIterating over values:")
for value in sample_dict.values():
    print(value)

print("\nIterating over key-value pairs:")
for key, value in sample_dict.items():
    print(key, "->", value)

# (6) 8. Write a  Python script to merge two Python dictionaries.
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)

# (7) 15. Write a Python program to get the maximum and minimum values of a dictionary.
sample_dict = {'a': 33, 'b': 40, 'c': 13, 'd': 10}

max_value = max(sample_dict.values())
min_value = min(sample_dict.values())

print("Maximum value:", max_value)
print("Minimum value:", min_value)

# (8) 10. Write a Python program to sum all the items in a dictionary.
def return_sum(dict):
    return sum(dict.values())

dict = {'a': 1, 'b': 2, 'c': 3}
print("Sum :", return_sum(dict))

# (9) 11. Write a Python program to multiply all the items in a dictionary.
d = {
    'a': 1,
    'b': 2,
    'c': 3,
}

x = 1

for i in d:
    x = x*d[i]

print(x)

# (10) 12. Write a  Python program to remove a key from a dictionary.
dict = {"A":1,"B":2,"C":3}
del dict['B']
print("Dictonary after removal:", dict)

# (11) 61. Write a Python program to count the frequency of a dictionary.
from collections import Counter

original_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

frequency_counter = Counter(original_dict.values())

print("Count the frequency of the dictionary:")
print(frequency_counter)

# (12) 65. Write a Python program to get the total length of all values in a given dictionary with string values.
def total_length_of_values(d):
    total_length = sum(len(value) for value in d.values() if isinstance(value, str))
    return total_length

original_dict = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

total_length = total_length_of_values(original_dict)
print("Total length of all values of the dictionary with string values:", total_length)

# (13) 37. Write a Python program to replace dictionary values with their sums.
def replace_with_sum(d):
    for key, value in d.items():
        if isinstance(value, list):
            d[key] = sum(value)
    return d

sample_dict = {'a': [1, 2, 3], 'b': 2, 'c': [4, 5], 'd': 'string'}

modified_dict = replace_with_sum(sample_dict)
print("Modified Dictionary with sums:")
print(modified_dict)

# (14) 34. Write a Python program to count the number of items in a dictionary value that is a list.
def count_list_items(d):
    count = 0
    for value in d.values():
        if isinstance(value, list):
            count += len(value)
    return count

sample_dict = {'a': [1, 2, 3], 'b': 2, 'c': [4, 5], 'd': 'string'}

num_list_items = count_list_items(sample_dict)
print("Number of items in dictionary values that are lists:", num_list_items)

# (15) 33. Write a Python program to check if multiple keys exist in a dictionary.
def check_keys_exist(d, keys):
    return all(key in d for key in keys)

sample_dict = {'a': 1, 'b': 2, 'c': 3}

keys_to_check = ['a', 'b', 'd']

if check_keys_exist(sample_dict, keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")

# (16) 32. Write a Python program to print a dictionary line by line.
sample_dict = {'a': 1, 'b': 2, 'c': 3}

print("The dictionary line by line:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")

# (17) 31. Write a  Python program to get the key, value and item in a dictionary.
sample_dict = {'a': 1, 'b': 2, 'c': 3}

print("Iterating over the dictionary:")
for key, value in sample_dict.items():
    print("Key:", key)
    print("Value:", value)
    print("Item (key-value pair):", (key, value))

# (18) 29. Write a Python program to remove spaces from dictionary keys.
def remove_spaces_from_keys(d):
    return {key.replace(' ', ''): value for key, value in d.items()}

sample_dict = {'maths physics': 10, 'art pe': 20, 'english spanish': 30}

result = remove_spaces_from_keys(sample_dict)
print("Dictionary after removing spaces from keys:")
print(result)

# (19) 28. Write a Python program to sort a list alphabetically in a dictionary.
def sort_list_in_dict(d):
    sorted_dict = {key: sorted(value) for key, value in d.items()}
    return sorted_dict

sample_dict = {'b': ['maths', 'physics', 'biology'], 'a': ['english', 'spanish', 'pe']}

sorted_dict = sort_list_in_dict(sample_dict)
print("Dictionary with sorted lists:")
print(sorted_dict)

# (20) 27. Write a Python program to convert a list into a nested dictionary of keys.
def list_to_nested_dict(keys_list, value):
    if len(keys_list) == 1:
        return {keys_list[0]: value}
    else:
        return {keys_list[0]: list_to_nested_dict(keys_list[1:], value)}

keys_list = ['a', 'b', 'c']
value = 1

nested_dict = list_to_nested_dict(keys_list, value)
print("Nested Dictionary:", nested_dict)