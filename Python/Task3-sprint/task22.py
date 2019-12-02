def freq(string):
    '''Question 22
    Write a program to compute the frequency of the words from the input.
    The output should output after sorting the key alphanumerically.
    Suppose the following input is supplied to the program:
    New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
    Then, the output should be:
        2:2
        3.:1
        3?:1
        New:1
        Python:5
        Read:1
        and:1
        between:1
        choosing:1
        or:2
        to:1'''

    # string = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'  # input('Type a string: ')
    list_word = string.split()
    set_word = set(list_word)
    cnt_dict = {word: list_word.count(word) for word in set_word}
    # print(cnt_dict)

    for k, v in sorted(cnt_dict.items()):
        print('{}:{}'.format(k, v))

    return sorted(cnt_dict.items())


# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3
freq('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')