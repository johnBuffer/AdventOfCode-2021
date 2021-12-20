from common.input_loader import load_input

data = load_input(20)
A, pict = [str(int(c == '#')) for c in data[0]], {(x, y): str(int(c == '#')) for y, l in enumerate(data[2:]) for x, c in enumerate(l)}
def bnd(d, op, i=0): return op(k[i] for k in d) + (2 if op == max else -1)
def apply(p, d): return {(x, y): A[int(''.join(p.get((ox, oy), d) for oy in range(y-1, y+2) for ox in range(x-1, x+2)), 2)] for y in range(bnd(p, min, 1), bnd(p, max, 1)) for x in range(bnd(p, min), bnd(p, max))}
def enhance(p, count, i=0): return p if count == 0 else enhance(apply(p, str(i%2)), count-1, i+1)


print(sum(int(v) for v in enhance(pict, 2).values()))
print(sum(int(v) for v in enhance(pict, 50).values()))
