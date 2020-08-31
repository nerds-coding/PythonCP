def StockSpan(data, size):
    stack = [1]

    for x in range(1, len(data)):
        j = 1
        i = x
        if(data[i-1] < data[x]):
            while(data[i-1] < data[x]):
                i -= 1
                j += 1
            stack.append(j)
        else:
            stack.append(1)
    print(stack)


data = [100, 80, 60, 70, 60, 75, 85]
StockSpan(data, 4)


#1, 1, 1, 2, 1, 4, 6
