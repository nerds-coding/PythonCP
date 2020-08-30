class PostfixToInfix:

    def __init__(self, data):
        self.data = data

        self.stack = []
        self.output = []

        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return self.stack == []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def isGreater(self, val):
        try:
            a = self.precedence[val]
            b = self.precedence[self.peek()]
            return True if(a <= b) else False
        except(KeyError):
            return False

    def isOperand(self, val):
        return val.isalpha()

    def postfix(self):
        #self.data = self.data[::-1]
        for x in self.data:
            if(self.isOperand(x)):
                self.output.append(x)

            else:
                self.output.insert(0, '('+self.output.pop(0)+''+x+''+self.output.pop(0)+')')
        return self.output


post = PostfixToInfix('ab*c+')
print(post.postfix())

# ((a*b)+c)
