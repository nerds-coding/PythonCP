# Reversing an array without uisng any extra space

def ReverseArray(n):
    start = 0
    end = len(n)-1
    while(start<end):
        n[start],n[end] = n[end],n[start]
        start+=1
        end-=1
    print(n)

ReverseArray([1,2,3,4,5,6])
