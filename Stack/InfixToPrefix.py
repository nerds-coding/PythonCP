def InfixToPrefix(data):
    prefix = ''
    prev = ''
    stack = []

    data = data[::-1]

    opening = set(('(', '[', '{'))
    closing = set((')', ']', '}'))
    final = {a: b for a, b in zip(opening, closing)}
    association_rule = {'+': '-', '-': '+', '*': '/', '/': '*'}
    for m in data:
        if(m.isalpha()):
            prefix += m
        elif((association_rule["+"] == m) or (association_rule['-'] == m)) and ((association_rule['*'] == prev) or (association_rule['/'] == prev)):
            prefix += stack.pop()
            stack.append(m)
            prev = m
        elif((association_rule["+"] == m) or (association_rule['-'] == m)) and ((association_rule['*'] != prev) or (association_rule['/'] != prev)):
            stack.append(m)
            prev = m
        elif(m in closing):
            stack.append(m)
        elif(m in opening):
            while stack:
                close = stack.pop()
                if(final[m] == close):
                    break
                elif(close not in closing):
                    prefix += close
        elif(association_rule['*'] == m or association_rule['/'] == m):
            stack.append(m)
            # print(m)
            prev = m

    prefix += ''.join(stack[::-1])

    print(prefix[::-1])


# *-A/BC-/AKL

if __name__ == '__main__':
    print(InfixToPrefix('(A - B/C) * (A/K-L)'))
