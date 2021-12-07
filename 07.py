from common.input_loader import load_input

numbers = [int(i) for i in load_input(7)[0].split(',')]
solve = lambda n, f: min(sum(f(abs(i - v)) for i in n) for v in range(max(n)))
    
print(solve(numbers, lambda x: x))
print(solve(numbers, lambda x: x*(x+1)//2))
