j = partition(arr,l,h)
    quickSort(arr,l,j-1)
    quickSort(arr,j+1,h)
