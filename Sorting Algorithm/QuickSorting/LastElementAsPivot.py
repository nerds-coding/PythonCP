def partition(arr,l,h):
    i = l-1
    pivot = arr[h]
    
    for j in range(l,h):
        if(arr[j]<=pivot):
            i+=1
            arr[j],arr[i] = arr[i],arr[j]
    
    i+=1
    arr[i],arr[h] = arr[h],arr[i]
    return i

def quickSort(arr,l,h):
    if(l<h):
        q = partition(arr,l,h)
        quickSort(arr,l,q-1)
        quickSort(arr,q+1,h)

arr = [34,56,2,1,45,67,89,90,323,56,787,8900]
quickSort(arr,0,len(arr)-1)

print(arr)