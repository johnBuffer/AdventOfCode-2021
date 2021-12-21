from common.input_loader import load_input
from collections import deque


def solve_1(p, s=(0, 0), rolls=0, i=0):
    if max(s) >= 1000: return min(s) * rolls
    t = sum(range(rolls+1, rolls+4))
    np = (p[0] + (1-i)*t, p[1] + i*t) # Add move to the current player's position
    ns = (s[0] + (1-i)*((np[0]-1)%10+1), s[1] + i*((np[1]-1)%10+1)) # Increase current player's score
    return solve_1(np, ns, rolls + 3, 1-i)
   

def solve_2(p):
    t1, t2, stack = 0, 0, deque([(0, p, (0, 0), 1)])
    while len(stack) > 0:
        i, p, s, u = stack.pop()
        if s[0] >= 21: t1 += u
        elif s[1] >= 21: t2 += u
        else:
            for t, c in {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}.items():
                np = (p[0] + (1-i)*t, p[1] + i*t) # Add move to the current player's position
                ns = (s[0] + (1-i)*((np[0]-1)%10+1), s[1] + i*((np[1]-1)%10+1)) # Increase current player's score
                stack.append((1-i, np, ns, u*c))
    return max(t1, t2)


data = [int(l[28:]) for l in load_input(21)]
print(solve_1(data))
print(solve_2(data))
