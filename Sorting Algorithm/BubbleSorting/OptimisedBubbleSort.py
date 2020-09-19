'''Optimized Implementation:

The previous function always runs O(n^2)
time even if the array is sorted.
It can be optimized by stopping the algorithm if
inner loop didn’t cause any swap.

'''


def SortingInAscending(arr):
    for _ in range(len(arr)):
        swap = False

        for j in range(len(arr)-1):
            if(arr[j] >= arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if(swap == True):
            return arr
    return arr


arr = [4, 6, 2, 7, 3, 9]

# print(SortingInDecending(arr))
print(SortingInAscending(arr))
