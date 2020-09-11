for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    s = set(arr)
    l = []
    for i in s:
        l.append(arr.count(i))
    c = 0
    for i in l:
        c += 2*(i//2)
    print(c)
