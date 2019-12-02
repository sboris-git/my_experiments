class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


obj = Circle(5)
print(obj.area())

# ********************************************************
class Rectangle:

    def __init__(self, lengt, width):
        self.lengt = lengt
        self.width = width

    def area(self):
        return self.lengt * self.width


obj = Rectangle(5, 6)
print(obj.area())

# ********************************************************
class Shape:

    def __init__(self, length=None, width=None):
        self.length = length
        self.width = width

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length=None):
        Shape.__init__(self, length)
        # self.length = length

    def area(self):
        return self.length ** 2


obj = Square(5)
print(obj.area())

# ********************************************************
def div_0(a, b):

    try:
        c = a / b
    except ZeroDivisionError:
        # print("You can't divide by zero!")
        c = None

    return c


print(div_0(5, 0))

# ********************************************************
class CustomException(Exception):
    '''Question 56  Define a custom exception class which takes a string message as attribute.
       message -- explanation of the error
    '''

    def __init__(self, message):
        self.message = message


a = 6
try:
    if a < 5:
        raise CustomException("The number is less than 5")
    elif a > 5:
        raise CustomException("The number is greater than 5")
except CustomException as err:
    print("Error: " + err.message)

# ********************************************************
def user():

    email = input('type the email: ')
    username = email.split('@')[0]
    return username


print(user())

# ********************************************************
def user1():
    email = input('type the email: ')
    domain = email.split('@')[1]
    domain_name = domain.split('.')[0]

    return domain_name


print(user1())
# ********************************************************
import re


def spaceSeparated():
    text = input('Type a text: ')
    pattern = re.compile(r'\d+')
    matches = pattern.findall(text)

    return matches
    # pattern = re.compile(r'(\d+)')
    # matches = pattern.finditer(text)
    # return print([match.group(0) for match in matches])


# text = '2 cats and 30 dogs.'
print(spaceSeparated())

# ********************************************************
def text_to_unicode(text):
    '''into byte!!!! b'hello word' - not unicode - have a look at task82.py'''
    # in Python 3 str type is Unicode

    text = text.encode('utf-8')
    text = text.decode('utf-8')

    return text


if __name__ == '__main__':
    text = 'hello word'
    print(text_to_unicode(text))
    print(u'string')

# ********************************************************