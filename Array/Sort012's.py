#Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


def sortArray(arr):
    l = 0
    m = 0 # reference pointer
    h = len(arr)-1

    while(m<h):
        if(arr[m]==0):
            arr[m],arr[l]=arr[l],arr[m]
            l+=1
            m+=1
        elif(arr[m]==1):
            m+=1
        elif(arr[m]==2):
            arr[m],arr[h] = arr[h],arr[m]
            h-=1
    return arr

print(sortArray([0,2,2,1,1,0,2,1,0,2]))
