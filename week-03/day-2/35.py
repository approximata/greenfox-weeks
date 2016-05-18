# create a function that returns it's input factorial

import math

def factorMate(n):
    for i in range(n, 1, -1):
        n *= i-1
    return n

print(factorMate(5))


def test(actual, expected):
    if expected == actual:
        print('check')
    else:
        print('jaj')

print(math.factorial(100))
test(math.factorial(100), factorMate(100))
