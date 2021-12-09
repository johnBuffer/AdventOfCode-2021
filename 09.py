from common.input_loader import load_input

DATA = [[int(i) for i in l] for l in load_input(9)]
is_valid = lambda x, y: (0 <= x < len(DATA[0])) and (0 <= y < len(DATA))
get_surr = lambda x, y: [(w, z) for w, z in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if is_valid(w, z)]
LOWS = [(x, y) for x in range(len(DATA[0])) for y in range(len(DATA)) if all(DATA[y][x] < DATA[oy][ox] for ox, oy in get_surr(x, y))]

# it works
def find_bassin(x, y, e = set()): return 0 if (x, y) in e else (e.add((x, y)), 1 + sum(find_bassin(w, z, e) for w, z in get_surr(x, y) if 9 > DATA[z][w] > DATA[y][x]))[1]

bassins = sorted([find_bassin(x, y) for x, y in LOWS])


print(sum(DATA[y][x] + 1 for x, y in LOWS))
print(bassins[-1] * bassins[-2] * bassins[-3])