def bank():
    '''uestion 17
    Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
    D 100
    W 200
    D means deposit while W means withdrawal.

    Suppose the following input is supplied to the program:
        D 300
        D 300
        W 200
        D 100
    Then, the output should be: 100-200+300+300-200+100 = 400!!!
    500'''

    trans = []

    while True:
        com = input()
        if len(com) == 0:
            break
        trans.append(com)
        print(trans)

    net = 0
    for item in trans:
        if 'D' in item:
            net += int(item.strip('D '))
        elif 'W' in item:
            net -= int(item.strip('W '))

    return net

print(bank())
# ['D 300', 'D 300', 'W 200', 'D 100']
# 400




