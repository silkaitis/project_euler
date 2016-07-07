# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:19:20 2016

@author: Danius.silkaitis
"""

#Problem 03
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?
def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n <= 1:
        return False
        
    sqr = int(pow(n,0.5)) + 1
    for t in range(3,sqr):
        if n % t == 0:
            return False  
    return True

Target = 600851475143
Sqr = int(pow(Target,0.5))+1
for t in range(1,Sqr):
    if is_prime(t):
        if Target % t == 0:
            PFact = t
print PFact