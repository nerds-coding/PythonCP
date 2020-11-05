def quickSort(arr, l, h):
    i = l
    j = h
    mid = (l+h)//2
    pivot = arr[mid]

    while(i < j):
        while(arr[i] < pivot):
            i += 1
        while(arr[j] > pivot):
            j -= 1
        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if(l < j):
        quickSort(arr, l, mid-1)
    if(i < h):
        quickSort(arr, mid+1, h)


arr = [34, 2, 1, 45, 67, 89, 90, 323, 56, 787, 8900]
quickSort(arr, 0, len(arr)-1)

print(arr)
