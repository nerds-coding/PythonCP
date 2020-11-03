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
    step1 = 0
    step2 = 0
    while (n):
        if(not(n%2)):
            n//=2
            step1+=1
        else:
            n-=1
            step2+=1
    return step2+step1


print(countSteps(13))

