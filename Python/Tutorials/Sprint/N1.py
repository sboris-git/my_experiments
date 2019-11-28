from collection import list_to_str


def filter_7_5(*list_a):

    list_a = [number for number in range(2000, 3200)]

    filter_obj = filter(lambda x: x % 7 == 0, filter(lambda x: x % 5 != 0, list_a))
    string = list_to_str(filter_obj)

    return print(string)

# list_a = [7, 15, 14, 4, 5, 21, 35, 49]
filter_7_5()


