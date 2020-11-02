'''
Given a number N. Find the number of operations required to reach N starting from 0.
You have 2 operations available:

    Double the number
    Add one to the number


    Input:
N = 8
Output: 4
Explanation: 0 + 1 = 1, 1 + 1 = 2,
2 * 2 = 4, 4 * 2 = 8
'''


def countSteps(n):
    counter = 0
    while(n != 0):
        sqrt = n**0.5
        if(sqrt - int(sqrt) == 0):
            n **= 0.5
        elif(n > 0) and (sqrt - int(sqrt) != 0):
            n -= 1
        counter += 1
        print(n)
    return counter


#print(countSteps(14))
sqrt = 2.4
print(sqrt - int(sqrt) == 0)
