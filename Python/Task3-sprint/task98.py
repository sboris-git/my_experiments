from modul import list_to_str


def drop_even(string):
    ''' Question 98
    Please write a program which accepts a string from console and print the characters that have even indexes.

    Example:
    If the following string is given as input to the program:
        H1e2l3l4o5w6o7r8l9d
    Then, the output of the program should be:
        Helloworld'''

    cleaned = [char for (i, char) in enumerate(list(string)) if i % 2 == 0 ]
    # cleaned = string[::2]

    return list_to_str(cleaned, '')


string = 'H1e2l3l4o5w6o7r8l9d'
print(drop_even(string))