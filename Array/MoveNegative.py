def MoveNegative(arr):
    temp = arr[0]
    for _ in range(len(arr)):
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]= arr[i+1],arr[i]
    return arr


print(MoveNegative([-12, 11, -13, -5, 6, -7, 5, -3, -6]))
