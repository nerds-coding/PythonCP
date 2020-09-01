def OperationPerformance(data):
    q = []
    stack = []

    for d in data:
        if(d[0] == 1):
            q.append(d[1])
        elif(d[0] == 2):
            q.pop(0)
        elif(d[0] == 3):
            stack.append(q[0])
    return stack


if __name__ == '__main__':
    n = list()
    for _ in range(int(input())):
        m = list(map(int, input().split()))
        n.append(m)
    m = OperationPerformance(n)
    while m:
        print(m.pop(0))
