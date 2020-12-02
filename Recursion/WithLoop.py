def fun(n):
    if(n == 1):
        return
    for x in range(n):
        print(x)
        print(n)
        print()
        fun(n-1)
        print("hello")


fun(3)