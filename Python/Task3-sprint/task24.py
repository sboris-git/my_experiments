def tuple_driver():
    ''' This is driver function tuple_driver() for sorting a list of tuples
    the function is given as an example of __doc__ '''
    pass


def docs():
    abs_doc = abs.__doc__
    int_doc = int.__doc__
    input_doc = input.__doc__
    tuple_driver_doc = tuple_driver.__doc__
    rep = [abs_doc, int_doc, input_doc, tuple_driver_doc]
    return rep

print(docs())
