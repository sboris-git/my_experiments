from collection import list_to_str

def sortstring(csv_string):
    list_string = input('type csv string ').split(',')
    list_str = sorted(list_string)
    return list_to_str(list_str, ',')

print(sortstring('without,hello,bag,world'))