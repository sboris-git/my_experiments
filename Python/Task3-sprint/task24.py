from pip._vendor.distlib.compat import raw_input


def tuple_driver():
    ''' This is driver function tuple_driver() for sorting a list of tuples '''

    tupl_list = [('Tom', 19, 80),
                 ('John', 20, 90),
                 ('Jony', 17, 91),
                 ('Jony', 17, 93),
                 ('Json', 21, 85)]
    tupl_list.sort(key=lambda x: (x[0], x[1], x[2]))
    return print(tupl_list)


def docs():
    print(abs.__doc__)
    print(int.__doc__)
    print(raw_input.__doc__)
    print(tuple_driver.__doc__)


docs()
