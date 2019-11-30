def map_sqr(list_a):

    sqr = list(map(lambda x: x ** 2, list_a))

    return sqr

list_a = [1,2,3,4,5,6,7,8,9,10]
print(map_sqr(list_a))