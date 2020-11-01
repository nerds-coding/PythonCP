'''
A boy lost the password of his super locker. 
He remembers the number of digits N as well as the sum S 
of all the digits of his password. He know that his password 
is the largest number of N digits that can be possible with given sum S.
As he is busy doing his homework, help him retrieving his password.

Example :
Input:
N = 5, S = 12
Output: 93000
Explanation: Sum of elements is 12.
Largest possible 5 digit number is 93000.


Example 2:
Input:
N = 3, S = 29
Output: -1
Explanation: There is no such three digit
number whose sum is 29.
'''


def findLargestNumber(n,s):
    m = ''
    for i in range(n):
        val =0
        if(s>9):
            val = 9
            s-=9
        else:
            val = s
            s=0
        m+=str(val)
    if(s>0):
        return -1
    else:
        return m

print(findLargestNumber(4,12))
