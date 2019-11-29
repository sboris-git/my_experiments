def count_upper_lower(text):

    upper = 0
    lower = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return print('UPPER CASE {} \nLOWER CASE {}'.format(upper, lower))

count_upper_lower('Hello world!')