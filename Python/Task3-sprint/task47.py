def map_filt_sqr(list_a):

    sqr = list(map(lambda x: x ** 2, list(filter(lambda x: x%2==0, list_a))))

    return print(sqr)

list_a = [1,2,3,4,5,6,7,8,9,10]
map_filt_sqr(list_a)