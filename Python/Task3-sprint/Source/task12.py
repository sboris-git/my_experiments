from modul import list_to_str

def even_digits(x, y):
    '''Write a program, which will find all such numbers between 1000 and 3000 (both included)
    such that each digit of the number is an even number.
    The numbers obtained should be printed in a comma-separated sequence on a single line.'''

    list = [number for number in range(x, y + 1)]
    filter_obj = filter(lambda x: x % 2 == 0, list)
    string = list_to_str(filter_obj, ',')

    return string

print(even_digits(1000,3000))