# Input : arr[] = {1, 2, 2, 3, 4, 1}
# Output : 9
#
# There are possible subarrays with even
# sum. The subarrays are
# 1) {1, 2, 2, 3}  Sum = 8
# 2) {1, 2, 2, 3, 4}  Sum = 12
# 3) {2}  Sum = 2 (At index 1)
# 4) {2, 2}  Sum = 4
# 5) {2, 2, 3, 4, 1}  Sum = 12
# 6) {2}  Sum = 2 (At index 2)
# 7) {2, 3, 4, 1} Sum = 10
# 8) {3, 4, 1}  Sum = 8
# 9) {4}  Sum = 4


def solve(arr, n):

    res = 0

    for i in range(n):
        sum = 0
        for x in range(i, n):
            sum += arr[x]
            if(sum % 2 == 0):
                res += 1
    print(res)


solve([1, 2, 2, 3, 4, 1], 6)
