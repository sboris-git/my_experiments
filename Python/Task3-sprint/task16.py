def comprehension():
    a_list = '1,2,3,4,5,6,7,8,9'
    list_num = [int(elem) for elem in a_list.split(',') if int(elem) % 2 != 0]

    return list_num


print(comprehension())