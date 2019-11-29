from collection import list_to_str

def div5(bin_str):
    bin_list = bin_str.split(',')
    list_dec = map(lambda x: int(str(x), 2), bin_list)
    filter_obj = filter(lambda x: x % 5 == 0, list_dec)
    string = list_to_str(filter_obj, ', ')
    return print(string)

data = '0100,0011,1010,1001'
div5(data)
