import math


def robot():
    x = 0
    y = 0
    while True:
        inp = input().split()
        if not inp:
            break
        if inp[0] == 'UP':
            x -= int(inp[1])
        if inp[0] == 'DOWN':
            x += int(inp[1])
        if inp[0] == 'RIGHT':
            y += int(inp[1])
        if inp[0] == 'LEFT':
            y -= int(inp[1])
        res = round(math.sqrt(x ** 2 + y ** 2))

    return res


print(robot())