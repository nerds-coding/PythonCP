def fun(n):
    if(n == 1):
        return
    for x in range(n):
        #print(x, end=" ")
        print(n)
        print()
        fun(n-1)


fun(3)
