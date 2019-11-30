def bank():

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
# ['D 100', 'W 200', 'D 300', 'D 300', 'W 200', 'D 100']
# 400




