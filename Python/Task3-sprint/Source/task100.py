import numpy as np


def sleq():
    '''Question 100
    Write a program to solve a classic ancient Chinese puzzle: 
    We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
    How many rabbits and how many chickens do we have?

    2*x + 4*y = 94
    x + y = 35
    '''

    a = np.array([[2, 4],
                  [1, 1]])
    b = np.array([94, 35])
    x = np.linalg.inv(a).dot(b)

    return x


print(sleq())