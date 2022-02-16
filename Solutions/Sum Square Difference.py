# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 18:07:22 2022

@author: roryc

~~~~~~~~ Project Euler Challenge 6 ~~~~~~~~

The sum of the squares of the first ten natural numbers is 385
The square of the sum of the first ten natural numbers is 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import numpy as np

number_array = np.array(range(1, 455 + 1, 1))
sum_of_square = 0
square_of_sum = 0

for x in number_array:
    sum_of_square += x**2
    square_of_sum += x

square_of_sum = square_of_sum**2

print(square_of_sum - sum_of_square)