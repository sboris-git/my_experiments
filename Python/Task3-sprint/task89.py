def drop_even(lst):
    '''Question 89
    By using list comprehension, please write a program to print the list after
    removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].'''

    filtered = [elem for (i, elem) in enumerate(lst) if i % 2 != 0]

    return filtered


lst = [12, 24, 35, 70, 88, 120, 155]
print(drop_even(lst))