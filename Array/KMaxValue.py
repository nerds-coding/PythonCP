# find the K Max Value of the Array

# Used Bubble Sort for sorting the array

def FindKMax(arr,k):
    for _ in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    
    print(arr[k-1])


FindKMax([53,1,5,2,1,3],3)
