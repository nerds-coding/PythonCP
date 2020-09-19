def SortingInAscending(arr):
    for x in range(1, len(arr)):
        key = arr[x]
        i = x-1
        while i >= 0 and key <= arr[i]:
            arr[i+1] = arr[i]
            i -= 1

        arr[i+1] = key
    return arr


arr = [6, 4, 2, 7, 3, 9]

# print(SortingInDecending(arr))
print(SortingInAscending(arr))
