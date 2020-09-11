for _ in range(int(input())):
    n = int(input())
    lt = list(map(int, input().split()))
    zc = lt.count(0)
    for i in range(zc):
        lt.remove(0)
    for i in range(zc):
        lt.append(0)
    for i in lt:
        print(i, end=' ')
    print()
