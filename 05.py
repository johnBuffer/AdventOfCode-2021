from collections import defaultdict
from common.input_loader import load_input

LS = [list(map(lambda x: int(x), l.replace(' -> ', ',').split(','))) for l in load_input(5)]
sign = lambda x1, x2: 1 if x1 < x2 else -1 if x1 > x2 else 0


def pts(x1, y1, x2, y2):
    return [(x1, y1)] + (pts(x1 + sign(x1, x2), y1 + sign(y1, y2), x2, y2) if x1!=x2 or y1!=y2 else [])


def solve(grid, filter):
    for x, y in sum((pts(*l) for l in LS if filter(*l)), []): grid[(x, y)] += 1
    return sum(1 for v in grid.values() if v > 1)


print(solve(defaultdict(int), lambda x1, y1, x2, y2: x1 == x2 or y1 == y2))
print(solve(defaultdict(int), lambda *args: True))
