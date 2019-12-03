import itertools


def perm(lst):
    '''Question 99
    Please write a program which prints all permutations of [1,2,3]'''

    per = list(itertools.permutations(lst))

    return per


lst = [1, 2, 3]
print(perm(lst))