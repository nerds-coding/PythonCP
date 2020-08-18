def ElementRotation(n, rot, arr):

    for x in range(rot):
        arr.append(arr[0])
        del arr[0]

    [print(x, end=' ') for x in arr]


arr = [5, 1, 2, 3, 4]
ElementRotation(5, 4, arr)
