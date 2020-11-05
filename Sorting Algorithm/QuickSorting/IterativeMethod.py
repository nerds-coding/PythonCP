def quicksortBetter(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksortBetter(left) + middle + quicksortBetter(right)


arr = [34, 56, 2, 1, 45, 67, 89, 90, 323, 56, 787, 8900]

print(quicksortBetter(arr))