def Catalan(n):
    if(n == 0)or (n == 1):
        return 1
    c = [1]*(n+1)

    for i in range(2, n+1):
        c[i] = 0
        for j in range(i):
            c[i] += c[j]*c[i-j-1]

    return c[n]


print(Catalan(1))
