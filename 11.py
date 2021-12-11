from common.input_loader import load_input
from collections import defaultdict


DATA = [[int(i) for i in l] for l in load_input(11)]


def add(x, y, grid):
    if grid[(x, y)] >= 10:
        grid[(x, y)] = 0
        for c in [(x + ox, y + oy) for oy in range(-1, 2) for ox in range(-1, 2)]:
            if grid[c] > 0:
                grid[c] += 1
                add(*c, grid)


def simulate(grid):
    for c in [(x, y) for x in range(10) for y in range(10)]: grid[c] += 1
    for c in [(x, y) for x in range(10) for y in range(10)]: add(*c, grid)
    return sum(grid[(x, y)] == 0 for x in range(10) for y in range(10))


def solve_1(grid):
    return sum(simulate(grid) for _ in range(100))


def solve_2(grid, s=0, i=0):
    return i if s == 100 else solve_2(grid, simulate(grid), i + 1)
    

print(solve_1(defaultdict(int, {(x, y): c for y, l in enumerate(DATA) for x, c in enumerate(l)})))
print(solve_2(defaultdict(int, {(x, y): c for y, l in enumerate(DATA) for x, c in enumerate(l)})))
