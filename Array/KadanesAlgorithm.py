# Kadanes Algorithm is used to find the maximum sum of contigous subarray

def KadanesAlgo(arr):
    for i in range(len(arr)-1):
        if(arr[i]+arr[i-1]>0):
            arr[i]+=arr[i-1]
    return max(arr)


print(KadanesAlgo([1, 2, 3, -2, 5]))
