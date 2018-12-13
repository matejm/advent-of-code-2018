import time
import os

with open('input') as file:
    data = [list(i[:-1]) for i in file.readlines()]

carts = []

i = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == '<':
            carts.append((i, x, y, 'L', 0))
            data[y][x] = '-'
        elif data[y][x] == '>':
            carts.append((i, x, y, 'R', 0))
            data[y][x] = '-'
        elif data[y][x] == 'v':
            carts.append((i, x, y, 'D', 0))
            data[y][x] = '|'
        elif data[y][x] == '^':
            carts.append((i, x, y, 'U', 0))
            data[y][x] = '|'
        i += 1

finished = False
collisions = []

broken = set()


new_data = [list(i) for i in data]
for cart in carts:
    new_data[cart[2]][cart[1]] = '0'

os.system('clear')
for line in new_data[:70]:
    print(''.join(line[:150]))
time.sleep(0.5)

while not finished and len(carts) > 1:
    new_carts = []

    carts = list(sorted(carts, key=lambda cart: (cart[1], cart[0])))
    for k in range(len(carts)):
        i, x, y, direction, turn = carts[k]

        if i in broken:
            continue

        new_loc = None
        new_data = None


        if direction == 'U':
            new_loc = (x, y - 1)

            if data[new_loc[1]][new_loc[0]] == '|':
                new_data = ('U', turn)
            elif data[new_loc[1]][new_loc[0]] == '\\':
                new_data = ('L', turn)
            elif data[new_loc[1]][new_loc[0]] == '/':
                new_data = ('R', turn)
            elif data[new_loc[1]][new_loc[0]] == '+':
                if turn == 0:                
                    new_data = ('L', (turn + 1) % 3)
                elif turn == 1:
                    new_data = ('U', (turn + 1) % 3)
                elif turn == 2:
                    new_data = ('R', (turn + 1) % 3)

        elif direction == 'D':
            new_loc = (x, y + 1)

            if data[new_loc[1]][new_loc[0]] == '|':
                new_data = ('D', turn)
            elif data[new_loc[1]][new_loc[0]] == '\\':
                new_data = ('R', turn)
            elif data[new_loc[1]][new_loc[0]] == '/':
                new_data = ('L', turn)
            elif data[new_loc[1]][new_loc[0]] == '+':
                if turn == 0:                
                    new_data = ('R', (turn + 1) % 3)
                elif turn == 1:
                    new_data = ('D', (turn + 1) % 3)
                elif turn == 2:
                    new_data = ('L', (turn + 1) % 3)

        elif direction == 'L':
            new_loc = (x - 1, y)

            if data[new_loc[1]][new_loc[0]] == '-':
                new_data = ('L', turn)
            elif data[new_loc[1]][new_loc[0]] == '\\':
                new_data = ('U', turn)
            elif data[new_loc[1]][new_loc[0]] == '/':
                new_data = ('D', turn)
            elif data[new_loc[1]][new_loc[0]] == '+':
                if turn == 0:                
                    new_data = ('D', (turn + 1) % 3)
                elif turn == 1:
                    new_data = ('L', (turn + 1) % 3)
                elif turn == 2:
                    new_data = ('U', (turn + 1) % 3)

        elif direction == 'R':
            new_loc = (x + 1, y)

            if data[new_loc[1]][new_loc[0]] == '-':
                new_data = ('R', turn)
            elif data[new_loc[1]][new_loc[0]] == '\\':
                new_data = ('D', turn)
            elif data[new_loc[1]][new_loc[0]] == '/':
                new_data = ('U', turn)
            elif data[new_loc[1]][new_loc[0]] == '+':
                if turn == 0:                
                    new_data = ('U', (turn + 1) % 3)
                elif turn == 1:
                    new_data = ('R', (turn + 1) % 3)
                elif turn == 2:
                    new_data = ('D', (turn + 1) % 3)


        # check collision
        for c in carts[k + 1 :] + new_carts:
            j, x, y, *_ = c
            if (x, y) == new_loc:
                collisions.append(new_loc)
                broken.add(i)
                broken.add(j)
                break


        if i not in broken:
            new_carts.append((i, new_loc[0], new_loc[1], new_data[0], new_data[1]))

    carts = new_carts
    
    new_data = [list(i) for i in data]
    for cart in carts:
        new_data[cart[2]][cart[1]] = '0'

    os.system('clear')
    for line in new_data[:70]:
        print(''.join(line[:150]))
    time.sleep(0.1)

print(','.join(map(str, collisions[0])))

print(','.join(map(str, carts[0][1: 3])), '<-- Might be 1 coord off')