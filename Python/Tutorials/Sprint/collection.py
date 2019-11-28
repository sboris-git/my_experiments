def list_to_str(a_list):
    '''The of numbers to be returned in a comma-separated sequence on a single string'''

    if isinstance(a_list, list) != True:
        a_list = list(a_list)

    string = ', '.join([str(item) for item in list(a_list)])

    return string
