from common.input_loader import load_input


data = [(a, b) for a, b in [l.split('-') for l in load_input(12)]]
M = {a: set(e for s, e in data if s == a) | set(s for s, e in data if e == a) for a in set(v[0] for v in data)}
get_nxt = lambda a, d, cs :{k: [c for c in v if c != a or a == d or not c.islower()] for k, v in cs.items()}


def walk(cs, a='start', d='', p=''):
    return {p} if a == 'end' else set().union(*[walk(get_nxt(a, d, cs), c, '' if a == d else d, p + a) for c in cs[a]])


print(len(walk(M)))
print(len(set().union(*[walk(M, d=c) for c in set(M) if c.islower() and c != 'start'])))
