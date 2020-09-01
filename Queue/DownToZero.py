import os
import sys
import math


def downToZero(N):
    if N == 0:
        return 0
    Q = [(N, 0)]
    print(Q)
    setQ = [0] * N
    while Q:
        N, steps = Q.pop(0)
        if N == 1:
            return steps+1
        div = int(math.sqrt(N))
        while div > 1:
            if N % div == 0 and not setQ[N // div]:
                Q.append((N // div, steps+1))
                setQ[N // div] = 1
            div -= 1
        if not setQ[N-1]:
            Q.append((N-1, steps+1))
            setQ[N-1] = 1


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = downToZero(n)

        print(result)
