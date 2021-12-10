from common.input_loader import load_input

data = load_input(10)
T = {'<': '>', '(': ')', '{': '}', '[': ']'}
S = {'>': 25137, ')': 3, '}': 1197, ']': 57}


def parse(l, s=''):
    return (0, s) if l == '' else parse(l[1:], s + l[0]) if l[0] in T else (S[l[0]], '') if l[0] != T[s[-1]] else parse(l[1:], s[:-1])


def calc_score(l, s=0):
    return calc_score(l[:-1], 5 * s + {'<': 4, '(': 1, '{': 3, '[': 2}[l[-1]]) if len(l) else s


print(sum(parse(l)[0] for l in data))
scores = sorted([calc_score(l) for l in [r for s, r in [parse(l) for l in data] if s == 0]])
print(scores[len(scores)//2])
