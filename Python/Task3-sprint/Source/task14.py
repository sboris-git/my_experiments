def count_upper_lower(text):
    '''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

    Suppose the following input is supplied to the program:
        Hello world!
    Then, the output should be:
        UPPER CASE 1
        LOWER CASE 9'''

    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return 'UPPER CASE {} \nLOWER CASE {}'.format(upper, lower)

print(count_upper_lower('Hello world!'))