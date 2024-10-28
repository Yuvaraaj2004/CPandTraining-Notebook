'''

Created By: _Cypher_0101

'''


from math import log2, ceil, floor, sqrt

# from sortedcontainers import *

from collections import Counter, defaultdict

from functools import cache


mod = 10**9+7


def GetL(type): return map(type, input().split())


def GetS(): return input()


def GetI(): return int(GetS())


def primeFactors(n):
    l = Counter()
    for i in range(2, int(sqrt(n)) + 1):
        while n != 1 and n % i == 0:
            l[i] += 1
            n //= i
        if n == 1:
            break
    if n != 1:
        l[n] += 1
    return sum(l.values())+1


def Solve():

    n = GetI()

    l = [0 for i in range(n+1)]

    for i in range(1, n+1):

        l[i] = primeFactors(i)

    l.pop(0)

    # print(max(l))

    print(*l)

    pass


if __name__ == "__main__":

    for i in range(int(input())):

        Solve()


# 1 2 2 3 2 3 2 4 3 3
# 1 2 2 3 2 4 2 4 3 4
