def SetOrNot(n,i):
    return True if(n&(1<<i-1)) else False

print(SetOrNot(11,2))