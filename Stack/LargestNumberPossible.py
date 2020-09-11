for t in range(int(input())):
    n, s = map(int, input().split())
    res = []
    if(9*n >= s and s != 0):
        for i in range(n):
            if(s >= 9):
                res.append(9)
                s -= 9
            else:
                res.append(s)
                s = 0

        print("".join(map(str, res)))
    else:
        print(-1)
