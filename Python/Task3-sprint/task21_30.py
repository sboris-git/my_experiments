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
freq('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')  # input('Type a string: ')

# ************************************
class Number:

    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2


obj = Number(5)
print(obj.square())
# ************************************
def tuple_driver():
    ''' This is driver function tuple_driver() for sorting a list of tuples
    the function is given as an example of __doc__
    The output is a list
    [abs_doc, int_doc, input_doc, tuple_driver_doc]
    '''
    pass


def docs():
    abs_doc = abs.__doc__
    int_doc = int.__doc__
    input_doc = input.__doc__
    tuple_driver_doc = tuple_driver.__doc__
    rep = [abs_doc, int_doc, input_doc, tuple_driver_doc]
    return rep

print(docs())

# ************************************
class City:
    city = "City"

    def __init__(self, city = None):
        self.city = city


usa = City("NY")
print("{} is {}".format(City.city, usa.city))

canada = City()
canada.city = "Toronto"

print("{} is {}".format(City.city, canada.city))

# ************************************
def sum(a, b):

    return a + b


print(sum(2, 3))
# ************************************
def int_into_str(num):

    return str(num)


print(int_into_str(53))

# ************************************
def int_into_str(num):

    return str(num)


print(int_into_str(53))

# ************************************
def sum_two_int_str(str1, str2):

    return int(str1) + int(str2)


print(sum_two_int_str('23', '11'))

# ************************************
def sum_two_int_str(str1, str2):
    return print(str1 + str2)


sum_two_int_str('23', '11')

# ************************************
