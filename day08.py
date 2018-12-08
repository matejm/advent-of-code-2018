class Tree:
    def __init__(self, i):
        global data
        global s 

        self.n = data[i]
        self.m = data[i + 1]
        i += 2

        self.children = []

        for _ in range(self.n):
            tree = Tree(i)
            i = tree.end
            self.children.append(tree)

        self.end = i + self.m
        self.metadata = data[i : self.end]

        s += sum(self.metadata)

        if self.n == 0:
            self.value = sum(self.metadata)
        else:
            self.value = 0
            for index in self.metadata:
                index -= 1

                if 0 <= index and index < self.n:
                    self.value += self.children[index].value



with open('input') as file:
    data = list(map(int, file.read().split()))

s = 0
t = Tree(0)

print('First star:', s)
print('Second star:', t.value)