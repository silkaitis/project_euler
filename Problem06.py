# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:36:09 2016

@author: Danius.silkaitis
"""
#Problem 6
#The sum of the squares of the first ten natural numbers is,
#
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)^2 = 552 = 3025

#Hence the difference between the sum of the squares of the first 
#ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

SumSq = pow(sum(range(1,101)),2)
SqSum = 0
for x in range(1,101):
    SqSum = SqSum + pow(x,2)
print SumSq - SqSum