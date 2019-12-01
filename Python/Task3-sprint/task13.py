def count_alpha_num(text):
    '''Write a program that accepts a sentence and calculate the number of letters and digits.

    Suppose the following input is supplied to the program:
        hello world! 123
    Then, the output should be:
        LETTERS 10
        DIGITS 3'''

    digits = 0
    alpha = 0

    for char in text:

        if char.isdigit():
            digits += 1
        elif char.isalpha():
            alpha += 1

    return 'LETTERS {} \nDIGITS {}'.format(alpha, digits)

print(count_alpha_num('hello world! 123'))


