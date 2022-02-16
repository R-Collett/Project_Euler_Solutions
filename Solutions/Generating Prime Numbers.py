# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:19:54 2022

@author: roryc

All prime numbers satisfy the condition that they are equal to 6n+1 or 6n-1. But how can we use
these identities to generate primes instead? #

This is a test of my hypothesis, that if n satisfies the condition that (n-1)/5 or (n-1)/7 is an integer number,
then that calculation of 6n-1/6n+1 respectively is not a prime number.

This is accurate up to 323, where factors of 19 mess it all up!

The shortcomings of this algorithm, present themselves as the multiples of prime numbers, which we would have to check separately. To further this algorithm beyond
this limit, we would have to check whether each number is divisble by the prime numbers established before it. This is laborious, and I don't require it for my
uses, as I'm looking for prime numbers below 20.

~~~~~~~~ Personal Challenge to Generate Prime Numbers ~~~~~~~~
"""

#Let's try and generate all the prime numbers up to 100.

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

print(generate_primes_to(20))