from modul import list_to_str


def div5(bin_str):
    '''Write a program which accepts a sequence of comma separated 4 digit binary numbers
    as its input and then check whether they are divisible by 5 or not. The numbers that are
    divisible by 5 are to be printed in a comma separated sequence.

    Example:
        0100,0011,1010,1001
    Then the output should be:
        1010
    Notes: Assume the data is input by console.'''

    bin_list = bin_str.split(',')
    filter_obj = filter(lambda x: int(str(x), 2) % 5 == 0, bin_list)

    string = list_to_str(filter_obj, ', ')

    return string


data = '0100,0011,1010,1001'
print(div5(data))

# *******************************************

def even_digits(x, y):
    '''Write a program, which will find all such numbers between 1000 and 3000 (both included)
    such that each digit of the number is an even number.
    The numbers obtained should be printed in a comma-separated sequence on a single line.'''

    list = [number for number in range(x, y + 1)]
    filter_obj = filter(lambda x: x % 2 == 0, list)
    string = list_to_str(filter_obj, ',')

    return string

print(even_digits(1000,3000))

# *******************************************
def count_alpha_num(text):
    '''Write a program that accepts a sentence and calculate the number of letters and digits.

    Suppose the following input is supplied to the program:
        hello world! 123
    Then, the output should be:
        LETTERS 10
        DIGITS 3'''

    digits = 0
    alpha = 0

    for char in text:

        if char.isdigit():
            digits += 1
        elif char.isalpha():
            alpha += 1

    return 'LETTERS {} \nDIGITS {}'.format(alpha, digits)

print(count_alpha_num('hello world! 123'))

# *******************************************
def count_upper_lower(text):
    '''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

    Suppose the following input is supplied to the program:
        Hello world!
    Then, the output should be:
        UPPER CASE 1
        LOWER CASE 9'''

    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return 'UPPER CASE {} \nLOWER CASE {}'.format(upper, lower)

print(count_upper_lower('Hello world!'))

# *******************************************
def compute(n):
    '''Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

    Suppose the following input is supplied to the program:
        9
    Then, the output should be:
        11106'''

    list_str = 'a+aa+aaa+aaaa'.replace('a', str(n)).split('+')
    ans = sum([int(elem) for elem in list_str])

    return ans

# sum([int(elem) for elem in 'a+aa+aaa+aaaa'.replace('a', '8').split('+')])

print(compute(9))

# *******************************************
def comprehension(a_list=None):
    '''Use a list comprehension to square each odd number in a list.
    The list is input by a sequence of comma-separated numbers.

    Suppose the following input is supplied to the program:
        1,2,3,4,5,6,7,8,9
    Then, the output should be:
        1,3,5,7,9   '''

    # a_list = '1,2,3,4,5,6,7,8,9'
    list_num = [int(elem) for elem in a_list.split(',') if int(elem) % 2 != 0]

    return list_num

a_list = '1,2,3,4,5,6,7,8,9'
print(comprehension(a_list))

# *******************************************
def bank():
    '''uestion 17
    Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
    D 100
    W 200
    D means deposit while W means withdrawal.

    Suppose the following input is supplied to the program:
        D 300
        D 300
        W 200
        D 100
    Then, the output should be: 100-200+300+300-200+100 = 400!!!
    500'''

    trans = 'D 300\nD 300\nW 200\nD 100'  #[]

    # while True:
    #     com = input()
    #     if len(com) == 0:
    #         break
    #     trans.append(com)
    #     print(trans)

    net = 0
    for item in trans:
        if 'D' in item:
            net += int(item.strip('D '))
        elif 'W' in item:
            net -= int(item.strip('W '))

    return net

print(bank())

# *******************************************
import re


def check(text):

    valid = None
    tmp_list = []

    if 6 <= len(text) <= 12:
        tmp_list.append(bool(re.search("[a-z]", text)))
        tmp_list.append(bool(re.search("[A-Z]", text)))
        tmp_list.append(bool(re.search("[0-9]", text)))
        tmp_list.append(bool(re.search("[$#@]", text)))

    if tmp_list.count(True) >= 4:
        valid = text

    return valid


def validation(pswd):

    valid_pswd = []

    if isinstance(pswd, list):
        for passwrd in pswd:
            if check(passwrd) is not None:
                valid_pswd.append(passwrd)
    else:
        valid_pswd.append(valid_pswd)

    return list_to_str(valid_pswd, ', ')  # ToDo , ','


pass_list = ['ABd1234@1', 'a F1#', '2w3E*', '2We3345']
print(validation(pass_list))

# *******************************************
def tuple_driver():
    ''' This is driver function tuple_driver() for sorting a list of tuples '''

    tupl_list = [('Tom', 19, 80), # ToDo
                 ('John', 20, 90),
                 ('Jony', 17, 91),
                 ('Jony', 17, 93),
                 ('Json', 21, 85)]

    tupl_list.sort(key=lambda x: (x[0], x[1], x[2]))

    return tupl_list


print(tuple_driver())

# *******************************************
class Gen:

    def gener(self, x):
        for number in range(x):
            if number % 7 == 0:
                yield number
        return number


n = 100
num = Gen()
gen_list = num.gener(n)
print(gen_list)

# *******************************************

