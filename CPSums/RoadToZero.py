try:
    for _ in range(int(input())):
        x,y = map(int,input().split())
        a,b = map(int,input().split())

        if(x>y):
            x,y = y,x
        total = a*(y-x)
        if(2*a<b):
            total +=x*(2*a)
        else:
            total+=x*b
        print(total)
except:
    pass
