from common.input_loader import load_input

data = load_input(4)
win = lambda g, n: any(set(g[i:i+5]).issubset(n) for i in range(0, 25, 5)) or any(set(g[i::5]).issubset(n) for i in range(0, 5)) # LEL
NS = [int(i) for i in data[0].split(',')]
GS = [[int(c) for c in ' '.join(data[i:i+6][:5]).split(' ') if len(c)] for i in range(2, len(data), 6)]


def solve(gs = GS, s = [], n = set(NS[:5]), i = 5):
    return s if i == len(NS) else solve([g for g in gs if not win(g, n)], s + [NS[i-1] * sum(set(g) - n) for g in gs if win(g, n)], n|{NS[i]}, i+1)


print(solve()[0])
print(solve()[-1])
