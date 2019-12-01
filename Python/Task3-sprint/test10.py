from modul import list_to_str


def wsd_text(text):
    '''Write a program that accepts a sequence of whitespace separated words
     as input and prints the words after removing all duplicate words and sorting them alphanumerically.
    Suppose the following input is supplied to the program:
    hello world and practice makes perfect and hello world again
    Then, the output should be:
    again and hello makes perfect practice world'''

    ans = list_to_str(sorted(set(text.split())), ' ')
    return ans


print(wsd_text('hello world and practice makes perfect and hello world again'))