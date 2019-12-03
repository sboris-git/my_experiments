def list_to_str(a_list, delimiter):
    '''The of numbers to be returned in a delimiter specified sequence on a single string'''

    if isinstance(a_list, list) != True:
        a_list = list(a_list)

    string = delimiter.join([str(item) for item in list(a_list)])

    return string


def tuple_sort(tupl_list):
    '''Sorting list of tuples. A list of tuples is an argument for the function'''

    ans = tupl_list.sort(key = lambda x: (x[0], x[1], x[2]))

    return ans
