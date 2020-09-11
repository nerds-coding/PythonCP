def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a//gcd(a, b)*b


# for _ in range(int(input())):
#     num = list(map(int, input().split()))
#     print(gcd(num[0], num[1]), lcm(num[0], num[1]))
print(gcd(100, 200), lcm(100, 200))


# lcm is lowest common multiple
