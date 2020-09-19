def SortingInDecending(arr):
    for x in range(len(arr)-1):
        min = x
        for j in range(x+1, len(arr)):
            if(arr[min] <= arr[j]):
                min = j

        temp = arr[min]
        arr[min] = arr[x]
        arr[x] = temp

    return arr


def SortingInAscending(arr):

    for x in range(len(arr)-1):
        min = x
        for j in range(x+1, len(arr)):
            if(arr[min] >= arr[j]):
                min = j
        # temp = arr[x]
        # arr[x] = arr[min]
        # arr[min] = temp

        arr[x], arr[min] = arr[min], arr[x]
    return arr


arr = [4, 6, 2, 7, 3, 9]

print(SortingInDecending(arr))
print(SortingInAscending(arr))
