from collection import list_to_str

def even_digits(x, y):
    list = [number for number in range(x, y+1)]
    filter_obj = filter(lambda x: x % 2 == 0, list)
    string = list_to_str(filter_obj, ',')

    return string

print(even_digits(1000,3000))