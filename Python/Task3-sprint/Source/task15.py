def compute(n):
    '''Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

    Suppose the following input is supplied to the program:
        9
    Then, the output should be:
        11106'''

    list_str = 'a+aa+aaa+aaaa'.replace('a', str(n)).split('+')
    ans = sum([int(elem) for elem in list_str])

    return ans

# sum([int(elem) for elem in 'a+aa+aaa+aaaa'.replace('a', '8').split('+')])

print(compute(9))