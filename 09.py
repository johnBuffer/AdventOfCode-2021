from common.input_loader import load_input

DATA = [[int(i) for i in l] for l in load_input(9)]
is_valid = lambda x, y: (0 <= x < len(DATA[0])) and (0 <= y < len(DATA))
get_surr = lambda x, y: [(w, z) for w, z in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if is_valid(w, z)]
LOWS = [(x, y) for x in range(len(DATA[0])) for y in range(len(DATA)) if all(DATA[y][x] < DATA[oy][ox] for ox, oy in get_surr(x, y))]

# it works
def get_bas(c, e=set()): return 0 if c in e else (e.add(c), 1 + sum(get_bas(o, e) for o in get_surr(*c) if 9 > DATA[o[1]][o[0]] > DATA[c[1]][c[0]]))[1]
BAS = sorted([get_bas(c) for c in LOWS])


print(sum(DATA[y][x] + 1 for x, y in LOWS))
print(BAS[-1] * BAS[-2] * BAS[-3])