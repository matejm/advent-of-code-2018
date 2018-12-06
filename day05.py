class ll:
    def __init__(self, a, prev, next):
        self.value = a 
        self.prev = prev
        self.next = next

def score(data):
    start = None
    last = None
    c = ll(data[0], None, None)

    for i in range(1, len(data)):
        last = c

        c = ll(data[i], last, None)
        last.next = c

        if start is None:
            start = last


    c = start

    while c.next is not None:

        a = c.value
        b = c.next.value

        if (a.lower() == b and a.lower() != a) or (a.upper() == b and a.upper() != a):
            # Delete
            if c == start:
                start = c.next.next
                c = start
            else:
                c.prev.next = c.next.next

                if c.next.next is not None:
                    c.next.next.prev = c.prev

                c = c.prev
        else:
            c = c.next

    s = ''
    c = start

    while c is not None:
        s += c.value
        c = c.next

    return len(s)


with open('input') as file:
    data = file.read().strip()

print('First star:', score(data))

m = 1e9

for c in 'abcdefghijklmnopqrstuvxywz':
    m = min(m, score(''.join(i for i in data if i.lower() != c)))

print('Second star:', m)