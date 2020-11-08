def partition(arr,l,h):
    i = l
    mid = (l+h)//2
    pivot = arr[mid]

    for j in range(l,h+1):
        if(arr[j]<pivot):
            arr[j],arr[i] = arr[i],arr[j]
            i += 1
    return mid

def quickSort(arr,l,h):
    if(l<h):
        q= partition(arr,l,h)
        quickSort(arr,l,q-1)
        quickSort(arr,q+1,h)

arr = [34, 2, 1, 45, 67, 667,7899,89, 90, 323, 56, 787, 8900]
quickSort(arr, 0, len(arr)-1)

print(arr)
