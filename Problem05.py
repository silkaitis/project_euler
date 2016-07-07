# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:30:18 2016

@author: Danius.silkaitis
"""

#Problem 5
#2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all 
#of the numbers from 1 to 20?

i = 0
sol = 0
while sol == 0:
    j = 0
    for x in range(1,21):
        if i % x == 0:
            j += 1
    if j == 20:
        sol = i
    i += 10