# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 18:07:22 2022

@author: roryc

~~~~~~~~ Project Euler Challenge 4 ~~~~~~~~

Find the largest palindrome number made from the product of two three
digit numbers.  
"""

import numpy as np

def check_palindrome(input_number):
    # Function to identify whether input number is a palindrom number or not
    # Construct a string from input, since strings are subscriptable.
    string_of_number = str(input_number)
    for i in range(len(string_of_number)):
        if(string_of_number[i] != string_of_number[len(string_of_number) - 1 - i]):
            return False
    return True
    
array_of_palindromes = np.array([], dtype="int64")
for i in range(1, 1001):
    for j in range(1, 1001):
        if(check_palindrome( (1000000 - i)* (1000000 - j) ) == True):
            print("i,j = ", 1000000 - i, ",", 1000000 - j)
            print("Palindrom of i,j = ", (1000000 - i)* (1000000 - j))
            array_of_palindromes = np.append(array_of_palindromes, (1000000 - i)* (1000000 - j))
            
print("Largest Palindrome = ", np.sort(array_of_palindromes)[np.size(array_of_palindromes)-1])