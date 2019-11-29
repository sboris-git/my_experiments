def count_alpha_num(text):

    digits = 0
    alpha = 0
    for char in text:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            alpha += 1

    return print('LETTERS {} \n DIGITS {}'.format(alpha, digits))

count_alpha_num('hello world! 123')


