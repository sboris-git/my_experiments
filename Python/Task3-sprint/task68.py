from collection import list_to_str


def even_num_gen(n):
    i = 0
    while i <= n:
        if i%2 == 0:
            yield i
        i += 1

def cycle():
    n = int(input('n: '))
    lst = []
    [lst.append(str(num)) for num in even_num_gen(n)]

    return list_to_str(lst, ',')


print(cycle())