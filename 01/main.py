file_data = open('input.txt').read().split('\n')
data = [int(l) for l in file_data]


def solve_1(data):
    return sum([data[i] > data[i-1] for i in range(1, len(data))])


def solve_2(data):
    return sum([sum(data[i:i+3]) > sum(data[i-1:i+2]) for i in range(1, len(data) - 2)])


print(solve_1(data))
print(solve_2(data))
