def div_0(a, b):

    try:
        c = a / b
    except ZeroDivisionError:
        # print("You can't divide by zero!")
        c = None

    return c


print(div_0(5, 0))
