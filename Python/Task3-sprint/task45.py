def filter_2(list_a):

    filt = list(filter(lambda x: x % 2 == 0, list_a))

    return print(filt)

list_a = [1,2,3,4,5,6,7,8,9,10]
filter_2(list_a)