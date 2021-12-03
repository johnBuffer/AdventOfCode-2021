from common.input_loader import load_input


data = [[int(i) for i in l] for l in load_input(3)]


def max_i(array, i):
    return int(len(array) - 2 * sum(v[i] for v in array) <= 0)


def get_number(bin):
    return int(''.join(str(i) for i in bin), 2)


def search(d, i, comp):
    return d[0] if len(d) == 1 else search([l for l in d if l[i] == comp(max_i(d, i))], i + 1, comp)


def solve_1():
    gamma = [max_i(data, k) for k in range(len(data[0]))]
    return get_number(gamma) * get_number([1-i for i in gamma])


print(solve_1())
print(get_number(search(data, 0, lambda x: x)) * get_number(search(data, 0, lambda x: 1-x)))
