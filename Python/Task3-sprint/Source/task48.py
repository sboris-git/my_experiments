def filt_list():

    return list(filter(lambda x: x % 2 == 0, [i for i in range(1, 20 + 1)]))

print(filt_list())

