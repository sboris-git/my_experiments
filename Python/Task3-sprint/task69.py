from collection import list_to_str
'''Question 69
    Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
        
    Example:
        If the following n is given as input to the program:
            100
        Then, the output of the program should be:
            0,35,70'''


def num_gen(n):
    i = 0
    while i <= n:
        if i % 5 == 0 and i % 7 == 0:  # i % 35 == 0
            yield i
        i += 1

def cycle():
    n = int(input('n: '))
    lst = []
    [lst.append(str(num)) for num in num_gen(n)]

    return list_to_str(lst, ',')


print(cycle())