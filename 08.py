from common.input_loader import load_input
import itertools

data  = [[a.split(' ') for a in l.split(' | ')] for l in load_input(8)]
SEG   = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
EZ    = {2: 1, 3: 7, 4: 4}
PERMS = list(itertools.permutations('abcdefg', 7))


def convert(seg, hyp): return ''.join(sorted(hyp['abcdefg'.index(i)] for i in seg))
def decode_hyp(seg, hyp): return SEG.index(convert(seg, hyp)) if convert(seg, hyp) in SEG else None
def find_possible(l, hyp): return [h for h in hyp if all(decode_hyp(d, h) == EZ[len(d)] for d in l[0] if len(d) in EZ)]


def decode(l, hyp):
    valid = [h for h in find_possible(l, hyp) if set(decode_hyp(d, h) for d in l[0]) == {i for i in range(10)}][0]
    return int(''.join(str(decode_hyp(dd, valid)) for dd in l[1]))


print(sum(int(len(d) in [2, 3, 4, 7]) for l in data for d in l[1]))
print(sum(decode(l, PERMS) for l in data))
