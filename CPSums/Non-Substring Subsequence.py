try:
    for _ in range(int(input())):
        n,q = map(int,input().split())
        s = input()
        for _ in range(q):
            l,r = map(int,input().split())
            
            if(r-l+1 == n):
                print("NO")
            else:
                flag1 = 0
                flag2 = 0
                sub = s[l-1:r]
                for i in range(l-1):
                    if(s[i]==sub[0]):
                        flag1 = 1
                for i in range(r,n):
                    if(s[i]==sub[r-l]):
                        flag2 = 1

                if(flag1==1) or (flag2==1):
                    print('YES')
                else:
                    print("NO")
                
except:
    pass
