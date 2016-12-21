'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
soln = [int(x) for x in list(str(pow(2, 1000)))]
print('Sum of the digits for 2^1000 is {}'.format(sum(soln)))
