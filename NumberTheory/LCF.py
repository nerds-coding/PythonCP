def lcf(x, y):

    mini = min(x, y)

    for i in range(2, mini//2):
        if(x % i == 0)and(y % i == 0):
            return i

    return 1


print(lcf(20, 10))
