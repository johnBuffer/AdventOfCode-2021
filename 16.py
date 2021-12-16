import functools
from common.input_loader import load_input


def load_packets(data, start, end, res):
    if (end - start) > 6:
        p = Packet(data, start); return load_packets(data, p.get_end(), end, res + [p])
    return res, 22 + sum(p.size for p in res)


def load_n_packets(data, start, n, res):
    if n > 0:
        p = Packet(data, start); return load_n_packets(data, p.get_end(), n-1, res + [p])
    return res, 18 + sum(p.size for p in res)


class Packet:
    def __init__(self, data, offset=0, indent=''):
        self.indent, self.offset = indent, offset
        tmp = data[offset:]
        self.version = int(tmp[:3], 2)
        self.type_id = int(tmp[3:6], 2)
        if self.type_id == 4: self.decode_num(data)
        else: self.decode_op(data)

    def get_end(self):
        return self.offset + self.size

    def decode_num(self, data):
        bits, tmp = '', data[self.offset + 6:]
        while tmp[0] == '1': bits, tmp = bits + tmp[1:5], tmp[5:]
        self.value = int(bits + tmp[1:5], 2)
        self.size = 6 + 5*(len(bits + tmp[1:5])//4)

    def decode_op(self, data):
        tmp = data[self.offset + 6:]
        type_length, tmp = int(tmp[0], 2), tmp[1:]
        if type_length == 0:
            packets_size, tmp = int(tmp[:15], 2), tmp[15:]
            start = self.offset + 22
            self.subpackets, self.size = load_packets(data, start, start + packets_size, [])
        else:
            self.subpackets, self.size = load_n_packets(data, self.offset + 18, int(tmp[:11], 2), [])

    def get_sum(self):
        return self.version if self.type_id == 4 else self.version + sum(p.get_sum() for p in self.subpackets)
    
    def get_value(self): # yes yes
        return [lambda p: sum(s.get_value() for s in p.subpackets),
              lambda p: functools.reduce(lambda x, y: x * y, [s.get_value() for s in p.subpackets]),
              lambda p: min(s.get_value() for s in p.subpackets),
              lambda p: max(s.get_value() for s in p.subpackets),
              lambda p: p.value,
              lambda p: int(p.subpackets[0].get_value() > p.subpackets[1].get_value()),
              lambda p: int(p.subpackets[0].get_value() < p.subpackets[1].get_value()),
              lambda p: int(p.subpackets[0].get_value() == p.subpackets[1].get_value())][self.type_id](self)
        

p = Packet(''.join([format(n, '04b') for n in [int(c, 16) for c in load_input(16)[0]]]))
print(p.get_sum())
print(p.get_value())
