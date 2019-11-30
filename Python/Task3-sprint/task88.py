def drop_35(lst=None):
    '''Question 88
    By using list comprehension, please write a program to print the list after removing delete
    numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
    '''

    target = list(filter(lambda x: x % 35 != 0, lst))

    return target


lst = [12, 24, 35, 70, 88, 120, 155]
print(drop_35(lst))