def coinChange(coins, n):

    table = [[0 for _ in range(n+1)] for _ in range(len(coins))]

    for x in range(len(coins)):
        table[x][0] = 1

    for x in range(n+1):
        if(not(x % coins[0])):
            table[0][x] = 1
    
    for x in range(len(coins)):
        for j in range(1,n+1):
            if(coins[x]>j):
                table[x][j] = table[x-1][j]
            else:
                table[x][j] = table[x-1][j]+table[x][j-coins[x]]
    
    return table[-1][-1]

arr = [2,3,5,10]
n = 15
print(coinChange(arr,n))


