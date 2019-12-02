from modul import list_to_str

# ************************
def n_1(a, b):

    list_a = [number for number in range(a, b + 1)]

    filter_obj = filter(lambda x: x % 7 == 0, filter(lambda x: x % 5 != 0, list_a))
    string = list_to_str(filter_obj, ', ')

    return string

# ************************
def n_2(n):

    if n == 1:
        return n
    else:
        return n*n_2(n-1)

def run():

    # in_str = input('Type a coma delimited numbers')
    in_str = '2, 4, 6, 8, 1'

    numbers = [int(item) for item in in_str.split(',')]
    ans = list_to_str([n_2(item) for item in numbers], ', ')

    return ans

# print(run())

# ************************
def n_3(n):
    '''3. With a given integral number n, write a program to generate a dictionary that
    contains (i, i*i) such that is an integral number between 1 and n (both included).
    and then the program should print the dictionary.

    Suppose the following input is supplied to the program:
        8
    Then, the output should be:
        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''

    d = dict()

    for x in range(1, n+1):
        d[x] = x ** 2

    return d


print(n_3(8))

# ************************

def n_4(inp_data=None):
    '''4. Write a program which accepts a sequence of comma-separated numbers from console and
    generate a list and a tuple which contains every number.

    Suppose the following input is supplied to the program:
        34,67,55,33,12,98
    Then, the output should be:
        ['34', '67', '55', '33', '12', '98']
        ('34', '67', '55', '33', '12', '98')'''
    # inp_data = '34, 67, 55, 33, 12, 98'

    inp_data = '34,67,55,33,12,98'  # input('Type a numbers: ')
    list_data = inp_data.split(',')
    tuple_data = tuple(i for i in list_data)
    ans = '{}\n{}'.format(list_data, tuple_data)

    return ans

print(n_4())

# ************************

class Test:
    '''Define a class which has at least two methods:
        getString: to get a string from console input
        printString: to print the string in upper case.
    Also please include simple test function to test the class methods.'''

    def __init__(self):
        self.string = ''

    def getString(self):
        self.string = input('Type a string: ')

    def printString(self):
        print(self.string.upper())


obj = Test()
obj.getString()
obj.printString()

# ************************
import math

def n_6(d=None):
    '''6. Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]

    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a comma-separated sequence.

    Example
        Let us assume the following comma separated input sequence is given to the program:
        100,150,180
        The output of the program should be:
        18,22,24'''

    c = 50
    h = 30
    q = []
    inp_data = '100,150,180'  # input('d= ')
    for d in inp_data.split(','):
        q.append(round(math.sqrt((2*c*int(d)/h))))

    return list_to_str(q, ',')

print(n_6())

# ************************
def n_7(x, y):
    '''Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1,ВЎВ­Y-1.

    Example
    Suppose the following inputs are given to the program:
        3,5
    Then, the output of the program should be:
        [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] '''

    array = []

    for i in range(0, x):
        temp = []

        for j in range(0, y):
            temp.append(i * j)
        array.append(temp)

    return array

print(n_7(3, 5))

# ************************
from modul import list_to_str


def n_8(csv_string=None):
    '''
    Write a program that accepts a comma separated sequence of words as input and prints
    the words in a comma-separated sequence after sorting them alphabetically.

    Suppose the following input is supplied to the program:
    without,hello,bag,world
    Then, the output should be:
    bag,hello,without,world
    '''

    list_string = input('type csv string ').split(',')
    list_str = sorted(list_string)
    list_str = list_to_str(list_str, ',')

    return list_str


print(n_8())
# ************************
def n_9(text):
    '''Write a program that accepts sequence of lines as input and prints the lines
    after making all characters in the sentence capitalized.

    Suppose the following input is supplied to the program:
        Hello world
        Practice makes perfect
    Then, the output should be:
        HELLO WORLD
        PRACTICE MAKES PERFECT'''

    return text.upper()

text = '''Hello world
Practice makes perfect
'''
print(n_9(text))

# ************************
def n_10(text):
    '''Write a program that accepts a sequence of whitespace separated words
     as input and prints the words after removing all duplicate words and sorting them alphanumerically.
    Suppose the following input is supplied to the program:
    hello world and practice makes perfect and hello world again
    Then, the output should be:
    again and hello makes perfect practice world'''

    ans = list_to_str(sorted(set(text.split())), ' ')
    return ans


print(n_10('hello world and practice makes perfect and hello world again'))

# ************************



