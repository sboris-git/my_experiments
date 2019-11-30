def text_to_unicode(text):
    '''Reads an ASCII string and converts it to a unicode string encoded by utf-8.'''

    return print(text.encode('UTF-8'))


text = 'hello word'
text_to_unicode(text)
# print(text_to_unicode.__doc__)
# print(u'string')