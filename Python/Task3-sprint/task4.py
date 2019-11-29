# inp_data = '34, 67, 55, 33, 12, 98'
def num4(*args):
    inp_data = input('Type a numbers: ')
    list_data = inp_data.split(',')
    print(list_data)
    print(tuple(i for i in list_data))
    return

num4()