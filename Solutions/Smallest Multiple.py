# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 18:07:22 2022

@author: roryc

~~~~~~~~ Project Euler Challenge 5 ~~~~~~~~

2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

"""

import math
import numpy as np

def generate_primes_to(max_integer):
    # Keep arrays separate to remove the terms accorrding to conditions outlined in header of code.
    number_array_add = np.array(range( 1, math.floor(max_integer/6)+1, 1))
    number_array_subtract = np.array(range( 1, math.floor(max_integer/6)+1, 1))
    # For 6n+1 terms represented in number_array_add, every n value which satisfies (n-1)/7 = integer must be deleted.

    deletion_index = np.array([],dtype='int32')
    for n in number_array_subtract:
        if (( ((n+1)/7).is_integer() == True or ( ((n-1)/5).is_integer() == True and n-1 != 0) ) or ( ( (6*n - 1)%11 == 0 and (6*n - 1)!=11 ) or ((6*n - 1)%13 == 0 and (6*n - 1)!=13) ) ) or ( np.sqrt( 6*n - 1 ).is_integer() == True ):
            deletion_index = np.append(deletion_index, int(n-1))
    number_array_subtract = np.delete(number_array_subtract, deletion_index)

    deletion_index = np.array([],dtype='int32')
    for n in number_array_add:
        if (( ( ((n-1)/7).is_integer() == True and n-1 != 0 ) or ( (n+1)/5 ).is_integer() == True ) or ( ( (6*n + 1)%11 == 0 and (6*n + 1)!=11 ) or ((6*n + 1)%13 == 0 and (6*n + 1)!=13) )) or ( np.sqrt( 6*n + 1 ).is_integer() == True ):
            deletion_index = np.append(deletion_index, int(n-1))
    number_array_add = np.delete(number_array_add, deletion_index)

    total_prime_array = np.append(6*number_array_add + 1, 6*number_array_subtract - 1)
    total_prime_array = sorted(np.append(total_prime_array, [2, 3]))
    return total_prime_array

# Generating the primes does most of the heavy lifting, the next step just involves repeating the prime numbers until we exceed the limit. In this case, 20.

multiply_up_to = 20
prime_array = np.array(generate_primes_to(multiply_up_to))
other_factor_array = np.array([])

for x in prime_array:
    for i in range(2, math.floor(math.log2(multiply_up_to)) + 1, 1):
        if x**i <= multiply_up_to:
            other_factor_array = np.append(other_factor_array, x)
        else:
            break

minimum_factor_array = np.array(sorted(np.append(prime_array, other_factor_array)))
multiple_of_all = 1
print(minimum_factor_array)

for x in minimum_factor_array:
    multiple_of_all = multiple_of_all*x

print("minimum evenly divisible number by numbers 1->20 =", multiple_of_all)