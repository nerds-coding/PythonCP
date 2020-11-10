def Merge(arr1,arr2):
    l1 = len(arr1)
    l2 = len(arr2)

    sorted_arr = []
    i=j=k=0

    while(i<l1)and(j<l2):
        if(arr1[i]<=arr2[j]):
            sorted_arr.append(arr1[i])
            i+=1
        else:
            sorted_arr.append(arr2[j])
            j+=1
        
    
    while(i<l1):
        sorted_arr.append(arr1[i])
        i+=1
    
    while(j<l2):
        sorted_arr.append(arr2[j])
        j+=1
    
    return sorted_arr

arr1 = [1, 2, 3, 4, 6]
arr2 = [6, 7, 9]

print(Merge(arr1, arr2))
