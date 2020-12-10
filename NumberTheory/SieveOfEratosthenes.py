#The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million

def findPrimeNumbers(n):
    arr = [True]*(n+1)

    for i in range(2,n+1):
        for j in range(2,n//2):
            if(len(arr)>(i*j)):
                arr[i*j]=False

    for i in range(2,n+1):
        if(arr[i]):
            print(i)

findPrimeNumbers(30)
