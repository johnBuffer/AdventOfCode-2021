from common.input_loader import load_input

data = [sum(1 for v in [int(i) for i in load_input(6)[0].split(',')] if v == i) for i in range(9)]
def solve(f, d): return solve([(f[(i+1)%9] if i != 6 else f[0]+f[7]) for i in range(9)], d-1) if d else sum(f)

print(solve(data, 80))
print(solve(data, 256))
