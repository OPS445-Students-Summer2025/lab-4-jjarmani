#!/usr/bin/env python3
'''
Lab 4 Investigation 2 Part 2 
Create a Python script to validate user input
'''
# Author ID: 170543235
# Author Name: Sing Man Wong

def is_digits(sobj):
    # place code here - loop through each character in sobj 
    for local_item in sobj:
        if local_item < '0' or local_item > '9':
            return False
        # if int(local_item) == False:
        #     return False
    return True

if __name__ == '__main__':
    # test_list = ['-12','1F','8503x','8503']
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')