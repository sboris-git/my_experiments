import random


def rnd_n():
    '''Question 81
    Please write a program to randomly print a integer number between 7 and 15 inclusive.'''

    n_random = random.choice([i for i in range(7, 16)])
    return n_random


print(rnd_n())