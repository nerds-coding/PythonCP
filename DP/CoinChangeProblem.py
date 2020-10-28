def coinChange(coins,m):
    arr = [[0 for _ in range(m+1)] for _ in range(len(coins))]

    for x in range(len(coins)):
        arr[x][0]=1
    
    for x in range(1,m+1):
        if(not(x%coins[0])):
            arr[0][x] = 1
        else:
            arr[0][x] = 0
    
    for i in range(len(coins)):
        for j in range(1,m+1):
            if(coins[i]>j):
                arr[i][j]=arr[i-1][j]
            else:
                arr[i][j] = arr[i-1][j]+arr[i][j-coins[i]]
    print(arr[-1][-1])



coinChange([2,3,5,10],15)
