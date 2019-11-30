def compute(n):
    list_str = 'a+aa+aaa+aaaa'.replace('a', str(n)).split('+')
    ans = sum([int(elem) for elem in list_str])
    return ans
# sum([int(elem) for elem in 'a+aa+aaa+aaaa'.replace('a', '8').split('+')])

print(compute(9))