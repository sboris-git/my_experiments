def comprehension(a_list):
    list_num = [int(elem) for elem in a_list.split(',') if elem %2 != 0]

    value = 123
    print(value, 'is', 'even' if value % 2 == 0 else 'odd')
