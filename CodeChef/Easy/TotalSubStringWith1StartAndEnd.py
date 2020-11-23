def SubString(s):
    n = 0
    for i in s:
        if(i=='1'):
            n+=1
    return (n*(n+1)//2)


print(SubString('11111'))