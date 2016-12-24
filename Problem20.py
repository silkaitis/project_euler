'''
n! = n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10!
is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
import math

if __name__ == '__main__':
    soln = sum([int(x) for x in list(str(math.factorial(100)))])

    print('10! digits sum to {}'.format(soln))
