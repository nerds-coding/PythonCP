class PrefixToInfix:

    def __init__(self):
        self.stack = []
        self.output = []

        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return self.stack == []

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def push(self, val):
        self.stack.append(val)

    def isGreater(self, val):
        try:
            a = self.precedence[val]
            b = self.precedence[self.peek()]
            return True if(a <= b) else False
        except(KeyError):
            return False

    def pop(self):
        return self.stack.pop()

    def isOperand(self, val):
        return val.isalpha()

    def infix(self, data):
        data = data[::-1]

        for x in data:
            if(self.isOperand(x)):
                self.output.append(x)

            else:
                i = '('+self.output.pop()+''+x+''+self.output.pop()+')'
                self.output.append(i)
        print(''.join(self.output[::-1]))


pre = PrefixToInfix()
pre.infix('*-A/BC-/AKL')


# ((A-(B/C))*((A/K)-L))
