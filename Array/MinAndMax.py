# find the minimum and maximum of an Array

def minimum(arr):
    temp = arr[0]
    for i in arr:
        if(temp > i):
            temp = i
    return temp


def Maximum(arr):
    temp = arr[0]
    for i in arr:
        if(temp < i):
            temp = i
    return temp


print(Maximum([5, 2, 3, 1, 4]))
print(minimum([5, 2, 3, 1, 4]))
