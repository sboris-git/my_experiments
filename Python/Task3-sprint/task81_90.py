import random


def rnd_n():
    '''Question 81
    Please write a program to randomly print a integer number between 7 and 15 inclusive.'''

    n_random = random.choice([i for i in range(7, 16)])
    return n_random


print(rnd_n())

# ************************************************
import bz2


# import zlib
def compress(text):
    '''Question 82
    Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".'''

    # comp_zlib = zlib.compress(text)
    # print("Compressed: ", comp_zlib)
    text = str.encode(text)
    comp_bz = bz2.compress(text)
    # print("Compressed: ", comp_bz)

    return comp_bz


def decompress(comp):
    # decomp_zlib = zlib.decompress(comp)
    # print("Decompressed: ", decomp_zlib)
    decomp_bz = bz2.decompress(comp)
    # print( "Decompressed: ", decomp_bz )
    decode_utf = decomp_bz.decode('utf-8')
    return decode_utf


text = "hello world!hello world!hello world!hello world!"
print(text)
comp = compress(text)
print(decompress(comp))

# ************************************************
import timeit
import time


'''Question 83
Please write a program to print the running time of execution of "1+1" for 100 times.'''

code_to_test = """
a = 1+1
"""
elapsed_time = timeit.timeit(code_to_test, number=100)

print(elapsed_time)


def elapsed_time():
    start = time.time()
    for i in range(100):
        x = 1 + 1
    finish = time.time()
    duration = finish - start

    return duration

print(elapsed_time())

# ************************************************
from random import shuffle


def shuffle_lst(lst):
    '''Question 84
    Please write a program to shuffle and print the list [3,6,7,8].'''

    shuffle(lst)
    return lst

if __name__ == '__main__':
    lst = [3, 6, 7, 8]
    print(shuffle_lst(lst))

# ************************************************
lst = [3, 6, 7, 8]
print(shuffle_lst(lst))

# ************************************************
def sentence():
    '''Question 86
    Please write a program to generate all sentences where subject is in ["I", "You"] and
    verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].'''

    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]
    full = []
    for sub in subjects:
        sent = []
        for verb in verbs:
            subj_verb = []
            for obj in objects:
                subj_verb.append([sub, verb, obj])
            sent.append(subj_verb)
        full.append(sent)

    return full


print(sentence())

# ************************************************
def odd_list(lst=None):
    '''Question 87
    Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].'''

    lst_res = list(filter(lambda n: n % 2 != 0, lst))
    return lst_res


lst = [5, 6, 77, 45, 22, 12, 24]
print(odd_list(lst))

# ************************************************
def drop_35(lst=None):
    '''Question 88
    By using list comprehension, please write a program to print the list after removing delete
    numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
    '''

    target = list(filter(lambda x: x % 35 != 0, lst))

    return target


lst = [12, 24, 35, 70, 88, 120, 155]
print(drop_35(lst))

# ************************************************
def drop_even(lst):
    '''Question 89
    By using list comprehension, please write a program to print the list after
    removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].'''

    filtered = [elem for (i, elem) in enumerate(lst) if i % 2 != 0]

    return filtered


lst = [12, 24, 35, 70, 88, 120, 155]
print(drop_even(lst))
