# def arrayManipulation(n, queries):
#     arr = [0]*n
#     for x, y, num in queries:
#         m = arr[x-1:y]
#         print(m)
#     return max(arr)


def arrayManipulation(n, queries):
    arr = [0] * (n+1)

    for a, b, k in queries:
        arr[a-1] += k
        arr[b] -= k

    maxVal, tmp = 0, 0
    for a in arr:
        tmp += a
        if tmp > maxVal:
            maxVal = tmp

    return maxVal


queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
n = 5

print(arrayManipulation(n, queries))
