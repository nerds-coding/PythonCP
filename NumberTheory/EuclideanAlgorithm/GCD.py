def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def givePrime(n):
    count = 0
    arr = [i for i in range(n)]
    
    for i in arr:
        if(gcd(n,i)==1):
            count+=1
    print(count)

givePrime(6)
#print(gcd(10, 20))



# Finding GCD with loop

def GCD(x,y):
    while(y):
        x,y = y,x%y
    return x