# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:58:16 2022

@author: roryc

~~~~~~~~ Project Euler Challenge 3 ~~~~~~~~

Find the largest prime factor of 600851475143 
"""

import math
import numpy as np

N = 600851475143
array_of_factors = np.array(1, dtype='int64')


N_copy = N
starting_point = 2
number_array = np.array(range( starting_point, math.floor(N_copy/100000), 1) )
for x in number_array:
    if(N_copy % x == 0):
        print("Factor found = ", x)
        N_copy = N_copy/x
        array_of_factors = np.append(array_of_factors, [x])
        starting_point = x
    if(N_copy == 1):
        break

multiplication = 1
for j in range( np.size(array_of_factors) ):
    multiplication = multiplication * array_of_factors[j]

if(N == multiplication):
    print("Prime Factorisation Successful!!")



print("Largest Prime Factor is of ", N, "is", np.sort(array_of_factors)[np.size(array_of_factors)-1])