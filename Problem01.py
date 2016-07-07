# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 09:11:13 2016

@author: Danius.silkaitis
"""

#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(m1,m2,ub):
    sum = 0
    for x in range(0,ub):
        if x % m1 == 0:
            sum = sum + x
        elif x % m2 == 0:
            sum = sum + x
    return(sum)

m1 = 3
m2 = 5
ub = 1000
sum = multiples(m1,m2,ub)
print sum