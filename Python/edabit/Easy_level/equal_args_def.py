def equal(a, b, c):
    list_arg = [a, b, c]
    set_args = set(list_arg)
    quantity = 0
    for elem in set_args:
        n = list_arg.count(elem)
        if n > 1: quantity = n  # quantity.append(n)
        print('{} elem {}'.format(n, elem))
    print('number of equals {}'.format(quantity))

    return quantity


# edabit variants
def equal_1(a, b, c):
    l = [a,b,c]
    m = max(l.count(a),l.count(b),l.count(c))
    if m == 1: m = m-1
    return m


def equal_2(a, b, c):
    return {3:0,2:2,1:3}[len({a,b,c})]


from collections import *
def equal_3(*a):
    return sum(v for v in Counter(a).values() if v > 1)


def equal_4(a, b, c):
    l = [a,b,c]
    m = max(l.count(a),l.count(b),l.count(c))
    if m == 1: m = m-1
    return m

print(equal(2,  1, 0))
print(equal(5,  1, 5))
print(equal(5,  5, 5))
print(equal(0,  0, 0))
print(equal(0,  5, 0))
print(equal(0,  0, 5))



