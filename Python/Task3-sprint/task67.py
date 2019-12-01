from modul import list_to_str
from task65 import f


def fib_sequence():

    n = int(input('n= '))
    res = [f(i) for i in range(n + 1)]
    return list_to_str(res, ',')

print(fib_sequence())