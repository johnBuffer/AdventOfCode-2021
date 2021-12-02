from common.input_loader import load_input


data = load_input(2)


def solve_1():
    x, y, c = 0, 0, {'up': (0, -1), 'down': (0, 1), 'forward': (1, 0)}
    for instr, value in [(i, int(v)) for i, v in [l.split(' ') for l in data]]:
        x += value * c[instr][0]
        y += value * c[instr][1]
    return x * y


def solve_2():
    x, y, a, c = 0, 0, 0, {'up': (0, 0, -1), 'down': (0, 0, 1), 'forward': (1, 1, 0)}
    for instr, value in [(i, int(v)) for i, v in [l.split(' ') for l in data]]:
        x += value * c[instr][0]
        y += value * c[instr][1] * a
        a += value * c[instr][2]
    return x * y


print(solve_1())
print(solve_2())
