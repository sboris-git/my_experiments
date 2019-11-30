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