def Unique(arr):
    ans = 0
    for j in arr:
        ans^=j
        print(ans)
    print(ans)

Unique([1,2,3,4,3,2,1])