def tuple_square(a, b):
    a = tuple(i * i for i in range(a, b + 1))
    return a

print(tuple_square(1, 20))