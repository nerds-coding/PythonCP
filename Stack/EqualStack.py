def equalStacks(h1, h2, h3):
    s1 = [sum(h1)-sum(h1[0:x]) for x in range(1, len(h1)+1)]
    s2 = [sum(h2)-sum(h2[0:x]) for x in range(1, len(h2)+1)]
    s3 = [sum(h3)-sum(h3[0:x]) for x in range(1, len(h3)+1)]

    for x in s1:
        if(x in s2) and (x in s3):
            return x


s1, s2, s3 = map(sum, (h1, h2, h3))
   while h1 and h2 and h3:
        m = min(s1, s2, s3)
        while s1 > m: s1 -= h1.pop(0)
        while s2 > m: s2 -= h2.pop(0)
        while s3 > m: s3 -= h3.pop(0)
        if s1 == s2 == s3: return s1
    return 0
