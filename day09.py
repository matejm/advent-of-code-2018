n = 459
m = 71790

l = [0]
i = 0

scores = [0 for i in range(n)]

for marble in range(1, m + 1):
    if marble % 23 != 0:
        i += 2
        i %= len(l)
        l.insert(i, marble)
    else:
        i -= 7
        i %= len(l)

        removed = l.pop(i)
        scores[marble % n] += marble + removed

print('First star:', max(scores))

n = 459
m = 7179000

class LL:
    def __init__(self, prev, val, next):
        self.prev = prev
        self.next = next
        self.val = val

l = LL(None, 0, None)
l.prev = l
l.next = l

scores = [0 for i in range(n)]

for marble in range(1, m + 1):
    if marble % 23 != 0:
        l = l.next

        prev = l
        next = l.next

        l = LL(prev, marble, next)
        prev.next = l
        next.prev = l

    else:
        for i in range(7):
            l = l.prev

        prev = l.prev
        next = l.next

        prev.next = next
        next.prev = prev

        scores[marble % n] += marble + l.val 

        l = next

print('Second star:', max(scores))