from modul import list_to_str


def filter_7_5(a, b):

    list_a = [number for number in range(a, b + 1)]

    filter_obj = filter(lambda x: x % 7 == 0, filter(lambda x: x % 5 != 0, list_a))
    string = list_to_str(filter_obj, ', ')

    return string


# list_a = [7, 15, 14, 4, 5, 21, 35, 49]
print(filter_7_5(2000, 3200))


