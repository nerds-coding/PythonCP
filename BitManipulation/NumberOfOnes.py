def CountingOnes(num):
    count = 0
    while(num != 0):
        num = num & (num-1)
        count += 1
    return count


print(CountingOnes(23))
