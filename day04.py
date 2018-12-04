import parse
from collections import defaultdict

with open('input') as file:
    lines = [tuple(parse.parse('[{:d}-{:d}-{:d} {:d}:{:d}] {}', i.strip())) for i in sorted(file.readlines())]

guards = defaultdict(lambda: [0 for i in range(60)])

last = None
guard = None

for line in lines:
    *_, h, m, s = line

    if s == 'wakes up':
        for i in range(last, m):
            guards[guard][i] += 1
    elif s == 'falls asleep':
        last = m
    else:
        guard = tuple(parse.parse('Guard #{:d} begins shift', str(s)))[0]


guard = max(guards.keys(), key=lambda g: sum(guards[g]))
minute = max(range(60), key=lambda m: guards[guard][m])

print(f'First star: {guard * minute}')

guard = max(guards.keys(), key=lambda g: max(guards[g]))
minute = max(range(60), key=lambda m: guards[guard][m])

print(f'Second star: {guard * minute}')