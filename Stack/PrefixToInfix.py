class PrefixToInfix:

    def __init__(self):
        self.output = []

        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

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
