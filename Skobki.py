class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]


line = '{()}}'
d = {
    '(': ')',
    '{': '}',
    '[': ']',
}

s = Stack()
# s.push('a')
# s.push('b')
# s.push('c')
# s.push('d')
# s.push('e')

# print(s.peek())
for x in line:
    if x in d:
        s.push(x)
    elif not s.isEmpty() and d[s.peek()] == x:
        s.pop()
    else:
        s.push(x)
        break
if s.isEmpty():
    print('True')
else:
    print('False')

