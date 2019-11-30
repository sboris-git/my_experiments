from bisect import bisect_left

def half_div_search(a, target):
    '''Question 72
    Locate the leftmost value exactly equal to target
    https://docs.python.org/3/library/bisect.html

    Please write a binary search function which searches an item in a sorted list.
    The function should return the index of element to be searched in the list.
    '''

    a.sort()
    i = bisect_left(a, target)
    if i != len(a) and a[i] == target:
        return i
    else:
        return -1


sequence = [1, 25, 4, 6, 8, 10, 46, 1, 5]

print(half_div_search(sequence, 3))