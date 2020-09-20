def Merge(arr1, arr2):
    if(arr1 is None)and(arr2 is None):
        return

    sorted = []
    len1 = len(arr1)
    len2 = len(arr2)

    i = 0
    j = 0

    while (i < len1)and(j < len2):
        if(arr1[i] <= arr2[j]):
            sorted.append(arr1[i])
            i += 1
        else:
            sorted.append(arr2[j])
            j += 1

    while (arr1 != []) and(i != len1):
        sorted.append(arr1.pop(0))
    while(arr2 != []) and(j != len2):
        sorted.append(arr2.pop(0))

    return sorted


arr1 = [1, 2, 3, 4, 6]
arr2 = [6, 7, 9]

print(Merge(arr1, arr2))
