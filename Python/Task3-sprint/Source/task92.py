def drop_elem(lst):
    '''Question 92
    By using list comprehension, please write a program to print the list after
    removing the value 24 in [12,24,35,24,88,120,155].'''

    filtered = [elem for elem in lst if elem != 24]

    return filtered


lst = [12, 24, 35, 70, 88, 120, 155]
print(drop_elem(lst))