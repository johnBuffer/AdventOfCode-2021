import math
from common.input_loader import load_input


def find_coma(x, d=0, r=1):
    return r if (x[0] == ',' and d == 0) else find_coma(x[1:], d + (x[0] == '[') - (x[0] == ']'), r + 1)


def parse_num(l, d=0, id=''):
    if l[0] != '[': return [(int(l), id)]
    coma = find_coma(l[1:-1])
    return parse_num(l[1:coma], d+1, id+'l') + parse_num(l[coma+1:-1], d+1, id+'r')


def explode(x):
    for i, (n, id) in enumerate(x):
        if len(id) > 4 and is_left(x, i):
            n_right, id_right = x[i+1]
            if i > 0: x[i-1] = (x[i-1][0]+n, x[i-1][1])
            if i < len(x) - 2: x[i+2] = (n_right+x[i+2][0], x[i+2][1])
            x.remove((n_right, id_right))
            x[i] = (0, id[:-1])
            return True
    return False


def split(x):
    for i, (n, id) in enumerate(x):
        if n > 9:
            x.remove((n, id))
            for v in [(int(math.ceil(n/2)), id+'r'), (n//2, id+'l')]: x.insert(i, v)
            return True
    return False


def is_left(x, i):
    if i < len(x)-1: return x[i][1][:-1] == x[i+1][1][:-1]
    return False


def calc_ampl(x):
    while len(x) > 1:
        for i, (n, id) in enumerate(x):
            if is_left(x, i):
                n_right, id_right = x[i+1]
                for v in [(n, id), (n_right, id_right)]: x.remove(v)
                x.insert(i, (3*n + 2*n_right, id[:-1]))
    return x[0][0]


def add(x, y):
    o, stop = [(n, 'l' + id) for n, id in x] + [(n, 'r' + id) for n, id in y], False
    while not stop: stop = (not explode(o) and not split(o))
    return o


def solve_1(d, res):
    return calc_ampl(res) if len(d) == 0 else solve_1(d[1:], add(res, d[0]))


data = [parse_num(l) for l in load_input(18)]
print(solve_1(data[1:], data[0]))
print(max(calc_ampl(add(d1, d2)) for i, d1 in enumerate(data) for j, d2 in enumerate(data) if j != i))
