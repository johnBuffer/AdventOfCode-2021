from common.input_loader import load_input

numbers = [int(i) for i in load_input(7)[0].split(',')]
def solve(n, f): return min(sum(f(abs(i - v)) for i in n) for v in range(len(n)))
    
print(solve(numbers, lambda x: x))
print(solve(numbers, lambda x: int(x*(x+1)/2)))
