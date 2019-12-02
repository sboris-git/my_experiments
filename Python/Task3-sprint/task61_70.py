def text_to_unicode(text):
    '''Reads an ASCII string and converts it to a unicode string encoded by utf-8.'''
    text.decode('UTF-8')
    return text.encode('UTF-8')


text = 'hello word'
print(text_to_unicode(text))
# print(text_to_unicode.__doc__)
# print(u'string')

# ******************************************************
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Question 62 ????
# Write a special comment to indicate a Python source code file is in unicode.

# You could provide the Unicode prefix when formatting:
#
# print(u"Writers: {}".format(writers))

# ******************************************************
def calc(n):
    '''Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

    Example:
        If the following n is given as input to the program:
            5
        Then, the output of the program should be:
            3.55
        In case of input data being supplied to the question, it should be assumed to be a console input.'''

    # n = int(input('type n: '))
    sum = 0.0

    for number in range(1, int(n) + 1):
        sum += float(number / (number + 1))

    return round(sum, 2)


print(calc(5))

# ******************************************************
def y(n):
    if n == 0:
        return 0
    return y(n-1) + 100

def cycle():
    n = int(input('n= '))
    res = [y(i) for i in range(n+1)]
    return res[-1]

print(cycle())

# ******************************************************
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 1)+f(n - 2)

def cycle(n):
    # n = int(input('n= '))
    res = [f(i) for i in range(n + 1)]
    return res[-1]


if __name__ == '__main__':
    print(cycle(5))

# ******************************************************
def cycle(n):
    # n = int(input('n= '))
    res = [f(i) for i in range(n + 1)]
    return res[-1]

# ******************************************************
from modul import list_to_str

def fib_sequence(n):

    # n = int(input('n= '))
    res = [f(i) for i in range(n + 1)]
    return list_to_str(res, ',')

print(fib_sequence(n))
# ******************************************************
def even_num_gen(n):
    i = 0
    while i <= n:
        if i%2 == 0:
            yield i
        i += 1

def cycle(n):
    # n = int(input('n: '))
    lst = []
    [lst.append(str(num)) for num in even_num_gen(n)]

    return list_to_str(lst, ',')


print(cycle())

# ******************************************************
'''Question 69
    Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

    Example:
        If the following n is given as input to the program:
            100
        Then, the output of the program should be:
            0,35,70'''


def num_gen(n):
    i = 0
    while i <= n:
        if i % 5 == 0 and i % 7 == 0:  # i % 35 == 0
            yield i
        i += 1


def cycle(n):
    # n = int(input('n: '))
    lst = []
    [lst.append(str(num)) for num in num_gen(n)]

    return list_to_str(lst, ',')


print(cycle())

# ******************************************************
def assert_data(data):

    for x in data:
        assert x % 2 == 0, "{} is an odd number".format(x)
    return


data = [2, 4, 5, 6]
assert_data(data)

