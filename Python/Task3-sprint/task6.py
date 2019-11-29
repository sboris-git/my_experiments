import math
from collection import list_to_str

def sqroot(d=None):
    c = 50
    h = 30
    q = []
    inp_data = input('d= ')
    for d in inp_data.split(','):
        q.append(round(math.sqrt((2*c*int(d)/h))))
    return list_to_str(q, ',')

print(sqroot())