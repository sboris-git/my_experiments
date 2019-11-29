def even(number=None):

    if number % 2 == 0:
        string = "It is an even number"
    else:
        string = "It is an odd number"

    return string

print(even(5))