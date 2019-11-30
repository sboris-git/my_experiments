def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1)+f(n-2)

def cycle():
    n = int(input('n= '))
    res = [f(i) for i in range(n+1)]
    return res[-1]


if __name__ == '__main__':
    print(cycle())
