for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    i, j = 0, n - 1
    maxLeft, maxRight = 0, 0
    while i < j:
        if a[i] < a[j]:
            maxLeft = max(maxLeft, a[i])
            res += maxLeft - a[i]
            i += 1
        else:
            maxRight = max(maxRight, a[j])
            res += maxRight - a[j]
            j -= 1
    print(res)
