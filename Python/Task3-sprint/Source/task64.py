def y(n):
    if n == 0:
        return 0
    return y(n-1) + 100

def cycle():
    n = int(input('n= '))
    res = [y(i) for i in range(n+1)]
    return res[-1]

print(cycle())
#  tasks 64-66 resonable to try decorating instead a cycle. ToDo