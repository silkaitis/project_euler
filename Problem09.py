# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:09:44 2016

@author: Danius.silkaitis
"""
#Problem 9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

for a in range(0,1000):
    b = (a*2.0e3-1e6)/(2.0*a-2.0e3)
    if b.is_integer():
        c = pow(pow(a,2)+pow(b,2),0.5)
        if c.is_integer():
            if a < b < c and a+b+c == 1000:
                print a*b*c