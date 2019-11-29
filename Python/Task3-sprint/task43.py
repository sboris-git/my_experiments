def tuple_even(tup):

    a = tuple(i * i for i in range(len(tup) + 1) if i%2==0)
    return a

print(tuple_square(1, 20))

tup = (1,2,3,4,5,6,7,8,9,10)
half_tuple_print(tup)