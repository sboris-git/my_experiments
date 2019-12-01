def num4(inp_data=None):
    '''4. Write a program which accepts a sequence of comma-separated numbers from console and
    generate a list and a tuple which contains every number.

    Suppose the following input is supplied to the program:
        34,67,55,33,12,98
    Then, the output should be:
        ['34', '67', '55', '33', '12', '98']
        ('34', '67', '55', '33', '12', '98')'''
    # inp_data = '34, 67, 55, 33, 12, 98'

    inp_data = input('Type a numbers: ')
    list_data = inp_data.split(',')
    tuple_data = tuple(i for i in list_data)
    ans = '{}\n{}'.format(list_data, tuple_data)

    return ans

print(num4())