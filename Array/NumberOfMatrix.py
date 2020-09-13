'''
The problem is to count all the possible paths from top left
to bottom right of a MxN matrix with the constraints that from
each cell you can either move to right or down.

Let the given input 3*3 matrix is filled as such:
A B C
D E F
G H I
The possible paths which exists to reach 'I' from 'A' following
above conditions are as follows:
ABCFI, ABEHI, ADGHI, ADEFI, ADEHI, ABEFI.
'''

# Dynamic Programming


def findingPath(m, n):
    col = [[1]*n]
    row = [[0]*(n-1)]*(m-1)

    row = col+[[1]+m for m in row]

    print(row[0])

    for i in range(1, len(row)):
        for j in range(1, len(row[0])):
            row[i][j] = row[i-1][j]+row[i][j-1]
    print(row)


findingPath(3, 9)
