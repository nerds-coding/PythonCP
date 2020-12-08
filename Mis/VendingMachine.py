def primeSum(n):
    arr = [i for i in range(1,n+1)]
    pr = []
    flag =False
    for i in arr:
        if(i==1):
            flag = True
        if(i==2):
            pr.append(2)
            flag = True
        for j in range(2,i):
            if(not(i%j)):
                flag = True
        if(not(flag)):
            pr.append(i)
        flag=False
    return sum(pr)

print(primeSum(5))

