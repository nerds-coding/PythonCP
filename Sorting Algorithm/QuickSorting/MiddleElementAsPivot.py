def partition(arr,l,h):
    i = l
    j = h
    half = len(arr)//2
    pivot = arr[half]

    while(i<j):
        while(arr[i]<pivot)and(i<h):
            i+=1
        while(arr[j]>pivot)and(j>l):
            j-=1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        elif(j==half)or(i==half):
            break
        else:
            i+=1
    return half

def quickSort(arr,l,h):
    if(l<h):
        q = partition(arr,l,h)
        quickSort(arr,l,q-1)
        quickSort(arr,q+1,h)


arr = [34, 56, 2, 1, 45, 67, 89, 90, 323, 56, 787, 8900]
quickSort(arr, 0, len(arr)-1)

print(arr)
    
    
