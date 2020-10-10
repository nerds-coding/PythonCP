'''
5+0 = 5 and 5^0=5
5+2 = 7 and 5^2=7

x = 0,1,2,3,4,5

 0 >= x <= n
'''


def sumXor(n):
    count = 0
    while (n != 0):
        if(n % 2 == 0):
            count += 1
        n //= 2
    return (1 << count)


sumXor(5)
