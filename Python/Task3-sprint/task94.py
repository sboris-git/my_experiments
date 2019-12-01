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