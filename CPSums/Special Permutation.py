try:
    for _ in range(int(input())):
        n = int(input())

        n = list(range(1,n+1))
        for i in range(len(n)-1):
            n[i],n[i+1] = n[i+1],n[i]
        for i in n:
            print(i,end=" ")
except:
    pass
        