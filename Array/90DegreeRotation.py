t = int(input())
for j in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            print(arr[(n-j-1)*n + i], end=(" "))
    print()
