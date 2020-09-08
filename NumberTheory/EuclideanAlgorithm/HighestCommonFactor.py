def hcf(x, y):
    mini = min(x, y)

    if(x % mini == 0) and(y % mini == 0):
        return mini

    for i in range(mini//2, 1, -1):
        if(x % i == 0)and(y % i == 0):
            return i

    return 1


print(hcf(16, 32))
