import numpy as np
def RatInMaze(board,x,y,n):
    sol = [[0 for _ in range(n)] for _ in range(n)]

    ratMazeHelper(n,board,sol,x,y)

    print(np.array(sol))


def isSafe(x, y, board, n):
    return True if(x >= 0 and x < n) and (y >= 0 and y < n) and (board[x][y] == 1) else False


def ratMazeHelper(n, board, sol, x, y):
    if(x == n-1) and (y == n-1) and (board[x][y] == 1):
        sol[x][y] = 1
        return True
    
    if(isSafe(x,y,board,n)):
        sol[x][y]=1

        if(ratMazeHelper(n,board,sol,x+1,y)):
            return True
        
        if(ratMazeHelper(n,board,sol,x,y+1)):
            return True

        sol[x][y]=0
        return False



board = [[1, 1, 0], [0, 1, 1], [1, 1, 1]]
RatInMaze(board, 0, 0, 3)
