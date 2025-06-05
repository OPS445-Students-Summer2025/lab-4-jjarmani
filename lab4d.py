#!/usr/bin/env python3
# Strings 1
'''
Lab 4 Investigation 2 Part 1 
Create a Python Script Demostrating Substrings
'''
# Author ID: 170543235
# Author Name: Sing Man Wong

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(local_str:str):
    # Place code here - refer to function specifics in section below
    return local_str[0:5]

def last_seven(local_str:str):
    # Place code here - refer to function specifics in section below
    return local_str[-7:]

def middle_number(local_int:int):
    # Place code here - refer to function specifics in section below. Returns a string containing the second and third characters in the number
    local_str = str(local_int)
    return local_str[1:3]

def first_three_last_three(local_str1:str, local_str2:str):
    # Place code here - refer to function specifics in section below, Returns a single string that starts with the first three characters of argument1 and ends with the last three characters of argument2
    local_str_combined = local_str1[0:3] + local_str2[-3:]
    return local_str_combined

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))