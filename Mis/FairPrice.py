def gcd(n):
    count = 0
    arr = [i for i in range(n)]
    temp = n
    for i in arr:
        while(i):
            temp , i = i, temp % i
        if(temp==1):
            count+=1
        temp=n
    print(count)

    

gcd(5)