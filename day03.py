import parse
from collections import defaultdict

with open('input') as file:
    queries = [list(parse.parse('#{:d} @ {:d},{:d}: {:d}x{:d}', i.strip())) for i in file.readlines()]

d = defaultdict(int)
count = 0

for i in range(len(queries)):
    index, y, x, h, w = queries[i]

    for a in range(x, x + w):
        for b in range(y, y + h):
            if d[(a, b)] == 1:
                count += 1

            d[(a, b)] += 1


print('First star:', count)

for q in queries:
    index, y, x, h, w = q

    ok = True
    for a in range(x, x + w):
        for b in range(y, y + h):
            if d[(a, b)] != 1:
                ok = False
        if not ok:
            break

    if ok:
        print('Second star:', index)
        break