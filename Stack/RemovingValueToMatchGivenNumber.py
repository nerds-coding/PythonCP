def twoStacks(x, a, b):
    s1, s2 = map(sum, (a, b))
    while s1 > x:
        o = a.pop(0)
        s1 -= o
    a.append(o)

    while s2 > x:
        o = b.pop(0)
        s2 -= o
    b.append(o)
    return (n-len(a))+(m-len(b))
