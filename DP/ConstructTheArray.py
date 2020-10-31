def construct(n,k,x):
    mod = (10**9)+7
    b,a = [None]*n,[None]*n
    a[0]= 1 if(x==1) else 0
    b[0] = 1 if(x!=1) else 0

    for i in range(1,n):
        a[i] = b[i-1]%mod
        b[i] = (a[i-1]*(k-1)+(b[i-1]*(k-2)))%mod

    return a[-1]

print(construct(4,3,2))