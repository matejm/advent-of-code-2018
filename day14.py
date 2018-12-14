inp = 409551

i = 0
j = 1
l = [3, 7]

inp2 = list(map(int, str(inp)))

first = False

while True:
    r = str(l[i] + l[j])

    for c in r:
        l.append(int(c))

    if l[-1] == inp2[-1] or l[-2] == inp2[-1]:
        if inp2 == l[-len(inp2):]:
            print('Second star:', len(l) - len(inp2))
            break
        elif inp2 == l[-len(inp2) - 1: -1]:
            print('Second star:', len(l) - len(inp2) - 1)
            break

    i = (i + 1 + l[i]) % len(l)
    j = (j + 1 + l[j]) % len(l)

    if not first and len(l) > inp + 10:
        print('First star:', ''.join(map(str, l[inp : inp + 10])))
        first = True
