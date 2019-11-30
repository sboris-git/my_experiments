def calc(n=None):
    '''Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

    Example:
        If the following n is given as input to the program:
            5
        Then, the output of the program should be:
            3.55
        In case of input data being supplied to the question, it should be assumed to be a console input.'''

    n = int(input('type n: '))
    sum = 0.0
    for number in range(1, n + 1):
        sum += float(number / (number + 1))
    return round(sum, 2)


print(calc())