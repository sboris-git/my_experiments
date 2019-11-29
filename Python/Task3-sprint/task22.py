def freq():

    string = input('Type a string: ')
    list_word = string.split()
    set_word = set(list_word)
    cnt_dict = {word: list_word.count(word) for word in set_word}
    print(cnt_dict)
    # res = dict(zip(list(word), list_word.count(word)))
    for k, v in sorted(cnt_dict.items()):
        print('{}:{}'.format(k, v))

    return


# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3
freq()