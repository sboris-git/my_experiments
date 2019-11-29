from collection import *

def factorial(n):

    if n == 1:
        return n
    else:
        return n*factorial(n-1)

in_str = input('Type a coma delimited numbers')
# in_str = '2, 4, 6, 8, 1'

numbers = [int(item) for item in in_str.split(',')]
print(list_to_str([factorial(item) for item in numbers], ', '))




