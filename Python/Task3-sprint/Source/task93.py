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