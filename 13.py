from common.input_loader import load_input

PTS = [tuple(map(int, l.split(','))) for l in load_input(13) if len(l) and 'fold' not in l]
FLD = [(int(l[11]=='x') * (int(l[13:]) + 1), int(l[11]=='y') * (int(l[13:]) + 1)) for l in load_input(13) if 'fold' in l]
scan = lambda s, a: range(max(c[a] for c in s), -1, -1)


def fold(c, sheet):
    return {(x-c[0] if x>=c[0] else c[0]-x-2, y-c[1] if y>=c[1] else c[1]-y-2) for x, y in sheet}


def solve(fs, s):
    return solve(fs[1:], fold(fs[0], s)) if fs else [['█' if (x, y) in s else ' ' for x in scan(s, 0)] for y in scan(s, 1)]


print(len(fold(FLD[0], PTS)))
for l in solve(FLD, PTS): print(''.join(l))
