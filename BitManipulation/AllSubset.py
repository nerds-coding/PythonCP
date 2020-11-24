def Subset(arr):
    for k in range(1<<len(arr)):
        for j in range(0,len(arr)):
            if(k&(1<<j)):
                print(arr[j])
Subset([1,2,3])