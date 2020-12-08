import numpy as np


def kinghtTour(n):
    chess = [[-1 for _ in range(n)] for _ in range(n)]

    kinghtTour_helper(0, 0, chess, 0, n)
    print(np.array(chess))


def kinghtTour_helper(x, y, chess, counter, n):
    if(counter == n*n):
        return True

    if(x < 0 or x >= n) or (y < 0 or y >= n) or (chess[y][x] != -1):
        return False

    chess[y][x] = counter

    for x_new, y_new in zip([-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]):
        if(kinghtTour_helper(x+x_new, y+y_new, chess, counter+1, n)):
            return True

    chess[y][x] = -1
    return False


kinghtTour(5)
