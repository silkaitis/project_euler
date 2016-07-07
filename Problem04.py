# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 09:39:53 2016

@author: Danius.silkaitis
"""
#Problem 4
#A palindromic number reads the same both ways. The largest palindrome made 
#from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

max = 999*999
sol = 0
for i in range(9,0,-1):
    for j in range(9,-1,-1):
        for k in range(9,-1,-1):
            pal = i*(1e5+1e0) + j*(1e4+1e1) + k*(1e3+1e2)
            if pal < max:
                for p in range(9,0,-1):
                    for q in range(9,-1,-1):
                        for r in range(9,-1,-1):
                            var = p*1e2 + q*1e1 + r*1e0
                            if pal % var == 0:
                                if pal / var < 1e3:
                                    if pal > sol:
                                        sol = pal

print sol