class Stack:

    def __init__(self):
        self.item = []

    def empty(self):
        self.item = []

    def push(self, data):
        return self.item.append(data)

    def pop(self):
        return self.item.pop()

    def iterating(self):
        for x in self.item[::-1]:
            print(x)


stack = Stack()

stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)

stack.pop()

stack.iterating()
