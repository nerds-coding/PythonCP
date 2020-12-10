def Union(arr1,arr2):
    for i in arr2:
        if(i not in arr1):
            arr1.append(i)
    
    return(arr1,len(arr1))

def Intersection(arr1,arr2):
    t = list()
    for i in arr2:
        if(i in arr1):
            t.append(i)
    return(t,len(t))


print(Union([1, 2 ,3 ,4 ,5],[1,2,3]))

print(Intersection([1, 2, 3, 4, 5], [1, 2, 3]))
