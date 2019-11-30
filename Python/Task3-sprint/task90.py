def matrix():
    '''Question 90
    By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
    '''

    array = [[[0]*3]*5]*8
    #array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]

    return array


for slice in matrix():
    print('-' * 10 )
    for flat in slice:
        print(flat)
