import parse
from collections import defaultdict

with open('input') as file:
    edges = [tuple(parse.parse('Step {} must be finished before step {} can begin.', i.strip())) for i in file.readlines()]


vertices = set()
graph = defaultdict(set)
rgraph = defaultdict(set)

for a, b in edges:
    vertices.add(a)
    vertices.add(b)

    graph[b].add(a)
    rgraph[a].add(b)

s = ''

while vertices:
    candidates = []

    for v in vertices:
        if len(graph[v]) == 0:
            candidates.append(v)

    candidates.sort()

    c = candidates[0]

    s += c

    vertices.remove(c)

    for v in rgraph[c]:
        graph[v].remove(c)

    graph[c] = set()
    rgraph[c] = set()

print('First star:', s)





vertices = set()
graph = defaultdict(set)
rgraph = defaultdict(set)

for a, b in edges:
    vertices.add(a)
    vertices.add(b)

    graph[b].add(a)
    rgraph[a].add(b)

remove = []

t = 0
workers = 5

finished = set()

while vertices:
    candidates = []

    remove.sort()

    while remove and remove[0][0] <= t:
        _, v, c = remove.pop(0)
        graph[v].remove(c)
        
        if c not in finished:
            workers += 1
            finished.add(c)

    if workers == 0:
        t += 1
        continue

    for v in vertices:
        if len(graph[v]) == 0:
            candidates.append(v)

    if candidates == []:
        t += 1
        continue


    for c in candidates:
        if workers == 0:
            break

        workers -= 1
        vertices.remove(c)

        for v in rgraph[c]:
            remove.append((t + ord(c) - ord('A') + 60 + 1, v, c))

        if not rgraph[c]:
            t += ord(c) - ord('A') + 60

        graph[c] = set()
        rgraph[c] = set()

    t += 1

while remove:
    while remove and remove[0][0] <= t:
        _, v, c = remove.pop(0)
        graph[v].remove(c)
        
        if c not in finished:
            workers += 1
            finished.add(c)
    t += 1

print('Second star:', t)
