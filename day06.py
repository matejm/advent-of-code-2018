with open('input') as file:
    points = [tuple(map(int, i.split(', '))) for i in file.readlines()]

def d(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

grid = [[-1 for i in range(1100)] for j in range(1100)]

count = [0 for i in range(len(points))]

on_edge = [False for i in range(len(points))]

for i in range(1100):
    print(i)
    for j in range(1100):
        m = 1e9
        mi = None
        tie = False

        for pi, p in enumerate(points):
            if d(p, (i - 400, j - 400)) <= m:
                if d(p, (i - 400, j - 400)) == m:
                    tie = True
                else:
                    m = d(p, (i - 400, j - 400))
                    tie = False
                    mi = pi

        if not tie:
            count[mi] += 1
            grid[i][j] = mi


for i in range(1100):
    point = grid[i][0]
    if point != -1:
        on_edge[point] = True

    point = grid[i][-1]
    if point != -1:
        on_edge[point] = True

    point = grid[0][i]
    if point != -1:
        on_edge[point] = True

    point = grid[-1][i]
    if point != -1:
        on_edge[point] = True

print('First star:', max([j for i, j in enumerate(count) if not on_edge[i]]))

c = 0

for i in range(-100, 700):
    print(i)
    for j in range(-100, 700):
        size = 0

        for p in points:
            a, b = p
            dist = abs(a - i) + abs(b - j)
            size += dist

        if size < 10000:
            c += 1


print('Second star:', c)
