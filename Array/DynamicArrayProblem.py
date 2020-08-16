def dynamicArray(n, queries):
    seq0 = [[] for _ in range(n)]
    lastAns = 0
    res = []
    for seq, x, y in queries:
        index = (x ^ lastAns) % n
        if(seq == 1):
            seq0[index].append(y)
        else:
            pos = y % len(seq0[index])
            lastAns = seq0[index][pos]
            res.append(lastAns)
    return res


queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
n = 2

print(dynamicArray(n, queries))
