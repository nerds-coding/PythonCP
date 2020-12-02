try:
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        n = [0]*n
        for i in a:
            n[i-1]+=1
        try:
            print(a.index(n.index(1)+1)+1)
        except:
            print(-1)
except:
    pass
