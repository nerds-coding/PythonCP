try:
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        arr2 = list(set(arr))

        if(len(arr2) == 1):
            print(0)
        elif(len(arr) == len(arr2)):
            print(1)
        elif(len(arr2) > 1):
            ind = [[] for _ in range(len(arr2))]

            for i in range(len(arr2)):
                for j in range(len(arr)):
                    if(arr2[i] == arr[j]):
                        ind[i].append(j)

            step = 0
            steps = []
            for x in ind:
                if(x[0] != 0):
                    step += 1
                if(x[-1] != len(arr)-1):
                    step += 1
                if(len(x) > 1):
                    for i in range(len(x)-1):
                        if(x[i+1]-x[i]) > 1:
                            step += 1
                    steps.append(step)
                    step = 0
            print(min(steps))
except:
    pass
