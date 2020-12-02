try:
    for _ in range(int(input())):
        n,k = map(int,input().split())
        a = input()
        b = input()

        ta = [0]*26
        tb = [0]*26
        flag = 0

        for i in a:
            ta[ord(i)-ord('a')]+=1
        for i in b:
            tb[ord(i)-ord('a')]+=1
        for i in range(25):
            d = ta[i]-tb[i]
            if(ta[i] < tb[i]) or (d % k != 0):
                flag=1
            else:
                ta[i+1]+=d
            

        if(flag):
            print("NO")
        else:
            print("YES")
except:
    pass

        
