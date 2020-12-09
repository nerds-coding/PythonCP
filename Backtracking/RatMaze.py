# Rat in Maze with All the four Direction

import numpy as np


def RatMaze(board, n, x, y):
    sol = [[0 for _ in range(n)] for _ in range(n)]
    RatMaze_helper(board, n, x, y, sol)
    print(np.array(sol))
    #print(sol)


def isSafe(board, x, y, n):
    return True if(x >= 0 and x < n) and (y >= 0 and y < n) and (board[x][y] == 1) else False


def RatMaze_helper(board, n, x, y, sol):
    if(x == n-1) and (y == n-1) and (board[x][y] == 1):
        sol[x][y] = 1
        return True

    if(isSafe(board, x, y, n)):
        sol[x][y] = 1

        if(RatMaze_helper(board, n, x+1, y, sol)):
            print('D')
            return True
        if(RatMaze_helper(board, n, x, y+1, sol)):
            print('R')
            return True
        if(RatMaze_helper(board, n, x, y-1, sol)):
            print('L')
            return True
        if(RatMaze_helper(board, n, x-1, y, sol)):
            print('B')
            return True
        

        sol[x][y] = 0
        return False


board = [[1, 1, 0], [0, 1, 1], [1, 1, 1]]
RatMaze(board, 3, 0, 0)