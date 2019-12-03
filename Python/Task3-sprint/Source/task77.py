import random


def rnd_35():
    '''Question 77
    Please write a program to output a random number,
    which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.'''

    even_random = random.choice([i / 100 for i in range(1100) if i % 35 == 0])  # extending range to float
    even_random = '{:.2f}'.format(even_random)

    return even_random


print(rnd_35())