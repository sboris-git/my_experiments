import random
from collection import list_to_str


def rnd_35(start, end, elements):
    '''Question 80
    Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 ,
    between 1 and 1000 inclusive.'''

    lst = [i / 100 for i in range(start * 100, (end + 1) * 100) if i % 35 == 0]
    lst_random = [random.choice(lst) for i in range(elements)]
    ans = list_to_str(lst_random, ', ')
    return ans


print(rnd_35(1, 1000, 5))
