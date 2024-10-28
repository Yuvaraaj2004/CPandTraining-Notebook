'''
Created at: 13-July-24 20:39
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
    n, l = GetI(), list(GetL())
    if n <= 2:
        print(-1)
    else:
        d = {}
        if n & 1 == 0:
            d[n] = n
            n -= 1
        for i in range(1, n+1):
            d[i] = n-i+1
        print(*[d[i] for i in l])
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
