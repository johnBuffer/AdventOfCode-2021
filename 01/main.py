file_data = open('input.txt').read().split('\n')
data = [int(l) for l in file_data]


def solve_1(data):
    return sum([data[i + 1] > data[i] for i, _ in enumerate(data[1:])])


def solve_2(data):
    return sum([sum(data[i+1:i+4]) > sum(data[i:i+3]) for i, _ in enumerate(data[1:-2])])


print(solve_1(data))
print(solve_2(data))
