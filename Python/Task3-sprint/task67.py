from collection import list_to_str
from task65 import f


def fib_sequence():

    n = int(input('n= '))
    res = [f(i) for i in range(n + 1)]
    return print(list_to_str(res, ','))

fib_sequence()