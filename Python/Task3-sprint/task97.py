def rev_list(string = None):
    '''Question 97
    Please write a program which accepts a string from console and print it in reverse order.

    Example:
    If the following string is given as input to the program:
        rise to vote sir
    Then, the output of the program should be:
        ris etov ot esir'''

    string = input('Type a string: ')
    string = ''.join(reversed(string))
    # string = string[::-1]

    return string


print(rev_list())
