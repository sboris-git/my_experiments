def tuple_square(a, b):

    a = tuple(i * i for i in range(a, b + 1))

    return a

print(tuple_square(1, 20))

# **************************************************
def half_tuple_print(a):

    half_len_a = len(a)//2
    ans = '{}\n{}'.format(a[:half_len_a], a[half_len_a:])

    return ans

tup = (1,2,3,4,5,6,7,8,9,10)
print(half_tuple_print(tup))

# **************************************************
def tuple_even(tup):

    a = tuple(i for i in range(len(tup) + 1) if i % 2 == 0)

    return a


tup = (1,2,3,4,5,6,7,8,9,10)
print(tuple_even(tup))

# **************************************************
def yes(string):

    return print('Yes' if string.upper() == 'YES' else "No")

yes('yEs')

# **************************************************
def filter_2(list_a):

    filt = list(filter(lambda x: x % 2 == 0, list_a))

    return filt

list_a = [1,2,3,4,5,6,7,8,9,10]
print(filter_2(list_a))

# **************************************************
def map_sqr(list_a):

    sqr = list(map(lambda x: x ** 2, list_a))

    return sqr

list_a = [1,2,3,4,5,6,7,8,9,10]
print(map_sqr(list_a))

# **************************************************
def mapFiltSqr(list_a):

    sqr = list(map(lambda x: x ** 2, list(filter(lambda x: x % 2 == 0, list_a))))

    return print(sqr)

list_a = [1,2,3,4,5,6,7,8,9,10]
mapFiltSqr(list_a)

# **************************************************
def filt_list():

    return list(filter(lambda x: x % 2 == 0, [i for i in range(1, 20 + 1)]))

print(filt_list())

# **************************************************
def map_list():

    return list(map(lambda x: x ** 2, [i for i in range(1, 20 + 1)]))

print(map_list())

# **************************************************
class American:

    @staticmethod
    def printNationality(nationality):
        print(nationality)


obj = American()
American().printNationality('Ukrainian')

