def compute(n):
    list_str = 'a+aa+aaa+aaaa'.replace('a', str(n)).split('+')
    return print(sum([int(elem) for elem in list_str]))
# sum([int(elem) for elem in 'a+aa+aaa+aaaa'.replace('a', '8').split('+')])

compute(9)