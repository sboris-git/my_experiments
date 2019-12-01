def dict_square(a, b):

    dict_sqr = {i: i * i for i in range(a, b + 1)}

    return dict_sqr


if __name__ == '__main__':
    print(dict_square(1, 3))

