def half_tuple_print(a):
    half_len_a = len(a)//2
    print('{}\n{}'.format(a[:half_len_a],a[half_len_a:]))
    return

tup = (1,2,3,4,5,6,7,8,9,10)
half_tuple_print(tup)