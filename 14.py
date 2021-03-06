from common.input_loader import load_input
from collections import defaultdict, Counter

data = load_input(14)
INS = {a: b for a, b in [l.split(' -> ') for l in data[2:]]}


def process(chain, count):
    res = defaultdict(int)
    for e, r in INS.items():
        res[e[0] + r] += chain[e]
        res[r + e[1]] += chain[e]
        count[r] += chain[e]
    return res


def solve(iter):
    d, count = defaultdict(int), defaultdict(int, Counter(data[0]))
    for i in range(len(data[0]) - 1): d[data[0][i:i+2]] += 1
    for _ in range(iter): d = process(d, count)
    return (max(count.values()) - min(count.values()))


print(solve(10))
print(solve(40))