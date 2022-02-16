# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:19:54 2022

@author: roryc

Program to identify all the even fibonnaci numbers below 4,000,000 and sum
them all together.

~~~~~~~~ Project Euler Challenge 2 ~~~~~~~~
"""

def next_fib_pair(n):
    # Function to calculate the next pair of fibonacci sequence numbers with
    # an even number
    next_even_pair = (3*n[0] + 2*n[1], 2*n[0] + n[1])
    return next_even_pair

# Define tuple of starting fibonacci sequence numbers and the total sum
fibonacci_pair = (2,1)
total_sum = 0

while( fibonacci_pair[0] < 4000000 ):
    total_sum += fibonacci_pair[0]
    fibonacci_pair = next_fib_pair(fibonacci_pair)
    
print("Total sum of even fibonnaci numbers under 4000000 =", total_sum)