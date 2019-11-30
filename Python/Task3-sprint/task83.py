import timeit


'''Question 83
Please write a program to print the running time of execution of "1+1" for 100 times.'''

code_to_test = """
a = 1+1
"""
elapsed_time = timeit.timeit(code_to_test, number=100)

print(elapsed_time)