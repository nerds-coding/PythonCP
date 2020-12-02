import numpy as np
def kinghtTour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]

    kinghtTour_helper(n=n,board= board,x=0,y=0,counter=0)

    print(np.array(board))

def kinghtTour_helper(n,board,x,y,counter):
    if(counter == n*n):
        return True
    
    if(x<0 or x>=n)or(y<0 or y>=n) or(board[y][x]!=-1):
        return False
    
    board[y][x] = counter
    for x_new, y_new in zip([-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2,-1, 1]):
        if(kinghtTour_helper(n,board,x+x_new,y+y_new,counter+1)):
            return True
    
    board[y][x] = -1
    return False



kinghtTour(5)