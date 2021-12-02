def day_to_str(day: int):
    if day < 10:
        return '0' + str(day)
    return str(day)

def load_input(day: int):
    return open('inputs/{}.txt'.format(day_to_str(day))).read().split('\n')

def load_intput_as_ints(day: int):
    data = load_input(day)
    return [int(l) for l in data]