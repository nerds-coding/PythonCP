def MatchingStack(brackets):
    table = {')': '(', ']': '[', '}': '{'}
    stack = []
    for x in s:
        if stack and table.get(x) == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    return "NO" if stack else "YES"


brackets = '{(){}}'

print(MatchingStack(brackets))
