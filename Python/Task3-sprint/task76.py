import random


def rnd_even():
    '''Question 76
    Please write a program to output a random even number between 0 and 10 inclusive
    using random module and list comprehension.'''
    even_random = random.choice([i / 100 for i in range(1100) if i % 2 == 0]) # extending range to float
    even_random = '{:.2f}'.format(even_random)
    return even_random

print(rnd_even())