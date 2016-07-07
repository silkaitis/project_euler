# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:37:41 2016

@author: Danius.silkaitis
"""

#Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?

import numpy
val = 3
primes=numpy.array([2])
while len(primes) < 10001:
    if min(val % primes) != 0:
        primes = numpy.append(primes,[val])
    val += 1

print primes[len(primes)-1]