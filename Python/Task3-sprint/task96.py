def freq(lst=None):
    '''Question 96
    Please write a program which count and print the numbers of each character in a string input by console.

    Example:
    If the following string is given as input to the program:
        abcdefgabc
    Then, the output of the program should be:
        a,2
        c,2
        b,2
        e,1
        d,1
        g,1
        f,1
    '''

    string = input('Type a string: ')
    list_chars = list(string)
    set_letter = set(list_chars)
    cnt_dict = {letter: list_chars.count(letter) for letter in set_letter}

    for k, v in sorted(cnt_dict.items()):
        print('{},{}'.format(k, v))

    return sorted(cnt_dict.items())


freq()