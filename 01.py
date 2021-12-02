from common.input_loader import load_intput_as_ints

data = load_intput_as_ints(day=1)

def solve_1():
    return sum([data[i] > data[i-1] for i in range(1, len(data))])


def solve_2():
    return sum([sum(data[i:i+3]) > sum(data[i-1:i+2]) for i in range(1, len(data) - 2)])

print(solve_1())
print(solve_2())

