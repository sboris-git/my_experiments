def count_alpha_num(text):

    digits = 0
    alpha = 0
    for char in text:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            alpha += 1

    return 'LETTERS {} \nDIGITS {}'.format(alpha, digits)

print(count_alpha_num('hello world! 123'))


