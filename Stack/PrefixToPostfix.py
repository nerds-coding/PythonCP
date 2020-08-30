class PrefixToPostfix:

    def __init__(self, data):
        self.data = data

        self.stack = []
        self.output = []

        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return self.stack == []

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def isGreater(self, val):
        try:
            a = self.precedence[val]
            b = self.precedence[self.peek()]

            return True if(a <= b) else False
        except(KeyError):
            return False

    def isOperand(self, val):
        return val.isalpha()

    def PrefixToInfix(self):
        self.data = self.data[::-1]

        for x in self.data:
            if(self.isOperand(x)):
                self.output.append(x)
            else:
                self.output.append('('+(self.output.pop()+''+x+self.output.pop())+')')
        self.data = ''.join(self.output[::-1])
        self.output = []

    def InfixToPostFix(self):
        for x in self.data:

            if(self.isOperand(x)):
                self.output.append(x)

            elif(x == '('):
                self.push(x)

            elif(x == ')'):
                while(not self.isEmpty())and self.peek() != '(':
                    self.output.append(self.pop())
                if(not self.isEmpty())and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            else:
                while(not self.isEmpty()) and self.isGreater(x):
                    self.output.append(self.pop())
                self.push(x)
        while not self.isEmpty():
            self.output.append(self.pop())
        print(''.join(self.output))


pre = PrefixToPostfix('*-A/BC-/AKL')
pre.PrefixToInfix()
pre.InfixToPostFix()
