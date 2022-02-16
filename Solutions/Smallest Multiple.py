# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 18:07:22 2022

@author: roryc

2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

~~~~~~~~ Project Euler Challenge 5 ~~~~~~~~
"""

import numpy as np

def find_prime_factors(input_integer):
    
    starting_point = 2
    number_array = np.array(range( starting_point, input_integer) )
    prime_factor_array = np.array([], dtype='int64')
    input_integer_copy = input_integer
    for x in number_array:
    
        if(input_integer_copy % x == 0):
            input_integer_copy = input_integer_copy/x
            prime_factor_array = np.append(prime_factor_array, [x])
            starting_point = x
        if(input_integer_copy == 1):
            break
    
    if( np.size( prime_factor_array ) == 0 ):
        np.append( prime_factor_array, input_integer )
        
    end = False
    while(end == False):
        
        new_size = np.size(prime_factor_array)
        old_size = 0
        for i in range(np.size(prime_factor_array)):
            for j in prime_factor_array:    
                if(prime_factor_array[i] % j == 0 and prime_factor_array[i] != j):
                    prime_factor_array = np.append(prime_factor_array, [j, (prime_factor_array[i]/j)])
                    prime_factor_array = np.delete(prime_factor_array, i)
                    old_size = np.size(prime_factor_array)
        if( old_size == new_size ):
            end = True
        
    return prime_factor_array

# N is the number up to which we are finding the smallest number evenly
# divisible by the positive integers below it.
N = 10
# Minimum factors require 2 and 3 minimum, so can always include these
minimum_factor_array = np.array([2,3], dtype="int64")

# Identify the prime factor decomposition of the next number
# Identify whether all of them are present in the minimum factors array,
# including whether they are repeated numbers.


print(find_prime_factors(16))


"""
Divide factors of number array by numbers preceding it in the array, 
finding the exact factors using the modulo operation.

Method goes as follows:
    - Establish whether next number can be constructed from the numbers
currently in the minimum factors
    - If it cannot, then add it to the list of minimum factors.


for i in range(2, N+1):
    potential_factor = i
    # Loop so we get full factor decomposition.
    while(potential_factor != 1):
        for j in np.size(minimum_factor_array):
            if( potential_factor % minimum_factor_array[j] == 0):
                for k in range(potential_factor, np.size(minimum_factor_array)):
                
"""         
    
    
        










