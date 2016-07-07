# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:58:58 2016

@author: Danius.silkaitis
"""
#Problem 10
#
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.

import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

n=0
SPrime=0
while n < 2e6:
    if is_prime(n):
        SPrime = SPrime + n
    n += 1
    
print SPrime