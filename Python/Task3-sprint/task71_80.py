def calc(expression):
    '''Question 71
    Please write a program which accepts basic mathematic expression from console and print the evaluation result.

        Example:
        If the following string is given as input to the program:
            35+3
        Then, the output of the program should be:
            38'''
    # operand = {'+': 'add',
    #            '-': 'sub',
    #            '*': 'mult',
    #            '/': 'div',
    #            '^': 'pow'
    #            }
    #
    # string = '7+8'  # input('Type a string: ')
    #
    # pattern = re.compile(r'(\d+)(\D)(\d+)')
    # matches = pattern.finditer(string)
    # print([match.group(2) for match in matches])
    expression = input('type math here: ')
    ans = eval(expression)

    return print(ans)

calc()

# *******************************************
from bisect import bisect_left

def half_div_search(a, target):
    '''Question 72
    Locate the leftmost value exactly equal to target
    https://docs.python.org/3/library/bisect.html

    Please write a binary search function which searches an item in a sorted list.
    The function should return the index of element to be searched in the list.
    '''

    a.sort()
    i = bisect_left(a, target)
    if i != len(a) and a[i] == target:
        return i
    else:
        return -1

if __name__ == '__main__':
    sequence = [1, 25, 4, 6, 8, 10, 46, 1, 5]

    print(half_div_search(sequence, 6))

# *******************************************
# task73
sequence = [1, 25, 4, 6, 8, 10, 46, 1, 5]

print(half_div_search(sequence, 6))

# *******************************************
from random import uniform


def rnd(start, end):
    '''Question 74
    Please generate a random float where the value is between 10 and 100 using Python math module.'''
    number = uniform(start, end)

    return number


if __name__ == '__main__':
    print(rnd(10, 100))

# *******************************************
print(rnd(5, 95))

# *******************************************
def rnd_even():
    '''Question 76
    Please write a program to output a random even number between 0 and 10 inclusive
    using random module and list comprehension.'''

    even_random = random.choice([i / 100 for i in range(1100) if i % 2 == 0]) # extending range to float
    even_random = '{:.2f}'.format(even_random)

    return even_random


print(rnd_even())

# *******************************************
def rnd_35():
    '''Question 77
    Please write a program to output a random number,
    which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.'''

    even_random = random.choice([i / 100 for i in range(1100) if i % 35 == 0])  # extending range to float
    even_random = '{:.2f}'.format(even_random)

    return even_random


print(rnd_35())

# *******************************************
def rnd_n(start, end, elements):
    '''Question 79
    Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
    '''
    lst = [i / 100 for i in range(start * 10, (end + 1) * 10) if i % 2 == 0]  # extending range to float
    lst_random = ['{:.2f}'.format(random.choice(lst)) for i in range(elements)]

    return lst_random


print(rnd_n(100, 200, 5))
# *******************************************
def rnd_n(start, end, elements):
    '''Question 78
    Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.'''
    lst = [i / 100 for i in range(start * 10, (end + 1) * 10)]  # extending range to float
    lst_random = ['{:.2f}'.format(random.choice(lst)) for i in range(elements)]

    return lst_random


print(rnd_n(100, 200, 5))
# *******************************************
from modul import list_to_str


def rnd_35(start, end, elements):
    '''Question 80
    Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 ,
    between 1 and 1000 inclusive.'''

    lst = [i / 100 for i in range(start * 100, (end + 1) * 100) if i % 35 == 0]
    lst_random = [random.choice(lst) for i in range(elements)]
    ans = list_to_str(lst_random, ', ')

    return ans


print(rnd_35(1, 1000, 5))