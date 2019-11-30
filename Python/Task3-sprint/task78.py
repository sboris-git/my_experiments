import random

def rnd_n(start, end, elements):
    '''Question 78
    Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.'''
    lst = [i / 100 for i in range(start*10, (end+1)*10)]  # extending range to float
    lst_random = ['{:.2f}'.format(random.choice(lst)) for i in range(elements)]
    return lst_random


print(rnd_n(100, 200, 5))