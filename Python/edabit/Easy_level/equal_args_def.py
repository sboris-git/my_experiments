def equal(a, b, c):
    list_arg = [a, b, c]
    set_args = set(list_arg)
    print(set_args)
    quantity = []
    for elem in set_args:
        n = list_arg.count(elem)
        quantity.append(n)
        print('{} elem {}'.format(n, elem))
        # res = n if n != 1 else 0
    n = max
    if n == 1:
        res = 0
    elif n > 1:
        res = n

    return res


# print(equal(2,  1, 0))
# print(equal(5,  1, 5))
# print(equal(5,  5, 5))
print(equal(0,  0, 0))

print(equal(0,  5, 0))
print(equal(0,  0, 5))



