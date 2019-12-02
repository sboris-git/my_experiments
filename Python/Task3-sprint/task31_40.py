def sum_two_int_str(str1, str2):

    str_x = str1 if len(str1) > len(str2) else str2

    return str_x


print(sum_two_int_str('233', '11'))

# *************************************************
def even(number=None):

    if number % 2 == 0:
        string = "It is an even number"
    else:
        string = "It is an odd number"

    return string

print(even(5))
# *************************************************
def dict_square(a, b):

    dict_sqr = {i: i * i for i in range(a, b + 1)}

    return dict_sqr


if __name__ == '__main__':
    print(dict_square(1, 3))

# *************************************************
def dict_sqr_from_import(a, b):

    return dict_square(a, b)

print(dict_sqr_from_import(1, 20))

# *************************************************
from modul import list_to_str


def dict_sqr_from_import(a, b):
    return list_to_str(dict_square(a, b).values(), ', ')

print(dict_sqr_from_import(1, 20))

# *************************************************
from modul import list_to_str


def dict_sqr_from_import(a, b):
    return list_to_str(dict_square(a, b).keys(), ', ')

print(dict_sqr_from_import(1, 20))

# *************************************************
def list_square(a, b):

    return [i * i for i in range(a, b + 1)]

print(list_square(1, 20))

# *************************************************
def list_square(a, b):

    list_a = [i * i for i in range(a, b + 1)]

    return list_a[:5]

print(list_square(1, 20))

# *************************************************
def list_square(a, b):

    list_a = [i * i for i in range(a, b + 1)]

    return list_a[-1:-6:-1]

print(list_square(1, 20))

# *************************************************
def list_square(a, b):

    list_a = [i * i for i in range(a, b + 1)]

    return list_a[5:]

print(list_square(1, 20))