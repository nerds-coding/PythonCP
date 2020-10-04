''' Another sorting method, the counting sort,
does not require comparison. Instead, you create
an integer array whose index range covers the entire
 range of values in your array to sort. Each time
 a value occurs in the original array, you increment
 the counter at that index. At the end, run through your
 counting array, printing the value of each non-zero valued
 index that number of times.
For example, consider an array arr[1,1,2,3,1].
All of the values are in the range(0 to 3) ,
so create an array of zeroes,result = [0,3,1,1].
 The results of each iteration follow

 i	arr[i]	result
0	1	[0, 1, 0, 0]
1	1	[0, 2, 0, 0]
2	3	[0, 2, 0, 1]
3	2	[0, 2, 1, 1]
4	1	[0, 3, 1, 1]
'''


def countingSort(arr):
    m = [0]*100
    for x in arr:
        m[x] += 1
    k = [x for x in range(100) for t in range(0, m[x])]
