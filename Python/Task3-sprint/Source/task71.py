def calc():
    '''Question 71
    Please write a program which accepts basic mathematic expression from console and print the evaluation result.

        Example:
        If the following string is given as input to the program:
            35+3
        Then, the output of the program should be:
            38'''
    # operand = {'+': 'add',
    #            '-': 'sub',
    #            '*': 'mult',
    #            '/': 'div',
    #            '^': 'pow'
    #            }
    #
    # string = '7+8'  # input('Type a string: ')
    #
    # pattern = re.compile(r'(\d+)(\D)(\d+)')
    # matches = pattern.finditer(string)
    # print([match.group(2) for match in matches])
    expression = input('type math here: ')
    ans = eval(expression)

    return print(ans)

calc()
