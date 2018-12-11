inp = 8979

grid = [[0 for i in range(301)] for j in range(301)]

for x in range(1, 301):
    for y in range(1, 301):
        rack = x + 10

        t = rack * y
        t += inp
        t *= rack

        grid[y][x] = (t // 100) % 10 - 5


m = -10000
mx, my = None, None

for x in range(1, 301 - 3):
    for y in range(1, 301 - 3):
        s = 0
        for a in range(3):
            for b in range(3):
                s += grid[y + b][x + a]

        if s > m:
            m = s
            mx = x
            my = y

print(f'First star: {mx},{my}')


sums = [[0 for i in range(301)] for j in range(301)]

for x in range(1, 301):
    for y in range(1, 301):
        sums[x][y] = sums[x][y - 1] + sums[x - 1][y] + grid[x][y] - sums[x - 1][y - 1]

m = -1000
m_data = None

for x in range(1, 301):
    for y in range(1, 301):
        for size in range(1, 301):
            if x + size > 300 or y + size > 300:
                break

            s = sums[y + size - 1][x + size - 1] - sums[y - 1][x + size - 1] - sums[y + size - 1][x - 1] + sums[y - 1][x - 1]

            if s > m:
                m = s
                m_data = x, y, size
                # print(s)

print('Second star:', ','.join(map(str, m_data)))