'''
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache


mod = 10**9+7


def GetL(): return map(int, input().split())


def GetS(): return input()


def GetI(): return int(GetS())


def Solve():
    a, b = GetL()
    d = Counter([1]*a)
    while len(d) == 1 and (v := max(d)) != a:
        v, mn = d[i], min(d)
        if v+mn <= b:
            d[v+mn] += 1
            d[mn] -= 1
            d[v] -= 1
            if d[mn] == 0:
                del d[mn]
            if d[v] == 0:
                del d[v]
        else:

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
