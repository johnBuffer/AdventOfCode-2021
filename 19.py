from common.input_loader import load_input


data, scanners, current = load_input(19) + [''], [], []
for l in data:
    if '---' in l: current = []
    elif l == '': scanners.append([tuple(int(c) for c in p) for p in current])
    else: current.append(l.split(','))

rotates = [
    lambda x, y, z, c: [(x, y, z), (x, -z, y), (x, -y, -z), (x, z, -y)][c],
    lambda x, y, z, c: [(x, y, z), (-z, y, x), (-x, y, -z), (z, y, x)][c],
    lambda x, y, z, c: [(x, y, z), (-y, x, z), (-x, -y, -z), (y, -x, z)][c]
]

def rotate(pts, axe, count): return [rotates[axe](*p, count) for p in pts]
def translate(pts, vx, vy, vz): return [(x+vx, y+vy, z+vz) for x, y, z in pts]
def diff(ax, ay, az, bx, by, bz): return (ax-bx, ay-by, az-bz)
def man_dist(a, b): return sum(abs(x) for x in diff(*a, *b))


def gen_try_list():
    t, tried, res = [(i, j, k) for i in range(4) for j in range(4) for k in range(4)], set(), []
    for i, j, k in t: 
        p = rotates[2](*rotates[1](*rotates[0](1, 2, 3, i), j), k)
        if p not in tried:
            tried.add(p)
            res.append((i, j, k))
    return res


to_try = gen_try_list()
def match(world, others):
    max_o, max_id, max_set, max_offset = 0, 0, None, None
    for scan_id, scan in enumerate(others):
        for i, j, k in to_try:
            pts = [rotates[2](*rotates[1](*rotates[0](*p, i), j), k) for p in scan]
            for pw in world:
                for ps in pts:
                    new_set = set(translate(pts, *diff(*pw, *ps)))
                    overlaps = len(world) + len(new_set) - len(new_set | world)
                    if overlaps > max_o: max_o, max_id, max_set, max_offset = overlaps, scan_id, new_set, diff(*pw, *ps)
    return max_id, max_set, max_offset


remaining = scanners[1:]
total = set(scanners[0])
pos = [(0, 0, 0)]


while len(remaining) > 0:
    nxt, pts, off = match(total, remaining)
    remaining.pop(nxt)
    total = total | pts
    pos.append(off)


print(len(total))
print(max(man_dist(a, b) for a in pos for b in pos))
