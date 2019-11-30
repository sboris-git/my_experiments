def text_to_unicode(text):
    return print(text.encode('UTF-8'))

if __name__ == '__main__':
    text = 'hello word'
    text_to_unicode(text)
    # print(u'string')