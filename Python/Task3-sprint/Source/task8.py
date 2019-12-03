from modul import list_to_str


def sortstring(csv_string=None):
    '''
    Write a program that accepts a comma separated sequence of words as input and prints
    the words in a comma-separated sequence after sorting them alphabetically.

    Suppose the following input is supplied to the program:
    without,hello,bag,world
    Then, the output should be:
    bag,hello,without,world
    '''

    list_string = input('type csv string ').split(',')
    list_str = sorted(list_string)
    list_str = list_to_str(list_str, ',')

    return list_str


print(sortstring())