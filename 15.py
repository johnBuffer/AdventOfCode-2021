from common.input_loader import load_input


data = [[int(c) for c in l] for l in load_input(15)]
is_valid = lambda c: 0 <= c[0] < len(data[0]) and 0 <= c[1] < len(data)


def generate_cave():
    res = [[(c + i - 1)%9 + 1 for i in range(5) for c in l] for l in data]    
    return [[(c + i - 1)%9 + 1 for c in l] for i in range(5) for l in res]


def solve_1():
    current = (len(data[0])-1, len(data)-1)
    to_visit = [current]
    dist = [[-1 for _ in l] for l in data]
    dist[current[1]][current[0]] = 0

    while True:
        to_visit.remove(current)
        x, y = current
        next = [(px, py) for px, py in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if is_valid((px, py))]
        for nx, ny in next:
            if dist[ny][nx] == -1:
                to_visit.append((nx, ny))
                dist[ny][nx] = dist[y][x] + data[ny][nx]
        if len(to_visit):
            current = to_visit[0]
            nx, ny = current
            current_min = dist[ny][nx]
            for nx, ny in to_visit[1:]:
                if dist[ny][nx] < current_min:
                    current_min = dist[ny][nx]
                    current = (nx, ny)
        else:
            break
    
    tot = 0
    c = (0, 0)
    while c != (len(data[0])-1, len(data)-1):
        x, y = c
        next = [(px, py) for px, py in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if is_valid((px, py))]
        if len(next):
            c = next[0]
            nx, ny = c
            current_min = dist[ny][nx]
            for nx, ny in next[1:]:
                if dist[ny][nx] < current_min:
                    current_min = dist[ny][nx]
                    c = (nx, ny)
            tot += data[c[1]][c[0]]
        else:
            break
    return tot


print(solve_1())
data = generate_cave()
print(solve_1())
