def findNum(n):
    for i in range(9):
        print(i)
        if(i<n):
            findNum(n)
        
findNum(3)