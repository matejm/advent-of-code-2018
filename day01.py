
with open('input.txt') as file:
    lines = file.readlines()

print(f'First star: {sum(map(int, lines))}')

all_fs = set([0])
current = 0
found = False

while not found:
    for f in map(int, lines):
        current += f
        if current in all_fs:
            found = True
            break

        all_fs.add(current)

print(f'Second star: {current}')
