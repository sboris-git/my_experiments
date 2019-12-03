def assert_data(data):

    for x in data:
        assert x % 2 == 0, "{} is an odd number".format(x)
    return


data = [2, 4, 5, 6]
assert_data(data)
