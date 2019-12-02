def drop_elem(lst):
    '''Question 91
    By using list comprehension, please write a program to print the list after
    removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]'''

    filtered = [elem for (i, elem) in enumerate(lst) if i not in [0, 4, 5]]

    return filtered


lst = [12, 24, 35, 70, 88, 120, 155]
print(drop_elem(lst))

# ***************************
def drop_elem(lst):
    '''Question 92
    By using list comprehension, please write a program to print the list after
    removing the value 24 in [12,24,35,24,88,120,155].'''

    filtered = [elem for elem in lst if elem != 24]

    return filtered


lst = [12, 24, 35, 70, 88, 120, 155]
print(drop_elem(lst))

# ***************************
def inters(lst1, lst2):
    '''Question 93
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
    write a program to make a list whose elements are intersection of the above given lists.'''

    set1 = set(lst1)
    set2 = set(lst2)
    inner_join = set.intersection(set1, set2)
    return inner_join


lst1 = [1, 3, 6, 78, 35, 55]
lst2 = [12, 24, 35, 24, 88, 120, 155]

print(inters(lst1, lst2))


# ***************************
def removeDuplicates(lst):
    '''Question 94
    With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after
    removing all duplicate values with original order reserved.'''

    unique = set(lst)
    for elem in unique:
        if lst.count(elem) > 1:
            lst.remove(elem)

    return lst


lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(removeDuplicates(lst))

# ***************************
class Person:
    '''Question 95
    Define a class Person and its two child classes: Male and Female. All classes have
    a method "getGender" which can print "Male" for Male class and "Female" for Female class.'''

    def __init__(self):
        self.gender = 'Person'

    def getGender(self):
        print(self.gender)


class Male(Person):

    def __init__(self):
        self.gender = 'Male'


class Female(Person):

    def __init__(self):
        self.gender = 'Female'


person1 = Person()
person1.getGender()

person2 = Male()
person2.getGender()

person3 = Female()
person3.getGender()
# ***************************
def freq(string):
    '''Question 96
    Please write a program which count and print the numbers of each character in a string input by console.

    Example:
    If the following string is given as input to the program:
        abcdefgabc
    Then, the output of the program should be:
        a,2
        c,2
        b,2
        e,1
        d,1
        g,1
        f,1
    '''

    # string = input('Type a string: ')
    list_chars = list(string)
    set_letter = set(list_chars)
    cnt_dict = {letter: list_chars.count(letter) for letter in set_letter}

    for k, v in sorted(cnt_dict.items()):
        print('{},{}'.format(k, v))

    return sorted(cnt_dict.items())


freq('abcdefgabc')
# ***************************
def rev_list(string):
    '''Question 97
    Please write a program which accepts a string from console and print it in reverse order.

    Example:
    If the following string is given as input to the program:
        rise to vote sir
    Then, the output of the program should be:
        ris etov ot esir'''

    # string = input('Type a string: ')
    string = ''.join(reversed(string))
    # string = string[::-1]

    return string


print(rev_list('rise to vote sir'))


# ***************************
from modul import list_to_str


def drop_even(string):
    ''' Question 98
    Please write a program which accepts a string from console and print the characters that have even indexes.

    Example:
    If the following string is given as input to the program:
        H1e2l3l4o5w6o7r8l9d
    Then, the output of the program should be:
        Helloworld'''

    cleaned = [char for (i, char) in enumerate(list(string)) if i % 2 == 0 ]
    # cleaned = string[::2]

    return list_to_str(cleaned, '')


string = 'H1e2l3l4o5w6o7r8l9d'
print(drop_even(string))


# ***************************
import itertools


def perm(lst):
    '''Question 99
    Please write a program which prints all permutations of [1,2,3]'''

    per = list(itertools.permutations(lst))

    return per


lst = [1, 2, 3]
print(perm(lst))
# ****************************
import numpy as np


def sleq():
    '''Question 100
    Write a program to solve a classic ancient Chinese puzzle:
    We count 35 heads and 94 legs among the chickens and rabbits in a farm.
    How many rabbits and how many chickens do we have?

    2*x + 4*y = 94
    x + y = 35
    '''

    a = np.array([[2, 4],
                  [1, 1]])
    b = np.array([94, 35])
    x = np.linalg.inv(a).dot(b)

    return x


print(sleq())

