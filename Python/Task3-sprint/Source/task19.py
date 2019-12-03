def tuple_driver():
    ''' This is driver function tuple_driver() for sorting a list of tuples '''


    tupl_list = [('Tom', 19, 80), # ToDo
                ('John', 20, 90),
                ('Jony', 17, 91),
                ('Jony', 17, 93),
                ('Json', 21, 85)]

    tupl_list.sort(key=lambda x: (x[0], x[1], x[2]))

    return tupl_list


print(tuple_driver())

