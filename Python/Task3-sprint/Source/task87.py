def odd_list(lst=None):
    '''Question 87
    Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].'''

    lst_res = list(filter(lambda n: n % 2 != 0, lst))
    return lst_res


lst = [5, 6, 77, 45, 22, 12, 24]
print(odd_list(lst))