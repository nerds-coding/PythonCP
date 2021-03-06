class InfixToPrefix:

    def __init__(self, size):
        self.size = size

        self.stack = []
        self.output = []

        self.top = -1
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return self.stack == []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        else:
            return "#"

    def push(self, val):
        self.top += 1
        self.stack.append(val)

    def isGreater(self, val):
        try:
            a = self.precedence[val]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except(KeyError):
            return False

    def isOperand(self, val):
        return val.isalpha()

    def prefix(self, data):
        data = data[::-1]

        for i in data:

            if(self.isOperand(i)):
                self.output.append(i)

            elif(i == ')'):
                self.push(i)

            elif(i == '('):
                while(not self.isEmpty() and self.peek() != ')'):
                    self.output.append(self.pop())
                if(not self.isEmpty())and self.peek() != ')':
                    return -1
                else:
                    self.pop()

            else:
                while(not self.isEmpty())and self.isGreater(i):
                    self.output.append(self.pop())
                self.push(i)

        while(not self.isEmpty()):
            self.output.append(self.pop())

        print(''.join(self.output[::-1]))


n = InfixToPrefix(8)
n.prefix('(A-B/C)*(A/K-L)')

# *-A/BC-/AKL
