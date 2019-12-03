from modul import list_to_str

def div5(bin_str):
    '''Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

    Example:
        0100,0011,1010,1001
    Then the output should be:
        1010
    Notes: Assume the data is input by console.'''

    bin_list = bin_str.split(',')
    filter_obj = filter(lambda x: int(str(x), 2) % 5 == 0, bin_list)

    string = list_to_str(filter_obj, ', ')

    return string


data = '0100,0011,1010,1001'
print(div5(data))
