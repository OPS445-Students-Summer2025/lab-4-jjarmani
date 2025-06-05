#!/usr/bin/env python3
'''
Lab 4 Investigation 1 Part 3 
Create a Python Script for Managing Dictionaries
'''
# Author ID: 170543235
# Author Name: Sing Man Wong

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
#accepts two lists as arguments keys and values, combines these lists together to create a dictionary (Tip: use a while loop to access elements in both the keys and values lists at the same time)
#returns a dictionary that has the keys and associated values from the lists
    result = {}
    i = 0
    while i < len(keys) and i < len(values):
        result[keys[i]] = values[i]
        i += 1
    return result

def shared_values(dict1, dict2):
#accepts two dictionaries as arguments and finds all values that are shared between the two dictionaries (Tip: generate sets containing only values for each dictionary, then use a function mentioned in a previous section to store the values that are common to both lists)
#returns a set containing ONLY values found in BOTH dictionaries
    set1 = set(dict1.values())
    set2 = set(dict2.values())
    return set1 & set2  # intersection of values


if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)