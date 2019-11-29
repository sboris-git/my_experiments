def tuple_driver():

    tupl_list = [('Tom', 19, 80),
                ('John', 20, 90),
                ('Jony', 17, 91),
                ('Jony', 17, 93),
                ('Json', 21, 85)]
    tupl_list.sort(key=lambda x: (x[0], x[1], x[2]))
    return print(tupl_list)


tuple_driver()

