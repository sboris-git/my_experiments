from task33 import dict_square
from modul import list_to_str


def dict_sqr_from_import(a, b):
    return list_to_str(dict_square(a, b).values(), ', ')

print(dict_sqr_from_import(1, 20))