import random


def rnd_35(start, end, elements):
    '''Question 80
    Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 ,
    between 1 and 1000 inclusive.'''

    lst = [i for i in range(start, end+1) if i % 35 == 0]  # how to extend range to float?
    lst_random = [random.choice(lst) for i in range(elements)]
    return lst_random


print(rnd_35(1, 1000, 5))
