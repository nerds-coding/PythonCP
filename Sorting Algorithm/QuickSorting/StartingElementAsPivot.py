def partition(arr,l,h):
    i = l+1
    j = h

    pivot = arr[l]

    while (i<=j):
        while (arr[i]<pivot)and(i<h):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        else:
            i+=1
    arr[l],arr[j]=arr[j],arr[l]
    return j

def quickSort(arr,l,h):
    if(l<h):
        q = partition(arr,l,h)
        quickSort(arr,l,q-1)
        quickSort(arr,q+1,h)

arr = [20,3,69,90,4,12,35,68,312]
quickSort(arr,0,len(arr)-1)

print(arr)