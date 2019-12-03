def tuple_even(tup):

    a = tuple(i for i in range(len(tup) + 1) if i % 2 == 0)

    return a


tup = (1,2,3,4,5,6,7,8,9,10)
print(tuple_even(tup))