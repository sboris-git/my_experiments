from random import uniform


def rnd(start, end):
    '''Question 74
    Please generate a random float where the value is between 10 and 100 using Python math module.'''
    number = uniform(start, end)

    return number


if __name__ == '__main__':
    print(rnd(10, 100))

