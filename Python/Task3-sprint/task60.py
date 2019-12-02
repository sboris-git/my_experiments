def text_to_unicode(text):
    '''into byte!!!! b'hello word' - not ToDo unicode - have a look at task82.py'''
    # in Python 3 str type is Unicode

    text = text.encode('utf-8') #  into byte!!!! not ToDo unicode - have a look at task82.py
    text = text.decode('utf-8')

    return text


if __name__ == '__main__':
    text = 'hello word'
    print(text_to_unicode(text))
    print(u'string')