def linearSearching(lst,n):
    for i in range(len(lst)):
        if(n==lst[i]):
            break
    return i

lst = [3,2,4,6,3,44,5,6,3,178,97]
n = 44

print(linearSearching(lst,n))