def solve(arr, queries):
    result = []
    queue = [min(queries)]
    m = 2
    for x in arr:
        j = len(queries)-x
        if(j != 0):
            for i in range(j):
                result.append(max(queries[i:i+m]))
                # print(max(queries[i:i+m]))
            m += 1
            queue.append(min(result))

        result = []
    print(queue)


q = [33, 11, 44, 11, 55]
arr = [1, 2, 3, 4, 5]
solve(arr, q)
