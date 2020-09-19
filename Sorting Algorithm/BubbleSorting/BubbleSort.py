def SortingInAscending(arr):
    for x in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j] >= arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def SortingInDecending(arr):
    for x in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j] <= arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


arr = [4, 6, 2, 7, 3, 9]

print(SortingInDecending(arr))
print(SortingInAscending(arr))
