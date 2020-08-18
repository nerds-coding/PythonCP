def matchingStrings(strings, queries):
    res = [0 for _ in queries]

    for i in strings:
        for index, q in enumerate(queries):
            if(q == i):
                res[index] += 1
    return res


strings = ['aba', 'baba', 'aba', 'xzxb']

queries = ['aba', 'xzxb', 'ab']

print(matchingStrings(strings, queries))
