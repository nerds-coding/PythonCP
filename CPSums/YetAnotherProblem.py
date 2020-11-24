try:
    for _ in range(int(input())):
        a,b,q = map(int,input().split())
        for _ in range(q):
            l,r = map(int,input().split())
            count = 0
            for x in range(l,r+1):
                if(((x%a)%b)!=((x%b)%a)):
                    count+=1
            print(count)
except:
    pass
