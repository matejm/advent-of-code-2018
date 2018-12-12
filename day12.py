def next_generation(state):
    state2 = ['.' for i in range(len(state))]

    for i in range(2, len(initial_state) - 3):
        state2[i] = d[''.join(state[i - 2 : i + 3])]

    return state2

def get_value(state):
    s = 0
    for i, c in enumerate(state):
        if c == '#':
            s += i - 200
    return s


with open('input') as file:
    lines = file.readlines()


initial_state = list(lines[0].strip().split()[-1])

d = {}

for line in lines[2:]:
    key, value = line.strip().split(' => ')
    d[key] = value

initial_state = ['.'] * 200 + initial_state + ['.'] * 200

for _ in range(20):
    initial_state = next_generation(initial_state)


print('First star:', get_value(initial_state))

n_generations = 50000000000

n = 150

for i in range(n - 20):
    initial_state = next_generation(initial_state)

s = get_value(initial_state) + sum(map(lambda x: x == '#', initial_state)) * (n_generations - n)

print('Second star:', s)
