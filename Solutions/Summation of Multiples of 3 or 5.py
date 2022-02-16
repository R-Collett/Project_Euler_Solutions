# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:00:10 2022

@author: roryc

Program to identify the summation of all multiples of 3 OR 5, but not both, up to 1000

~~~~~~~~ Project Euler Challenge 1 ~~~~~~~~
"""

import math

def sum_of(input_array_size, multiple):
    return multiple*input_array_size*(input_array_size+1)/2

# Define which number to do the multiple of and how many there are up to 1000
multiple_of_3 = 3
multiple_of_5 = 5
multiples_of_both = multiple_of_3 * multiple_of_5
number_of_multiples_3 = math.floor(1000/multiple_of_3)
number_of_multiples_5 = math.floor(1000/multiple_of_5)-1
number_of_multiples_both = math.floor(1000/multiples_of_both)

total_sum = sum_of(number_of_multiples_3, 3) + sum_of(number_of_multiples_5, 5) - sum_of(number_of_multiples_both, 15)
    
print("Total sum of the multiples of 3 OR 5", "=", total_sum)