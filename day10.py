import parse
import os
import time

with open('input') as file:
    data = [tuple(map(int, parse.parse('position=<{},{}> velocity=<{},{}>', i.strip()))) for i in file.readlines()]

points = [(x, y) for y, x, *_ in data]
velocity = [(vx, vy) for *_, vy, vx in data]

mv, mh = 1e9, 1e9

for i in range(50000):

    width = max([x for x, y in points]) - min([x for x, y in points])
    height = max([y for x, y in points]) - min([y for x, y in points])

    if width <= mv and height <= mh:
        mv = width
        mh = height

        if width == 9:
            grid = [[' ' for _ in range(height + 10)] for __ in range(width + 10)]
            c = 0

            for x, y in points:
                x -= min([y for x, y in points]) - 3
                y -= min([x for x, y in points]) - 3

                if 0 <= x and x <= width + 5 and 0 <= y and y <= height + 5:
                    grid[x][y] = '#'
                    c += 1

            for line in grid:
                print(''.join(line))
            
            print('Second star:', i)
            break

    for a in range(len(points)):
        x, y = points[a]
        vx, vy = velocity[a]

        points[a] = (x + vx, y + vy)

