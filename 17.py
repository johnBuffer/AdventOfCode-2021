import math, re
from common.input_loader import load_input


r = re.search(r'.*x=(.*)\.\.(.*), y=(.*)\.\.(.*)', load_input(17)[0])
min_x, max_x, min_y, max_y = [int(x) for x in (r.group(1), r.group(2), r.group(3), r.group(4))]


def hit(x, y): return (min_x <= x <= max_x) and (min_y <= y <= max_y)
def mss(x, y, vx): return x > max_x or y < min_y or (x < min_x and vx == 0)


def simulate(initial_speed, num_step):
    x, y, vx, vy, h = 0, 0, *initial_speed, 0
    for _ in range(num_step):
        x, y, h, vx, vy = x + vx, y + vy, max(h, y), vx - (vx > 0), vy - 1
        if hit(x, y): return h
        if mss(x, y, vx): break
    return None


print(max(h for h in (simulate((vx, vy), 1000) for vx in range(math.ceil(math.sqrt(0.5+2*min_x)-0.5), max_x+1) for vy in range(200)) if h is not None))
print(sum(simulate((vx, vy), 1000) is not None for vx in range(math.ceil(math.sqrt(0.5+2*min_x)-0.5), max_x+1) for vy in range(min_y, 200)))
