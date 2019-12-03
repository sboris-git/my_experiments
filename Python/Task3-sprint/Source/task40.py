def list_square(a, b):

    list_a = [i * i for i in range(a, b + 1)]

    return list_a[5:]

print(list_square(1, 20))