def quickSort(arr,l,h):
    i = l
    j = h
    pivot = arr[(l+h)//2]

    while(i<=j):
        while(arr[i]<pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if(i<=j):
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1

    if(l<j):
        quickSort(arr,l,j)
    if(i<h):
        quickSort(arr,i,h)


arr = [34, 2, 1, 45, 67, 667,7899,89, 90, 323, 56, 787, 8900]
quickSort(arr, 0, len(arr)-1)

print(arr)
