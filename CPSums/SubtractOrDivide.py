try:
    for _ in range(int(input())):
        n = int(input())
        if(n==1)or(n==0):
            print(0)
        elif(n==2):
            print(1)
        elif(n==3):
            print(2)
        elif(not(n&1)):
            print(2)
        elif(n&1):
            print(3)
except:
    pass
