def partition(arr,l,h):
    i = l+1
    pivot = arr[l]

    for j in range(l+1,h+1):
        if(arr[j]<=pivot):
            arr[j],arr[i] = arr[i],arr[j]
            i+=1

    arr[l],arr[i-1]=arr[i-1],arr[l]

    return i-1

def quickSort(arr,l,h):
    if(l<h):
        q = partition(arr,l,h)
        quickSort(arr,l,q-1)
        quickSort(arr,q+1,h)


arr = [16, 537, 454, 959, 100, 19, 61, 10]
quickSort(arr,0,len(arr)-1)

print(arr)
