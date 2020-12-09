import numpy as np

def isValid(arr,r,c,val):
    for i in range(9):
        if(arr[r][i]==val):
            return False
    
    for j in range(9):
        if(arr[j][c]==val):
            return False
    
    newr = r//3*3
    newc = c//3*3

    for i in range(3):
        for j in range(3):
            if(arr[newr+i][newc+j]==val):
                return False
    
    return True

def solveSudko(arr,r,c):
    if(r==len(arr)):
        print(np.array(arr))
        return
    
    nr = 0
    nc = 0
    if(c == 8):
        nr = r+1
        nc = 0
    else:
        nr = r
        nc = c+1
    
    if(arr[r][c]!=0):
        solveSudko(arr,nr,nc)
    else:
        for val in range(1,10):
            if(isValid(arr,r,c,val)):
                arr[r][c] = val
                solveSudko(arr,nr,nc)
                arr[r][c] = 0

def solver():
    arr = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    solveSudko(arr, 0, 0)

solver()
