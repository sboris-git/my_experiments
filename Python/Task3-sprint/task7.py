def twodigits(x, y):
    array = []
    for i in range(0, x):
        temp = []
        for j in range(0, y):
            temp.append(i*j)
        array.append(temp)
    print(array)

twodigits(3,5)
